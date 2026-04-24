# Application

This folder contains the Streamlit-based web application for the capstone project:

**Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators**

---

## 📊 Overview

The application provides an interactive interface to explore and analyze county-level economic risk across the United States using modeled socioeconomic data.

Users can:

- View economic risk scores for U.S. counties  
- Explore key socioeconomic indicators  
- Compare counties and identify high-risk regions  
- Understand patterns contributing to economic decline  

---

## ⚙️ How to Run

From the root directory of the repository:

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## 📁 Files
|--app.py – Main Streamlit application script

|--README.md – Documentation for the application

## 🧠 Data Source

The application uses the processed dataset: _data/county_risk_app_ready.csv_

This dataset is generated from the full pipeline, including:

- Data cleaning and preprocessing

- Exploratory data analysis (EDA)

- Feature engineering

- Economic risk modeling and validation

## 🎯 Purpose

This application translates the modeling results into an interactive tool that enables:

- Data-driven insights into regional economic risk

- Exploration of socioeconomic disparities

- Support for policy and research analysis
