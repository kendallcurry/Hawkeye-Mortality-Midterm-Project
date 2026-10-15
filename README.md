# Hawkeye Mortality Midterm
####  Group: Hawkeye Mortality 
Julia Kapusta, Kendall Curry, and Kevin Szybist
## Project Overview
The goal of our project is to investigate the relationship between social connectedness and mortality rates. We chose to focus our initial analysis on counties in Iowa because they have relatively little variation in population size, land area, and population density. This allows for more consistent comparisons across counties. Additionally, we chose to incorporate county-level age data into our exploration because age is one the primary factors associated with mortality. By accounting for differences in age across counties, we hope to better understand whether a statistically significant relationship exists between social connectedness and mortality rates. 

## Data
Our project uses three county level datasets to investigate the relationship between social connectedness and mortality rates across Iowa's 99 counties. These datasets provide information on economic connectedness, mortality, and the proportion of residents aged 65 and older. 

### Data Sources 
The datasets used in this project were obtained from publicly available sources:
- Social Capital: Opportunity Insights, Social Capital Atlas. This dataset provides county level economic connectedness measures.
- Mortality: Centers for Disease Control and Prevention (CDC), Underlying Cause of Death, 2018-2024, Single Race. This dataset provides county level mortality information.
- Population Aged 65 and Older: County level age data used to examine differences in the elderly population across Iowa counties. The original source and reference year will be added once confirmed.

### Economic Connectedness
Economic connectedness measures the extent to which individuals from lower socioeconomic backgrounds form friendships with individuals from higher socioeconomic backgrounds. According to Opportunity Insights, economic connectedness is calculated as twice the average share of higher socioeconomic status friends among lower socioeconomic status individuals. 

A value of 1.0 indicates that approximately 50% of the friendships of lower socioeconomic status individuals are with higher socioeconomic status individuals. Values below 1.0 indicate lower levels of cross income connectedness, while above 1.0 indicate higher levels. 

In our Iowa county level data, economic connectedness values range from approximately 0.62 to 1.21. Higher values represent greater social interaction across socioeconomic groups, while lower values suggest that friendships are more concentrated among individuals of similar socioeconomic backgrounds.


## Data Cleaning and Preprocessing
### Social Capital Data
Starting with the Social_Capital_County.csv , we filtered the data to include only counties within the state of Iowa. This allowed us to narrow our analysis to the 99 Iowa counties relevant to our research question. The counties were then sorted alphabetically and assigned a numerical index ranging from 1 (Adair County) to 99 (Wright County). This indexing system will be kept consistent throughout the analysis to ensure that counties can be easily identified and compared across dataset.
We also examined the economic connectedness measure, which one of the indicators of social capital included in the dataset. This measure will be used to investigate potential relationships between social connectedness and mortality rates across Iowa counties.

### Mortality Data
For the Underlying Cause of Death, 2018-2024, Single Race (1).csv , we made sure that the counties were alphabetically ordered and assigned a numerical index ranging from 1 (Adair County) to 99 (Wright County) to match seamlessly with the Social Capital county data. To make the data cleaner, we also got rid of the notes column included in the CDC data, shortened the name of the county without the state abbreviation, and got rid of the total row. 

### Age Data

### Merging the Three Datasets
After cleaning the three datasets individually, we combined them into one dataset containing information on economic connectedness, mortality rates, and the percentage of residents 65 and older across Iowa counties. We first made sure that the FIPS codes were consistent across all three datasets by renaming the relevant columns and converting the codes to integers. Using Python's panda library, we then merged based on their FIPS codes. We used inner joins to match the datasets based on county FIPS codes and checked that each county appeared only once in the dataset. After merging, we confirmed all 99 counties were still included in the final dataset. The final merged dataset contains 99 counties and 37 columns. We also checked for missing values in our three main variables (ec_county , Crude Rate, and Percent_65+) to make sure the data was ready for futher analysis. The final dataset was saved as iowa_merged_data.csv. 

## Methodology

## Results and Visualizations
### Population Aged 65 and Older Across Iowa Counties

![Percentage of Population Aged 65 and Older](percent-of-population-age-65-and-older-i.png)
#### Iowa Mortality Map

![Crude Death Rate by Iowa County, 2022](iowa_mortality_map.png)
### Economic Connectedness Visualization
To further explore differences in economic connectedness across Iowa counties, we created a horizontal bar chart comparing the 10 counties with the lowest values. Using Python's pandas library, we identified these counties with the nlargest() and nsmallest() functions and combined them into a single dataset for visualization. We then used Matplotlib to construct the bar chart, displaying county names along the vertical axis and economic connectedness values along the horizontal axis. This visualization allows us to identify variation in economic connectedness across Iowa counties and provides an initial descriptive comparison before investing its relationship with mortality rates. 



## Findings and Interpretations
## Limitations and Future Research
## Reproducibility
