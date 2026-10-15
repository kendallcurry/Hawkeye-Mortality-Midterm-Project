import pandas as pd
import json
from urllib.request import urlopen

import pandas as pd
import plotly.express as px

IN_FILE = "age_data_clean.csv"
OUT_HTML = "age_map.html"
OUT_PNG = "age_map.png"
STATE_RATE = 18.1

df = pd.read_csv('age_data_clean.csv')

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
    locations="FIPS",          # matches each row to a county shape by FIPS
    color="Percent_65+",
    color_continuous_scale="Greens",
    hover_name="County",
    hover_data={"FIPS": False, "Percent_65+": ":.1f"},
    labels={"Percent_65+": "Percent of Population Age 65 and Older"},
)
fig.update_geos(fitbounds="locations", visible=False)   # zoom to Iowa, hide the rest
fig.update_layout(
    title=f"Percent of Population Age 65 and Older, Iowa 2020-2024 (state rate: {STATE_RATE})",
    margin=dict(l=0, r=0, t=50, b=0),
)

# 4. Save and open
fig.write_html(OUT_HTML)