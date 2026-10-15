import pandas as pd
social_df = pd.read_csv("iowa_social_capital.csv")
mortality_df = pd.read_csv("iowa_mortality_clean.csv")
age_df = pd.read_csv("age_data_clean.csv")

print("Social Capital:", social_df.columns.tolist())
print("Mortality:", mortality_df.columns.tolist())
print("Age:", age_df.columns.tolist())
social_df = social_df.rename(columns={"county": "FIPS"})
mortality_df = mortality_df.rename(columns={"County Code": "FIPS"})

social_df["FIPS"] = pd.to_numeric(social_df["FIPS"]).astype(int)
mortality_df["FIPS"] = pd.to_numeric(mortality_df["FIPS"]).astype(int)
age_df["FIPS"] = pd.to_numeric(age_df["FIPS"]).astype(int)

print("Social Capital:", social_df["FIPS"].nunique())
print("Mortality:", mortality_df["FIPS"].nunique())
print("Age:", age_df["FIPS"].nunique())

merged_df = pd.merge(social_df, mortality_df, on="FIPS", how="inner", validate="one_to_one")
merged_df = pd.merge(merged_df, age_df, on="FIPS", how="inner", validate= "one_to_one")
print("Merged dataset shape:", merged_df.shape)
print("Number of counties:", merged_df["FIPS"].nunique())
print(merged_df[["FIPS", "county_name", "ec_county", "Crude Rate", "Percent_65+"]].head())
print(merged_df[["ec_county", "Crude Rate", "Percent_65+"]]
      .isna()
      .sum())
merged_df.to_csv("iowa_merged_data.csv", index=False)
