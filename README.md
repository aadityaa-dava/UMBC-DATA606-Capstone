# 📊 UMBC-DATA-606 Capstone  
## Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators

This repository contains the capstone project for **DATA 606 at the University of Maryland, Baltimore County (UMBC)**.

The project analyzes **U.S. county-level socioeconomic data (ACS 2024)** to identify regions at risk of economic decline and uncover key contributing factors using data analysis, machine learning, and interactive visualization.

---

## 🚀 Project Overview

Economic decline is influenced by multiple socioeconomic indicators such as income, employment, education, and demographics.

This project aims to:

- Analyze **county-level socioeconomic indicators (ACS data)**
- Identify **regional disparities across U.S. counties**
- Build models to detect **counties at risk of economic decline**
- Develop an **interactive Streamlit application** for data exploration

---

## 📂 Repository Structure

**app/**

|---|---app.py  _# Streamlit application_

|---|---README.md

**data/**

|---|---ACSDT5Y2024.B01003-Data.csv   _# Population data_

|---|---ACSDT5Y2024.B15003-Data.csv   _# Education data_

|---|---ACSDT5Y2024.B17001-Data.csv  _# Poverty data_

|---|---ACSDT5Y2024.B19013-Data.csv   _# Median income_

|---|---ACSDT5Y2024.B23025-Data.csv   _# Employment data_

|---|---ACSDT5Y2024.B25003-Data.csv   _# Housing data_

|---|---county_master.csv           _# Cleaned merged dataset_

|---|---county_risk_app_ready.csv    _# Final dataset used in app_

|---|---README.md

**docs/**

|---|---project report.md            _# Final report_

|---|---Resume.md

|---|---headshot.jpg

|---|---README.md

**notebooks/**

|---|---01_cleaning_preprocessing.ipynb

|---|---02_eda_economic_risk.ipynb

|---|---03_economic_risk_modeling_and_validation.ipynb

|---|---04_visualization_streamlit.ipynb

|---|---README.md

**requirements.txt**

**README.md**

---

## 📊 Data

The project uses **American Community Survey (ACS) 5-Year Estimates (2024)** datasets:

- **B01003** – Population  
- **B15003** – Education  
- **B17001** – Poverty  
- **B19013** – Median Income  
- **B23025** – Employment  
- **B25003** – Housing  

These datasets are cleaned, merged, and transformed into a unified **county-level dataset (`county_master.csv`)**.

---

## 🔍 Methodology

### 1. Data Cleaning & Preprocessing  
📁 `notebooks/01_cleaning_preprocessing.ipynb`

- Merged multiple ACS datasets  
- Handled missing and inconsistent values  
- Created a unified dataset (`county_master.csv`)  

---

### 2. Exploratory Data Analysis (EDA)  
📁 `notebooks/02_eda_economic_risk.ipynb`

- Analyzed distributions of socioeconomic indicators  
- Identified regional disparities  
- Explored correlations between variables  

---

### 3. Economic Risk Modeling  
📁 `notebooks/03_economic_risk_modeling_and_validation.ipynb`

- Built models to identify counties at risk  
- Evaluated model performance  
- Identified key predictors of economic decline  

---

### 4. Visualization & Application  
📁 `notebooks/04_visualisation_streamlit.ipynb`  
📁 `app/app.py`

- Developed an interactive **Streamlit application**
- Enables:
  - County-level exploration  
  - Visualization of socioeconomic indicators  
  - Insight-driven analysis  

---

## 🛠️ Tech Stack

- **Python**: Pandas, NumPy, Scikit-learn  
- **Visualization**: Matplotlib, Seaborn, Plotly  
- **Application**: Streamlit  
- **Environment**: Jupyter Notebook  

---

## 📈 Key Outcomes

- Identified **counties at higher risk of economic decline**  
- Determined **key socioeconomic drivers** influencing outcomes  
- Built an **interactive dashboard** for exploration and insights  

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/aadityaa-dava/UMBC-DATA606-Capstone.git
cd UMBC-DATA606-Capstone
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit app
```bash
streamlit run app/app.py
```
