import os
import pandas as pd

df = pd.read_csv('iowa_65older_by_county.csv',header=3)

df_drop = df.drop(columns = ['People (Age 65 And Over)','Rank within US (of 3143 counties)'])

df_county = df_drop.loc[~df_drop['County'].isin(['United States','Iowa'])
                   & df_drop['FIPS'].notna()]

#calculate and print summary statistics
q1 = df_county['Percent'].quantile(0.25)
q3 = df_county['Percent'].quantile(0.75)
iqr = q3 - q1

print("Mean:", df_county['Percent'].mean())
print("Median:", df_county['Percent'].median())
print("Minimum:", df_county['Percent'].min())
print("Maximum:", df_county['Percent'].max())
print("Range:", df_county['Percent'].max() - df_county['Percent'].min())
print("Standard deviation:", df_county['Percent'].std())
print("IQR:", iqr)

df_renamed = df_county.rename(columns={'Percent': 'Percent_65+'})

df_renamed.to_csv('age_data_clean.csv', index = False)