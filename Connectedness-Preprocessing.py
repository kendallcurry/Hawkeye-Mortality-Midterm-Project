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