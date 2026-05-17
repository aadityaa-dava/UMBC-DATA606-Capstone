# 📱 Streamlit Application

This folder contains the interactive Streamlit dashboard developed for the DATA 606 Capstone project:

## Identifying U.S. Counties at Risk of Economic Decline Using Public Socioeconomic Indicators

The application allows users to explore county-level socioeconomic indicators and analyze economic risk patterns across the United States using interactive visualizations and data-driven insights.

---

# Features

The Streamlit application provides:

- Interactive county-level data exploration
- Economic risk score visualization
- Socioeconomic indicator analysis
- Dynamic charts and plots
- Risk category comparisons
- Geographic and statistical insights

---

# Data Used

The application uses the processed dataset:

```text
county_risk_app_ready.csv
```

This dataset includes:

- Median household income
- Poverty rate
- Unemployment rate
- Educational attainment
- Homeownership rate
- Economic risk score
- Risk categories

---

# Technologies Used

- Streamlit
- Pandas
- Plotly
- NumPy
- Scikit-learn

---

# Running the Application

## 1. Navigate to the project root directory

```bash
cd UMBC-DATA606-Capstone
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Launch the Streamlit app

```bash
streamlit run app/app.py
```

---

# Files in This Folder

```text
app/
│
├── app.py
└── README.md
```

| File | Description |
|---|---|
| `app.py` | Main Streamlit dashboard application |
| `README.md` | Documentation for the application folder |

---

# Dashboard Capabilities

Users can:

- Explore county-level socioeconomic trends
- Compare economic indicators across counties
- Analyze distributions and correlations
- Visualize economic risk categories
- Interact with charts and filters dynamically

---

# Purpose of the Application

The dashboard was developed to make socioeconomic data more accessible and interpretable through interactive analytics and visual storytelling.

It demonstrates how public data can be transformed into actionable insights for understanding economic disparities across U.S. counties.
