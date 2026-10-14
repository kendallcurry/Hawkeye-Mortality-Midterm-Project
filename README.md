# Hawkeye Mortality Midterm
#### Hawkeye Mortality 
## Project Overview
The goal of our project is to investigate the relationship between social connectedness and mortality rates. We chose to focus our initial analysis on counties in Iowa because they have relatively little variation in population size, land area, and population density. This allows for more consistent comparisons across counties. Additionally, we chose to incorporate county-level age data into our exploration because age is one the primary factors associated with mortality. By accounting for differences in age across counties, we hope to better understand whether a statistically significant relationship exists between social connectedness and mortality rates. 

### Data sets


## Data Cleaning and Preprocessing
Starting with the Social_Capital_County.csv , we filtered the data to include only counties within the state of Iowa. This allowed us to narrow our analysis to the 99 Iowa counties relevant to our research question. The counties were then sorted alphabetically and assigned a numerical index ranging from 1 (Adair County) to 99 (Wright County). This indexing system will be kept consistent throughout the analysis to ensure that counties can be easily identified and compared across dataset.
We also examined the economic connectedness measure, which one of the indicators of social capital included in the dataset. This measure will be used to investigate potential relationships between social connectedness and mortality rates across Iowa counties.

For the Underlying Cause of Death, 2018-2024, Single Race (1).csv , we made sure that the counties were alphabetically ordered and assigned a numerical index ranging from 1 (Adair County) to 99 (Wright County) to match seamlessly with the Social Capital county data. To make the data cleaner, we also got rid of the notes column included in the CDC data, shortened the name of the county without the state abbreviation, and got rid of the total row. 
