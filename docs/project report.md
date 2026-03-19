# U.S. County Economic Risk Analysis

## 1. Title and Author

- **Project Title**: Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators  
- **Author**: Aadityaa Dava  
- **Semester**: Spring 2026  
- **Program**: UMBC Data Science Master's Degree Capstone  
- **Instructor**: Dr. Chaojie (Jay) Wang  

- **GitHub Repository**:  
  https://github.com/aadityaa-dava/UMBC-DATA606-Capstone  

- **LinkedIn Profile**:  
  https://www.linkedin.com/in/aadityaa-dava-688908308  

---

## 2. Background

### What is this project about?

This project focuses on identifying counties in the United States that may be at risk of economic decline using data from the American Community Survey (ACS).

Key socioeconomic indicators used include:
- income
- poverty
- unemployment
- education
- homeownership

These indicators are combined into a **composite economic risk score**, which is used to classify counties into:
- Low Risk  
- Medium Risk  
- High Risk  

The results are presented through:
- interactive visualizations  
- a Streamlit dashboard  
- an interpretable scoring methodology  

---

### Why does this matter?

Economic decline directly affects:
- employment opportunities  
- income levels  
- poverty rates  
- housing stability  
- access to education and healthcare  

By identifying high-risk counties, this project helps highlight areas that may need:
- policy attention  
- economic support  
- targeted interventions  

Additionally, this project demonstrates how publicly available data can be transformed into **actionable insights**.

---

### Research Questions

1. Which U.S. counties are at the highest risk of economic decline?  
2. How do income, poverty, unemployment, education, and homeownership influence economic risk?  
3. What are the distributions and patterns of these indicators across counties?  
4. Are there geographic patterns in economic risk across states or regions?  
5. Can multiple indicators be combined into a clear and interpretable risk score?  

---

## 3. Data

### Data Source

This project uses data from the **U.S. Census Bureau – American Community Survey (ACS) 5-Year Estimates**.

The ACS provides reliable, publicly available socioeconomic data at the county level.

**Tables used:**

- Total Population (B01003)  
- Median Household Income (B19013)  
- Poverty (B17001)  
- Unemployment (B23025)  
- Education (B15003)  
- Homeownership (B25003)  

🔗 https://data.census.gov/table?g=010XX00US$0500000  

---

### Data Size

- ~10 MB  

### Final Shape

- Rows: **3,222 counties**  
- Columns: **9+ features (including derived variables)**  

### Time Period

- **ACS 5-Year Estimates (2019–2023)**  

---

### What does each row represent?

Each row represents **one U.S. county**, including:

- population  
- income  
- poverty rate  
- unemployment rate  
- education level  
- homeownership rate  
- calculated economic risk score  
- risk category  

---

### Data Dictionary

| Column Name | Data Type | Description |
|------------|----------|-------------|
| county_fips | String | Unique 5-digit county identifier |
| county_name | Text | County + State |
| total_population | Integer | County population |
| median_household_income | Float | Median income (USD) |
| poverty_rate | Float | % below poverty line |
| unemployment_rate | Float | % unemployed |
| bachelors_or_higher_pct | Float | % with bachelor's degree |
| homeownership_rate | Float | % owner-occupied housing |
| renter_rate | Float | % renter-occupied housing |
| economic_risk_score | Float | Composite risk score |
| risk_category | Category | Low / Medium / High |

---

### Target Variable

- **risk_category (Low, Medium, High)**  

---

### Features / Predictors

- median_household_income  
- poverty_rate  
- unemployment_rate  
- bachelors_or_higher_pct  
- homeownership_rate  

These variables directly represent economic conditions.

---

## 4. Exploratory Data Analysis (EDA)

### Overview

Exploratory Data Analysis (EDA) was conducted to gain a deeper understanding of the dataset, validate data quality, and uncover meaningful patterns across U.S. counties.

The analysis focused on the key socioeconomic indicators used to construct the economic risk score:
- income
- poverty
- unemployment
- education
- homeownership

The primary goals of EDA were to:
- understand variable distributions  
- identify relationships between indicators  
- detect data quality issues  
- ensure readiness for modeling and visualization  

---

### Summary Statistics & Insights

The dataset contains 3,222 U.S. counties, each with multiple socioeconomic indicators.

Key observations:

- **Median Household Income**
  - Shows significant variation across counties  
  - Indicates strong differences in economic strength and opportunity  

- **Poverty Rate**
  - Right-skewed distribution  
  - Most counties have moderate poverty, but a subset experiences very high poverty  

- **Unemployment Rate**
  - Concentrated at lower values  
  - Contains outliers representing economically distressed counties  

- **Education (Bachelor’s or Higher %)**
  - Wide variation across counties  
  - Reflects differences in workforce skill levels  

- **Homeownership Rate**
  - Generally high across counties  
  - Still provides meaningful variation related to economic stability  

- **Economic Risk Score**
  - Effectively combines all indicators into a single interpretable metric  
  - Allows direct comparison across counties  

---

### Visualizations (Plotly)

Interactive visualizations were created using Plotly Express to explore patterns and relationships:

#### Distribution Analysis
- Histograms were used to analyze the spread and skewness of each indicator:
  - median_household_income  
  - poverty_rate  
  - unemployment_rate  
  - bachelors_or_higher_pct  
  - homeownership_rate  

These visualizations highlighted variability and outliers across counties.

#### Relationship Analysis
- Scatter plots were used to understand relationships between variables:
  - Income vs Poverty  
  - Education vs Income  
  - Unemployment vs Poverty  

#### Correlation Analysis
- A correlation heatmap was used to quantify relationships between variables:
  - Income has a strong negative correlation with poverty  
  - Income has a strong positive correlation with education  
  - Poverty has a positive correlation with unemployment  
  - Education has a negative relationship with poverty  

#### Risk-Based Analysis
- Distribution of counties across risk categories  
- Boxplots showing economic risk score across categories  
- Bar charts comparing average indicators across risk groups  

These visualizations confirmed that risk categories meaningfully separate counties based on economic conditions.

---

### Key Relationships

EDA revealed several strong and consistent relationships:

- **Income and Poverty**
  - Higher income counties tend to have lower poverty rates  

- **Education and Income**
  - Higher education levels are strongly associated with higher income  

- **Poverty and Unemployment**
  - Counties with higher unemployment tend to experience higher poverty  

- **Homeownership and Stability**
  - Higher homeownership rates are associated with more economically stable counties  

These relationships validate the choice of features used in the economic risk score.

---

### Data Quality Assessment

#### Missing Values
- Very few missing values were present in the dataset  
- Missing values (e.g., income) were handled using **median imputation**  
- After preprocessing, the dataset contained no critical missing data  

#### Duplicate Records
- Duplicate counties were checked using `county_fips`  
- No duplicate records were found in the final dataset  

---

### Data Transformations

Several preprocessing steps were necessary:

- **Merging**
  - Multiple ACS datasets were merged using `county_fips`  

- **Feature Engineering**
  - Converted raw counts into meaningful rates:
    - poverty_rate  
    - unemployment_rate  
    - education percentage  
    - homeownership rate  

- **Splitting**
  - `county_name` was split into separate `county` and `state` fields  

---

### Key Findings

- There is significant economic variation across U.S. counties  
- Economic risk is influenced by multiple interrelated factors  
- High-risk counties consistently show:
  - lower income  
  - higher poverty  
  - higher unemployment  
  - lower education  
  - lower homeownership  

- The constructed risk score effectively captures these patterns  
