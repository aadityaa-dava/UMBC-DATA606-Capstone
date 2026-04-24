# Notebooks

This folder contains the Jupyter notebooks used throughout the capstone project:

**Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators**

---

## 📊 Overview

The notebooks follow a structured, end-to-end data science pipeline:

1. Data Cleaning and Preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Economic Risk Modeling and Validation  
4. Visualization and Application Integration  

Each notebook builds on the previous step, forming a complete workflow from raw data to final insights.

---

## 📁 Notebook Descriptions

### `01_cleaning_preprocessing.ipynb`
- Loads raw ACS datasets  
- Cleans and standardizes data  
- Merges multiple tables using `county_fips`  
- Performs feature engineering (rates, percentages)  
- Outputs the processed dataset (`county_master.csv`)  

### `02_eda_economic_risk.ipynb`
- Performs exploratory data analysis  
- Generates summary statistics  
- Creates visualizations using Plotly  
- Analyzes distributions and relationships between variables  
- Identifies patterns across counties  

### `03_economic_risk_modeling_and_validation.ipynb`
- Constructs the economic risk score  
- Combines multiple indicators into a composite metric  
- Categorizes counties into Low, Medium, and High risk  
- Validates the scoring approach through analysis and comparison  

### `04_visualisation_streamlit.ipynb`
- Prepares final dataset for application use  
- Generates visualizations used in the Streamlit dashboard  
- Exports the final dataset (`county_risk_app_ready.csv`)  

---

## ⚙️ Workflow Summary

Raw ACS Data → Cleaning & Merging → EDA → Risk Scoring → Final Dataset → Streamlit App

---

## 🎯 Purpose

These notebooks demonstrate:

- A complete data science workflow  
- Data preprocessing and feature engineering  
- Exploratory and statistical analysis  
- Interpretable modeling approach  
- Integration with an interactive application

---  
