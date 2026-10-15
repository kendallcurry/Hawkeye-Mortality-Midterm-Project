"""
Clean the CDC county export for Iowa data
- keep real Iowa county rows (FIPS)
- sort alphabetically ordered counties and number them 1-99
- shorten county names
- drop Notes column, the "Total" row, and the footer/citation text

Run once in the terminal first:  pip install pandas
"""

import pandas as pd

IN_FILE = "Underlying Cause of Death, 2018-2024, Single Race (1).csv"
OUT_FILE = "iowa_mortality_clean.csv"

# 1. Read everything as text
raw = pd.read_csv(IN_FILE, dtype=str, on_bad_lines="skip")

# 2. Keep only rows with a valid 5-digit Iowa FIPS code
#    (this removes the Total row and all the notes/caveats at the bottom)
df = raw[raw["County Code"].fillna("").str.strip().str.match(r"^19\d{3}$")].copy()
df = df.drop(columns=["Notes"])

# 3. Tidy columns: short county name, numeric values
df["County Name"] = df["County"].str.replace(" County, IA", "", regex=False)
num_cols = ["Deaths", "Population", "Crude Rate",
            "Crude Rate Lower 95% Confidence Interval",
            "Crude Rate Upper 95% Confidence Interval"]

for col in num_cols:
    df[col] = pd.to_numeric(df[col].str.replace(",", ""), errors="coerce")

# 4. Sort alphabetically and number 1..N
df = df.sort_values("County Name", key=lambda s: s.str.lower()).reset_index(drop=True)
df.insert(0, "No.", range(1, len(df) + 1))

# 5. Reorder columns and save
df = df[["No.", "County Name", "County", "County Code"] + num_cols]
df.to_csv(OUT_FILE, index=False)

print(f"Kept {len(df)} counties (Iowa has 99).")
if len(df) != 99:
    print("Warning: count isn't 99 — check for missing or suppressed counties.")
print(df.head(10).to_string(index=False))

"""
Map Iowa's 2022 crude death rates by county.

Output: iowa_mortality_map.html  
"""

import json
from urllib.request import urlopen

import pandas as pd
import plotly.express as px

IN_FILE = "iowa_mortality_clean.csv"
OUT_FILE = "iowa_mortality_map.html"
STATE_RATE = 1061.5   # Iowa's overall crude rate, from CDC's Total row

# 1. Load the cleaned data (keep county rows only)
df = pd.read_csv(IN_FILE, dtype=str, on_bad_lines="skip")
df = df[df["County Code"].fillna("").str.match(r"^19\d{3}$")].copy()
for col in ["Deaths", "Population", "Crude Rate"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 2. Download county boundary shapes, keyed by 5-digit FIPS code
URL = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
with urlopen(URL) as resp:
    counties = json.load(resp)
# keep only Iowa's shapes 
counties["features"] = [f for f in counties["features"] if f["id"].startswith("19")]

# 3. Draw the map
fig = px.choropleth(
    df,
    geojson=counties,
    locations="County Code",          # matches each row to a county shape by FIPS
    color="Crude Rate",
    color_continuous_scale="Reds",
    hover_name="County Name",
    hover_data={"County Code": False, "Crude Rate": ":.1f",
                "Deaths": ":,", "Population": ":,"},
    labels={"Crude Rate": "Deaths per 100,000"},
)
fig.update_geos(fitbounds="locations", visible=False)   # zoom to Iowa, hide the rest
fig.update_layout(
    title=f"Crude death rate by county, Iowa 2022 (state rate: {STATE_RATE})",
    margin=dict(l=0, r=0, t=50, b=0),
)

# 4. Save and open
fig.write_html(OUT_FILE)
print(f"Saved {OUT_FILE} ({len(df)} counties). Opening in your browser...")
fig.show()

fig.write_image("iowa_mortality_map.png", scale=3) 
