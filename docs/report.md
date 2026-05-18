# 1. Title and Author

## Project Title

# Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators

Prepared for UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang

---

## Author Information

- **Author Name:** Aadityaa Dava  
- **Program:** Master’s in Data Science  
- **University:** University of Maryland, Baltimore County (UMBC)  
- **Semester:** Spring 2026  

---

## Project Links

### GitHub Repository
[GitHub Repo link](https://github.com/aadityaa-dava/UMBC-DATA606-Capstone)

### LinkedIn Profile
[LinkedIn Profile link](https://www.linkedin.com/in/aadityaa-dava-688908308)

### PowerPoint Presentation File
[Presentation file](final_presentation.pdf)

### YouTube Presentation Video
[YouTube video link](https://youtu.be/CmFJ-8MSs6c)

---

# 2. Background

## What is the project about?

This project analyzes county-level socioeconomic indicators across the United States using publicly available data from the American Community Survey (ACS).

The analysis focuses on identifying counties that may be at risk of economic decline using indicators such as:
- Median household income
- Poverty rate
- Unemployment rate
- Educational attainment
- Homeownership rate

The project combines:
- Data preprocessing
- Exploratory data analysis
- Economic risk scoring
- Interactive visualizations
- Streamlit dashboard development

to generate interpretable insights about county-level economic conditions.

---

## Why does it matter?

Economic instability affects:
- Employment opportunities
- Household income
- Housing stability
- Educational access
- Community development
- Long-term regional growth

Understanding economic vulnerability at the county level can help:
- Policymakers
- Researchers
- Community organizations
- Economic planners

identify regions that may require targeted intervention, economic investment, or policy support.

This project also demonstrates how publicly available government datasets can be transformed into actionable insights using data science techniques.

---

## Research Questions

1. Which U.S. counties are at the highest risk of economic decline?
2. How do socioeconomic indicators influence economic risk?
3. What relationships exist between poverty, income, education, employment, and housing?
4. Are there geographic disparities in economic vulnerability?
5. Can multiple indicators be combined into an interpretable economic risk score?

---

# 3. Data

## Data Sources

This project uses datasets from the:

# U.S. Census Bureau – American Community Survey (ACS) 5-Year Estimates (2019–2023)

The ACS provides county-level demographic and socioeconomic data across the United States.

---

## ACS Tables Used

| Dataset | Description |
|---|---|
| B01003 | Total Population |
| B19013 | Median Household Income |
| B17001 | Poverty Status |
| B23025 | Employment Status |
| B15003 | Educational Attainment |
| B25003 | Housing Tenure |

Data Source:  
https://data.census.gov/

---

## Dataset Size

- Approximate Size: ~10 MB

---

## Dataset Shape

- Rows: 3,222 counties
- Columns: 9+ engineered socioeconomic features

---

## Time Period

- ACS 5-Year Estimates (2019–2023)

---

## What does each row represent?

Each row in the final dataset represents a single U.S. county containing:
- Demographic indicators
- Socioeconomic variables
- Economic risk metrics

---

## Data Dictionary

| Column Name | Data Type | Definition | Potential Values |
|---|---|---|---|
| county_fips | String | Unique county identifier | 5-digit FIPS code |
| county_name | Text | County and state name | County names |
| total_population | Integer | Total county population | Positive integers |
| median_household_income | Float | Median household income | USD values |
| poverty_rate | Float | Percentage below poverty line | 0–100 |
| unemployment_rate | Float | Percentage unemployed | 0–100 |
| bachelors_or_higher_pct | Float | Percentage with bachelor’s degree or higher | 0–100 |
| homeownership_rate | Float | Percentage of owner-occupied housing | 0–100 |
| renter_rate | Float | Percentage of renter-occupied housing | 0–100 |
| economic_risk_score | Float | Composite economic risk metric | Continuous values |
| risk_category | Category | Economic risk classification | Low / Medium / High |

---

## Target Variable

The target variable used in the project is:

```text
risk_category
```

Categories:
- Low Risk
- Medium Risk
- High Risk

---

## Features / Predictors

Key predictors used in the project include:
- median_household_income
- poverty_rate
- unemployment_rate
- bachelors_or_higher_pct
- homeownership_rate

These indicators represent major dimensions of economic stability and vulnerability.

---

# 4. Exploratory Data Analysis (EDA)

## Data Exploration

EDA was performed using Jupyter Notebook to:
- Understand feature distributions
- Analyze socioeconomic relationships
- Identify patterns and disparities
- Validate data quality

The analysis focused on:
- Poverty
- Income
- Unemployment
- Education
- Homeownership
- Economic risk score

---

## Summary Statistics

The analysis revealed:
- Large variation in income across counties
- Higher poverty in economically distressed counties
- Strong relationships between education and income
- Significant differences in unemployment rates
- Variability in homeownership and stability indicators

---

## Visualizations

Interactive visualizations were created using Plotly Express, including:
- Histograms
- Scatter plots
- Boxplots
- Correlation heatmaps

These visualizations helped identify:
- Distribution patterns
- Outliers
- Correlations between indicators
- Risk category differences

---

## Data Cleansing

### Missing Values
- Minimal missing values were identified
- Handled using median imputation

### Duplicate Rows
- Checked using county FIPS identifiers
- No duplicate counties were found

---

## Data Transformation

The datasets required:
- Cleaning
- Standardization
- Merging
- Feature engineering

ACS datasets were merged using:
```text
county_fips
```

Raw counts were converted into:
- Rates
- Percentages
- Interpretable indicators

---

## Tidy Dataset Structure

The final dataset satisfies tidy data principles:
- Each row represents one county
- Each column represents one unique property of that county

---

## Key Findings from EDA

The analysis showed that high-risk counties generally exhibit:
- Lower household income
- Higher poverty
- Higher unemployment
- Lower educational attainment
- Lower homeownership

These findings validate the selected features used in the economic risk framework.

---

# 5. Model Training

## Modeling Approach

This project uses an interpretable composite economic risk scoring framework instead of a black-box machine learning model.

Multiple socioeconomic indicators were combined into a single economic risk score representing county-level vulnerability.

---

## Economic Risk Score

The score incorporates:
- Poverty rate
- Unemployment rate
- Income
- Educational attainment
- Homeownership rate

Indicators associated with economic instability increase the risk score, while indicators associated with economic stability reduce the score.

---

## Risk Classification

Counties were categorized into:
- Low Risk
- Medium Risk
- High Risk

based on score thresholds derived from the score distribution.

---

## Python Packages Used

- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit

---

## Development Environment

The project was developed using:
- Jupyter Notebook
- Local Python environment
- Streamlit

---

## Model Validation

The scoring framework was evaluated using:
- Correlation analysis
- Distribution analysis
- County comparisons
- Risk category consistency checks

High-risk counties consistently showed:
- Higher poverty
- Higher unemployment
- Lower education
- Lower income
- Lower homeownership

---

# 6. Application of the Trained Models

## Streamlit Dashboard

An interactive Streamlit application was developed to allow users to explore county-level socioeconomic indicators and economic risk patterns.

---

## Dashboard Features

The application allows users to:
- Explore county-level data
- Compare counties across indicators
- Visualize risk scores
- Analyze socioeconomic trends
- Interact with dynamic visualizations

---

## Technologies Used

- Streamlit
- Plotly
- Pandas
- NumPy

---

## Purpose of the Application

The dashboard transforms complex socioeconomic datasets into interpretable visual insights that support:
- Data exploration
- Educational analysis
- Policy understanding
- Public awareness

---

# 7. Conclusion

## Summary of Work

This project analyzed county-level socioeconomic indicators across the United States to identify regions potentially vulnerable to economic decline.

Using publicly available ACS data, the project:
- Built a structured preprocessing pipeline
- Developed an interpretable economic risk scoring methodology
- Performed exploratory data analysis
- Created an interactive Streamlit dashboard

---

## Potential Applications

The project can support:
- Economic research
- Policy analysis
- Community planning
- Regional socioeconomic monitoring
- Educational and analytical exploration

---

## Limitations

Several limitations exist:
- ACS data are survey estimates
- Cross-sectional analysis limits temporal interpretation
- Risk thresholds simplify complex economic conditions
- Additional variables could improve the analysis

---

## Lessons Learned

This project provided practical experience in:
- Data preprocessing
- Exploratory data analysis
- Feature engineering
- Risk modeling
- Dashboard development
- Data storytelling and visualization

---

## Future Research Directions

Future improvements may include:
- Time-series analysis
- Geographic mapping
- Advanced machine learning models
- Additional socioeconomic indicators
- Cloud deployment of the dashboard

---

# 8. References

1. U.S. Census Bureau – American Community Survey (ACS)  
https://data.census.gov/

2. Streamlit Documentation  
https://docs.streamlit.io/

3. Plotly Documentation  
https://plotly.com/python/

4. Scikit-learn Documentation  
https://scikit-learn.org/

5. Pandas Documentation  
https://pandas.pydata.org/

6. NumPy Documentation  
https://numpy.org/

7. Jupyter Notebook Documentation  
https://jupyter.org/
