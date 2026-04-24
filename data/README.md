# Data

This folder contains all datasets used in the capstone project:

**Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators**

---

## 📊 Data Sources

The primary data source is the **American Community Survey (ACS) 5-Year Estimates (2024)** from the U.S. Census Bureau.

The following datasets are included:

- `ACSDT5Y2024.B01003-Data.csv` – Total Population  
- `ACSDT5Y2024.B15003-Data.csv` – Educational Attainment  
- `ACSDT5Y2024.B17001-Data.csv` – Poverty Status  
- `ACSDT5Y2024.B19013-Data.csv` – Median Household Income  
- `ACSDT5Y2024.B23025-Data.csv` – Employment Status  
- `ACSDT5Y2024.B25003-Data.csv` – Housing Tenure  

These datasets provide key socioeconomic indicators at the county level across the United States.

---

## 📁 Processed Data

- `county_master.csv`  
  - Combined dataset after merging all ACS tables  
  - Contains cleaned and structured county-level features  

- `county_risk_app_ready.csv`  
  - Final dataset used in the Streamlit application  
  - Includes engineered features and computed economic risk scores  

---

## ⚙️ Data Pipeline

The datasets in this folder are processed through the following steps:

1. Data cleaning and preprocessing  
2. Merging multiple ACS tables  
3. Feature engineering  
4. Risk modeling and validation  

These steps are implemented in the notebooks located in the `notebooks/` directory.

---

## 🎯 Purpose

This data is used to:

- Analyze socioeconomic disparities across U.S. counties  
- Build predictive models for economic risk  
- Support interactive visualization and exploration in the application  

---
