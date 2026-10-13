import pandas as pd
df = pd.read_csv("social_capital_county.csv")
print(df.head())
df["county"] = pd.to_numeric(df["county"])
iowa_df = df[(df["county"] // 1000) == 19].copy()
print("Number of Iowa Counties:", iowa_df["county"].nunique)

