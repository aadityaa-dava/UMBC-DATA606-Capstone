
## 1. Title and Author

- Project Title -  **Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators**
- Author - *Aadityaa Dava*
- Semester - Spring'26
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Link to the author's GitHub repo of the project: https://github.com/aadityaa-dava/UMBC-DATA606-Capstone
- Link to the author's LinkedIn profile: www.linkedin.com/in/aadityaa-dava-688908308
    
## 2. Background

- **What is it about?**

The project focuses on identifying counties in the United States that may be at risk of economic decline based on actual data of the American Community Survey (ACS). I rely on such valuable clues as the level of income, the degree of poverty, unemployment, education, and homeownership to know the economic situation in this or that county. All these factors are put together as one economic risk score, which assists in ranking the counties as to low, medium, and high risk. This analysis will be made transparent and easy to understand and the results will be presented in a streamlit application and interactive visualizations so that the users can explore and understand the economic risk of an entire country in a very simple manner.

- **Why does it matter?**

The significance of this project is that the economic issues have an impact on ordinary life. A people may find it difficult to secure employment, income levels will be reduced and poverty levels will rise when a county begins to deteriorate. This may also spill over to schools, health services, accommodation, and general standards of living. It is possible to determine counties that are potentially at increased risk and, in this way, comprehend communities that could require more support and attention.

It is also important as it converts raw data into something useful and easily comprehensible. This project does not consider a single number, such as income or unemployment, but a combination of several meaningful indicators into a single risk score. It is thus more convenient to match counties with each other in a clear and fair manner. It demonstrates how one can use public data to draw insights that can make people make better decisions.

**What are your research questions?**

1. Which U.S. counties are at the highest risk of economic decline based on key socioeconomic indicators?

2. How do income, poverty, unemployment, education, and homeownership together influence a county's economic risk?

3. Are there noticeable geographic patterns in economic risk across different states or regions?

4. Can we create a clear and transparent scoring method that combines multiple indicators into one meaningful economic risk score?

## 3. Data 

**Data sources**

- This project uses data from the U.S. Census Bureau’s American Community Survey (ACS) 5-Year Estimates. The ACS is a nationally recognized and reliable public dataset that provides detailed socioeconomic information at the county level.

The specific ACS tables used include:

* Total Population (B01003) – to understand county size

* Median Household Income (B19013) – to measure economic strength

* Poverty Rate (B17001) – to measure economic hardship

* Unemployment Rate (B23025) – to measure labor market conditions

* Education Level (B15003) – percentage of adults with a bachelor’s degree or higher

* Homeownership Rate (B25003) – to understand housing stability

All datasets are publicly available from the U.S. Census Bureau website and were merged using county codes to create a unified county-level dataset for analysis.

https://data.census.gov/table?g=010XX00US$0500000

**Data size**

~10 MB

**Final Shape**
- Number of rows: 3222
- Number of columns: 9

**Time period:** 
- 5-Year Estimates (2019–2023)
 
**What does each row represent?**
- Each row represents one U.S. county.

More specifically, each row contains the socioeconomic data for a single county with its Population, Median household income, Poverty rate, Unemployment rate, Education level (Bachelor’s or higher %), Homeownership rate, Calculated economic risk score and Risk category(derived)
 
**Data dictionary**

| Column Name | Data Type | Definition | Potential Values |
|------------|----------|------------|------------------|
| county_fips | String (5-digit code) | Unique FIPS identifier for each U.S. county | 01001, 06037, 17031 |
| county_name | Text | Full county name including state | Autauga County, Alabama |
| total_population | Numeric (Integer) | Total population of the county | Positive integers |
| median_household_income | Numeric (Float) | Median annual household income (USD) | 16,000 – 180,000+ |
| poverty_rate | Numeric (Float, 0–1) | Proportion of population below poverty line | 0.01 – 0.63 |
| unemployment_rate | Numeric (Float, 0–1) | Proportion of labor force unemployed | 0.00 – 0.28 |
| bachelors_or_higher_pct | Numeric (Float, 0–1) | Proportion of adults with bachelor’s degree or higher | 0.00 – 0.80 |
| homeownership_rate | Numeric (Float, 0–1) | Proportion of housing units that are owner-occupied | 0.00 – 0.96 |
| renter_rate | Numeric (Float, 0–1) | Proportion of housing units that are renter-occupied | 0.04 – 1.00 |
| economic_risk_score | Numeric (Float, 0–1) | Composite risk score calculated from normalized socioeconomic indicators | 0.00 – 1.00 |
| risk_category | Categorical | Risk group assigned using quantile-based classification | Low Risk, Medium Risk, High Risk |

**Which variable/column will be your target/label in your ML model?**
- The data does not include an already computed target column. The target was created in our analysis by constructing an economic risk score out of several socioeconomic indicators.
- The **risk level (Low Risk, Medium Risk, High Risk)** will be considered as the target variable.
  
**Which variables/columns may be selected as features/predictors for your ML models?**
- The ML model characteristics will be chosen among the key socioeconomic variables in the dataset: median household income, poverty rate, unemployment rate, percentage of people with a bachelor degree and higher, and homeownership rate.
- The reason why these variables are selected is that they directly indicate the economic situation in a county and can be used to explain the reason behind a county becoming low, medium, or high economic risk.
