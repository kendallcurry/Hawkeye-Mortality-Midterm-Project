import pandas as pd
df = pd.read_csv("social_capital_county.csv")
print(df.head())
df["county"] = pd.to_numeric(df["county"])
iowa_df = df[(df["county"] // 1000) == 19].copy()
print("Number of Iowa Counties:", iowa_df["county"].nunique())
iowa_df.to_csv("iowa_social_capital.csv", index=False)
print("Iowa dataset shape:", iowa_df.shape)
