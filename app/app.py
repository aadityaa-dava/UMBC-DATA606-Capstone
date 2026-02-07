import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px
import json
import urllib.request

# ---------------------------------
# Page config
# ---------------------------------
st.set_page_config(page_title="US County Economic Risk", layout="wide")
st.title("Identifying U.S. Counties at Risk of Economic Decline")
st.caption("County-level risk ranking using ACS 5-Year indicators")

# ---------------------------------
# Load data (cached)
# ---------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/county_master.csv")
    df["county_fips"] = df["county_fips"].astype(int).astype(str).str.zfill(5)
    df["state"] = df["county_name"].str.split(", ").str[-1].str.strip()
    return df

df = load_data()

# ---------------------------------
# Build economic risk score
# ---------------------------------
risk_features = [
    "median_household_income",
    "poverty_rate",
    "unemployment_rate",
    "bachelors_or_higher_pct",
    "homeownership_rate",
]

df_model = df.copy()
df_model[risk_features] = df_model[risk_features].fillna(
    df_model[risk_features].median(numeric_only=True)
)

scaler = MinMaxScaler()
df_norm = df_model.copy()
df_norm[risk_features] = scaler.fit_transform(df_model[risk_features])

df_norm["economic_risk_score"] = (
    (1 - df_norm["median_household_income"]) +
    df_norm["poverty_rate"] +
    df_norm["unemployment_rate"] +
    (1 - df_norm["bachelors_or_higher_pct"]) +
    (1 - df_norm["homeownership_rate"])
) / 5

df_norm["risk_category"] = pd.qcut(
    df_norm["economic_risk_score"],
    q=3,
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

df_display = df.copy()
df_display["economic_risk_score"] = df_norm["economic_risk_score"].values
df_display["risk_category"] = df_norm["risk_category"].astype(str).values

# ---------------------------------
# Load GeoJSON (cached)
# ---------------------------------
@st.cache_data
def load_geojson():
    url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    with urllib.request.urlopen(url) as response:
        return json.load(response)

counties_geojson = load_geojson()

# ----------------------------
# Sidebar: Methodology
# ----------------------------
st.sidebar.header("Methodology")

st.sidebar.markdown("""
**Data Source:**  
U.S. Census Bureau – American Community Survey (ACS)
""")

with st.sidebar.expander("What is this app doing?", expanded=True):
    st.markdown("""
This app ranks U.S. counties by **economic risk** using ACS 5-year indicators.

**Goal:** Identify counties that may be more vulnerable to economic decline
using a transparent, data-driven scoring approach.
""")

with st.sidebar.expander("Indicators used (ACS)"):
    st.markdown("""
- Median household income *(lower → higher risk)*
- Poverty rate *(higher → higher risk)*
- Unemployment rate *(higher → higher risk)*
- Bachelor’s degree or higher *(lower → higher risk)*
- Homeownership rate *(lower → higher risk)*
""")

with st.sidebar.expander("How the risk score is computed"):
    st.markdown("""
Each indicator is normalized (0–1) using Min–Max scaling.

**Economic Risk Score** is the mean of:
- `1 − income`
- `poverty`
- `unemployment`
- `1 − education`
- `1 − homeownership`
""")

with st.sidebar.expander("How risk categories are assigned"):
    st.markdown("""
Counties are divided into three equal groups using quantiles:
- Low Risk
- Medium Risk
- High Risk
""")

with st.sidebar.expander("Limitations"):
    st.markdown("""
- Survey-based ACS data
- Relative risk, not causality
- Some economic drivers not included
""")

# ----------------------------
# Sidebar: Search and Filters
# ----------------------------
st.sidebar.divider()
st.sidebar.header("Search and Filters")

county_search = st.sidebar.text_input(
    "Search by county name",
    placeholder="e.g., Cook County"
)

state_options = ["All"] + sorted(df_display["state"].unique())
selected_state = st.sidebar.selectbox("State", state_options)

selected_risk = st.sidebar.selectbox(
    "Risk Category",
    ["All", "Low Risk", "Medium Risk", "High Risk"]
)

score_min = float(df_display["economic_risk_score"].min())
score_max = float(df_display["economic_risk_score"].max())

score_range = st.sidebar.slider(
    "Economic Risk Score Range",
    min_value=score_min,
    max_value=score_max,
    value=(score_min, score_max),
    step=0.001
)

# ----------------------------
# Apply filters
# ----------------------------
df_filtered = df_display.copy()

if county_search.strip():
    df_filtered = df_filtered[
        df_filtered["county_name"].str.contains(county_search, case=False, na=False)
    ]

if selected_state != "All":
    df_filtered = df_filtered[df_filtered["state"] == selected_state]

if selected_risk != "All":
    df_filtered = df_filtered[df_filtered["risk_category"] == selected_risk]

df_filtered = df_filtered[
    df_filtered["economic_risk_score"].between(score_range[0], score_range[1])
]

# ----------------------------
# Map (DISCRETE ONLY)
# ----------------------------
st.subheader("County-Level Economic Risk Map")

hover_cols = [
    "county_fips",
    "risk_category",
    "median_household_income",
    "poverty_rate",
    "unemployment_rate",
    "bachelors_or_higher_pct",
    "homeownership_rate",
    "economic_risk_score",
]

if df_filtered.empty:
    st.warning("No counties match the selected filters.")
else:
    fig = px.choropleth(
        df_filtered,
        geojson=counties_geojson,
        locations="county_fips",
        featureidkey="id",
        color="risk_category",
        color_discrete_map={
            "Low Risk": "green",
            "Medium Risk": "orange",
            "High Risk": "red"
        },
        scope="usa",
        hover_name="county_name",
        title="Economic Risk Categories Across U.S. Counties"
    )

    fig.update_traces(
        customdata=df_filtered[hover_cols].to_numpy(),
        hovertemplate=
            "<b>%{hovertext}</b><br><br>"
            "Risk Category: %{customdata[1]}<br>"
            "Income: $%{customdata[2]:,.0f}<br>"
            "Poverty: %{customdata[3]:.2%}<br>"
            "Unemployment: %{customdata[4]:.2%}<br>"
            "Education: %{customdata[5]:.2%}<br>"
            "Homeownership: %{customdata[6]:.2%}<br>"
            "Risk Score: %{customdata[7]:.3f}"
            "<extra></extra>"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Top counties table
# ----------------------------
st.subheader("Top Counties Based on Selected Filters")

if not df_filtered.empty:
    table_df = (
        df_filtered.sort_values(
            "economic_risk_score",
            ascending=(selected_risk == "Low Risk")
        )
        .head(25)
    )

    st.dataframe(
        table_df[
            [
                "county_name",
                "state",
                "risk_category",
                "economic_risk_score",
                "median_household_income",
                "poverty_rate",
                "unemployment_rate",
            ]
        ],
        use_container_width=True,
    )

# ----------------------------
# Sidebar: Download (BOTTOM)
# ----------------------------
st.sidebar.divider()
st.sidebar.download_button(
    "Download Risk-Scored County Data",
    df_display.to_csv(index=False).encode("utf-8"),
    file_name="county_risk_scored.csv",
    mime="text/csv",
)
