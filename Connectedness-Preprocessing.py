import pandas as pd
df = pd.read_csv("social_capital_county.csv")
print(df.head())
df["county"] = pd.to_numeric(df["county"])
iowa_df = df[(df["county"] // 1000) == 19].copy()
iowa_df = iowa_df.sort_values("county_name").reset_index(drop=True)
iowa_df.insert(0, "county_index", range(1, len(iowa_df) + 1))
print("Number of Iowa Counties:", iowa_df["county"].nunique())
iowa_df.to_csv("iowa_social_capital.csv", index=False)
print("Iowa dataset shape:", iowa_df.shape)
print(iowa_df[["county_name", "county"]].head((15)))

import matplotlib.pyplot as plt
lowest = iowa_df.nsmallest(10, "ec_county")
highest = iowa_df.nlargest(10, "ec_county")
graph_df = pd.concat([lowest,highest])
graph_df["county_name"] = graph_df["county_name"].str.replace(", Iowa", "", regex=False)
graph_df.plot.barh(
    x="county_name",
    y="ec_county",
    figsize=(10, 8),
    legend=False
)
plt.title("Most and Least Economically Connected Iowa Counties")
plt.xlabel("Economic Connectedness")
plt.ylabel("County")
plt.tight_layout()
plt.savefig("iowa_connectedness_chart.png", dpi=300, bbox_inches="tight")
plt.show()
