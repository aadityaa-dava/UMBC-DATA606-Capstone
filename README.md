# UMBC-DATA606 Capstone

# Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators

This repository contains the capstone project for **DATA 606 – Capstone in Data Science** at the **University of Maryland, Baltimore County (UMBC)**.

The project analyzes **U.S. county-level socioeconomic indicators** using publicly available data from the **American Community Survey (ACS) 5-Year Estimates** to identify counties at risk of economic decline through data analysis, risk modeling, and interactive visualization.

---

# Project Overview

Economic decline is influenced by multiple interconnected socioeconomic factors such as:
- Income
- Poverty
- Employment
- Education
- Housing stability

This project aims to:
- Analyze county-level socioeconomic indicators
- Identify regional economic disparities across U.S. counties
- Develop a composite economic risk scoring methodology
- Categorize counties into risk groups
- Build an interactive Streamlit dashboard for exploration and visualization

The project demonstrates how publicly available government datasets can be transformed into actionable insights using data science methodologies.

---

# Repository Structure

```text
UMBC-DATA606-Capstone/
│
├── app/
│   ├── app.py
│   └── README.md
│
├── data/
│   ├── ACSDT5Y2024.B01003-Data.csv
│   ├── ACSDT5Y2024.B15003-Data.csv
│   ├── ACSDT5Y2024.B17001-Data.csv
│   ├── ACSDT5Y2024.B19013-Data.csv
│   ├── ACSDT5Y2024.B23025-Data.csv
│   ├── ACSDT5Y2024.B25003-Data.csv
│   ├── county_master.csv
│   ├── county_risk_app_ready.csv
│   └── README.md
│
├── docs/
│   ├── Final Presentation.pdf
│   ├── project_report.md
│   ├── resume.md
│   ├── headshot.jpg
│   └── README.md
│
├── notebooks/
│   ├── 01_cleaning_preprocessing.ipynb
│   ├── 02_eda_economic_risk.ipynb
│   ├── 03_economic_risk_modeling_and_validation.ipynb
│   ├── 04_visualization_streamlit.ipynb
│   └── README.md
│
├── requirements.txt
└── README.md
```

---

# Project Objectives

The primary objectives of this project are to:

- Analyze county-level socioeconomic conditions across the United States
- Identify counties potentially vulnerable to economic decline
- Examine relationships between income, poverty, employment, education, and housing
- Develop interpretable economic risk metrics
- Create interactive visualizations and dashboards for data exploration

---

# Data Sources

The project uses datasets from the:

## U.S. Census Bureau – American Community Survey (ACS) 5-Year Estimates (2019–2023)

### ACS Tables Used

| Dataset | Description |
|---|---|
| B01003 | Total Population |
| B15003 | Educational Attainment |
| B17001 | Poverty Status |
| B19013 | Median Household Income |
| B23025 | Employment Status |
| B25003 | Housing Tenure |

Data Source:  
https://data.census.gov/

---

# Methodology

The project follows a structured end-to-end data science workflow.

## 1. Data Cleaning & Preprocessing
📁 `notebooks/01_cleaning_preprocessing.ipynb`

- Loaded multiple ACS datasets
- Cleaned and standardized variables
- Handled missing values
- Merged datasets using county FIPS codes
- Engineered socioeconomic indicators and rates

### Output
```text
county_master.csv
```

---

## 2. Exploratory Data Analysis (EDA)
📁 `notebooks/02_eda_economic_risk.ipynb`

- Generated summary statistics
- Explored variable distributions
- Performed correlation analysis
- Created interactive visualizations using Plotly
- Identified socioeconomic patterns and disparities

---

## 3. Economic Risk Modeling
📁 `notebooks/03_economic_risk_modeling_and_validation.ipynb`

- Developed a composite economic risk score
- Combined multiple socioeconomic indicators
- Categorized counties into:
  - Low Risk
  - Medium Risk
  - High Risk
- Validated the risk scoring methodology

---

## 4. Visualization & Dashboard Development
📁 `notebooks/04_visualization_streamlit.ipynb`  
📁 `app/app.py`

- Prepared application-ready datasets
- Built interactive visualizations
- Developed a Streamlit dashboard for county-level exploration

### Output
```text
county_risk_app_ready.csv
```

---

# Streamlit Dashboard

The project includes an interactive Streamlit application that allows users to:

- Explore county-level socioeconomic indicators
- Compare counties across economic measures
- Analyze risk categories
- Visualize trends and distributions
- Interact with dynamic charts and filters

---

# Technologies Used

| Category | Tools & Libraries |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Development | Jupyter Notebook |

---

# Key Findings

The analysis revealed that counties with:
- Higher poverty rates
- Higher unemployment
- Lower educational attainment
- Lower household income
- Lower homeownership rates

tended to exhibit higher economic risk scores.

The project successfully demonstrates how multiple socioeconomic indicators can be integrated into a clear and interpretable economic risk framework.

---

# How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/aadityaa-dava/UMBC-DATA606-Capstone.git
cd UMBC-DATA606-Capstone
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run the Streamlit Application

```bash
streamlit run app/app.py
```

---

# Documentation

Additional project documentation is available in the `docs/` folder, including:

- Final Presentation
- Project Report
- Resume
- Supporting materials

---

# Future Improvements

Potential future enhancements include:
- Time-series economic analysis
- Geographic mapping visualizations
- Additional socioeconomic indicators
- Advanced machine learning models
- Cloud deployment of the dashboard

---

# Author

## Aadityaa Dava

Graduate Student – Data Science  

University of Maryland, Baltimore County (UMBC)  

GitHub:  
https://github.com/aadityaa-dava

LinkedIn:  
https://www.linkedin.com/in/aadityaa-dava-688908308
