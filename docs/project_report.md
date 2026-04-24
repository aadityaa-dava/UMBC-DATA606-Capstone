# U.S. County Economic Risk Analysis

---

## 1. Title and Author

- **Project Title**: Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators  
- **Author**: Aadityaa Dava  
- **Semester**: Spring 2026  
- **Program**: Master’s in Data Science  
- **Instructor**: Dr. Chaojie (Jay) Wang  

- **GitHub Repository**:  
  https://github.com/aadityaa-dava/UMBC-DATA606-Capstone  

- **LinkedIn Profile**:  
  https://www.linkedin.com/in/aadityaa-dava-688908308  

---

## 2. Background

### Project Overview

This project aims to identify U.S. counties that may be at risk of economic decline using publicly available data from the **American Community Survey (ACS)**.

Key socioeconomic indicators used in the analysis include:

- Median household income  
- Poverty rate  
- Unemployment rate  
- Educational attainment  
- Homeownership rate  

These indicators are combined into a **composite economic risk score**, which is used to classify counties into:

- Low Risk  
- Medium Risk  
- High Risk  

The results are presented through:

- Interactive visualizations  
- A Streamlit-based dashboard  
- An interpretable scoring methodology  

---

### Motivation

Economic decline impacts multiple aspects of community well-being, including:

- Employment opportunities  
- Income levels  
- Poverty conditions  
- Housing stability  
- Access to education and healthcare  

By identifying high-risk counties, this project helps highlight regions that may require:

- Policy attention  
- Economic investment  
- Targeted interventions  

Additionally, this work demonstrates how publicly available data can be transformed into **actionable insights for decision-making**.

---

### Research Questions

1. Which U.S. counties are at the highest risk of economic decline?  
2. How do income, poverty, unemployment, education, and homeownership influence economic risk?  
3. What patterns exist across counties for these indicators?  
4. Are there geographic trends in economic risk?  
5. Can multiple indicators be combined into a clear and interpretable risk score?  

---

## 3. Data

### Data Source

This project uses data from the **U.S. Census Bureau – American Community Survey (ACS) 5-Year Estimates (2019–2023)**.

The ACS provides reliable, publicly available socioeconomic data at the county level.

**Tables used:**

- B01003 – Total Population  
- B19013 – Median Household Income  
- B17001 – Poverty Status  
- B23025 – Employment Status  
- B15003 – Educational Attainment  
- B25003 – Housing Tenure  

🔗 https://data.census.gov/table?g=010XX00US$0500000  

---

### Dataset Summary

- **Size**: ~10 MB  
- **Rows**: 3,222 counties  
- **Columns**: 9+ features (including engineered variables)  
- **Time Period**: 2019–2023 (ACS 5-Year Estimates)  

---

### Unit of Analysis

Each row represents a **single U.S. county**, including demographic and socioeconomic indicators along with computed risk metrics.

---

### Data Dictionary

| Column Name | Data Type | Description |
|------------|----------|-------------|
| county_fips | String | Unique 5-digit county identifier |
| county_name | Text | County and state name |
| total_population | Integer | Total population |
| median_household_income | Float | Median household income (USD) |
| poverty_rate | Float | Percentage below poverty line |
| unemployment_rate | Float | Percentage unemployed |
| bachelors_or_higher_pct | Float | Percentage with bachelor's degree or higher |
| homeownership_rate | Float | Percentage of owner-occupied housing |
| renter_rate | Float | Percentage of renter-occupied housing |
| economic_risk_score | Float | Composite economic risk score |
| risk_category | Category | Low / Medium / High |

---

### Target Variable

- **risk_category** (Low, Medium, High)

---

### Features / Predictors

- median_household_income  
- poverty_rate  
- unemployment_rate  
- bachelors_or_higher_pct  
- homeownership_rate  

These variables represent key dimensions of economic health.

---

## 4. Exploratory Data Analysis (EDA)

### Overview

Exploratory Data Analysis (EDA) was conducted to understand the dataset, validate data quality, and uncover relationships between socioeconomic indicators.

The analysis focused on:

- Income  
- Poverty  
- Unemployment  
- Education  
- Homeownership  

Key objectives:

- Understand distributions  
- Identify relationships  
- Detect anomalies  
- Prepare data for modeling  

---

### Summary Statistics & Observations

- **Median Household Income**
  - Large variation across counties  
  - Reflects economic disparities  

- **Poverty Rate**
  - Right-skewed distribution  
  - Some counties exhibit very high poverty  

- **Unemployment Rate**
  - Concentrated at lower values  
  - Outliers indicate distressed regions  

- **Education Level**
  - Wide variation across counties  
  - Strong indicator of economic potential  

- **Homeownership Rate**
  - Generally high but still informative  
  - Linked to economic stability  

- **Economic Risk Score**
  - Combines multiple indicators into a single interpretable metric  

---

### Visual Analysis (Plotly)

#### Distribution Analysis
Histograms were used to examine:

- Income  
- Poverty  
- Unemployment  
- Education  
- Homeownership  

These revealed skewness, spread, and outliers.

---

#### Relationship Analysis

Scatter plots explored relationships such as:

- Income vs Poverty  
- Education vs Income  
- Unemployment vs Poverty  

---

#### Correlation Analysis

A correlation heatmap showed:

- Income negatively correlated with poverty  
- Income positively correlated with education  
- Poverty positively correlated with unemployment  
- Education negatively correlated with poverty  

---

#### Risk-Based Analysis

- Distribution of counties across risk categories  
- Boxplots of risk score by category  
- Comparison of indicators across risk levels  

These confirmed that the risk categories meaningfully differentiate counties.

---

### Key Relationships

- Higher income → Lower poverty  
- Higher education → Higher income  
- Higher unemployment → Higher poverty  
- Higher homeownership → Greater stability  

These relationships validate the feature selection for modeling.

---

### Data Quality Assessment

#### Missing Values
- Minimal missing values  
- Handled using **median imputation**  

#### Duplicates
- Checked using `county_fips`  
- No duplicates found  

---

### Data Transformations

- Merged multiple ACS datasets using `county_fips`  
- Converted raw counts into rates  
- Engineered meaningful features  
- Split `county_name` into county and state  

---

### Key Findings

- Significant economic variation exists across U.S. counties  
- Economic risk is driven by multiple interrelated factors  
- High-risk counties consistently show:
  - Lower income  
  - Higher poverty  
  - Higher unemployment  
  - Lower education  
  - Lower homeownership  

- The composite risk score effectively captures these patterns  

---
