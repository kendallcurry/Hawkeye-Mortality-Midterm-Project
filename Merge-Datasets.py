import pandas as pd

## Load data
social_df = pd.read_csv("iowa_social_capital.csv")
mortality_df = pd.read_csv("iowa_mortality_clean.csv")
age_df = pd.read_csv("age_data_clean.csv")

## Check columns
print("Social Capital:", social_df.columns.tolist())
print("Mortality:", mortality_df.columns.tolist())
print("Age:", age_df.columns.tolist())

## Make FIPS codes consistent
social_df = social_df.rename(columns={"county": "FIPS"})
mortality_df = mortality_df.rename(columns={"County Code": "FIPS"})

social_df["FIPS"] = pd.to_numeric(social_df["FIPS"]).astype(int)
mortality_df["FIPS"] = pd.to_numeric(mortality_df["FIPS"]).astype(int)
age_df["FIPS"] = pd.to_numeric(age_df["FIPS"]).astype(int)

## Check county counts
print("Social Capital:", social_df["FIPS"].nunique())
print("Mortality:", mortality_df["FIPS"].nunique())
print("Age:", age_df["FIPS"].nunique())

## Merge datasets
merged_df = pd.merge(social_df, mortality_df, on="FIPS", how="inner", validate="one_to_one")
merged_df = pd.merge(merged_df, age_df, on="FIPS", how="inner", validate= "one_to_one")

## Check merged data
print("Merged dataset shape:", merged_df.shape)
print("Number of counties:", merged_df["FIPS"].nunique())
print(merged_df[["FIPS", "county_name", "ec_county", "Crude Rate", "Percent_65+"]].head())
print(merged_df[["ec_county", "Crude Rate", "Percent_65+"]]
      .isna()
      .sum())
merged_df.to_csv("iowa_merged_data.csv", index=False)
