import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="County Economic Risk Dashboard", layout="wide")

st.title("U.S. County Economic Risk Dashboard")
st.caption("Built from ACS 5-year county-level indicators and a transparent composite risk score.")

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parent / "data" / "county_risk_app_ready.csv"

@st.cache_data
def load_data():
    if not DATA_PATH.exists():
        st.error(f"Data file not found at: {DATA_PATH}")
        st.stop()
    return pd.read_csv(DATA_PATH)

df = load_data()

# -------------------------------------------------------
# Sidebar: Project Details
# -------------------------------------------------------
st.sidebar.title("Project Details")

st.sidebar.markdown("""
**Project Title:**  
Identifying U.S. Counties at Risk of Economic Decline

**Author:**  
Aadityaa Dava

**Purpose:**  
This dashboard identifies counties that may be at greater risk of economic decline using publicly available socioeconomic indicators from the American Community Survey (ACS).
""")

with st.sidebar.expander("Research Questions", expanded=False):
    st.markdown("""
- Which U.S. counties are at the highest risk of economic decline?
- How do income, poverty, unemployment, education, and homeownership influence economic risk?
- Are there noticeable patterns in economic risk across counties?
- Can multiple indicators be combined into a clear and interpretable economic risk score?
""")

with st.sidebar.expander("Indicators Used", expanded=False):
    st.markdown("""
- Median Household Income  
- Poverty Rate  
- Unemployment Rate  
- Bachelor's Degree or Higher (%)  
- Homeownership Rate
""")

with st.sidebar.expander("Risk Score Methodology", expanded=False):
    st.markdown("""
The economic risk score is based on five normalized indicators.

Higher risk is assigned to counties with:
- lower income
- higher poverty
- higher unemployment
- lower education
- lower homeownership

The final score is the average of these adjusted normalized values.
""")

with st.sidebar.expander("Risk Categories", expanded=False):
    st.markdown("""
Counties are grouped into:
- Low Risk
- Medium Risk
- High Risk

Categories are assigned using quantile-based binning so that the groups are balanced in size.
""")

with st.sidebar.expander("Data Source", expanded=False):
    st.markdown("""
U.S. Census Bureau  
American Community Survey (ACS) 5-Year Estimates
""")

# -------------------------------------------------------
# Sidebar: Filters
# -------------------------------------------------------
st.sidebar.divider()
st.sidebar.header("Filters")

selected_state = st.sidebar.selectbox(
    "Select State",
    options=["All"] + sorted(df["state"].dropna().unique().tolist())
)

selected_risk = st.sidebar.multiselect(
    "Select Risk Category",
    options=sorted(df["risk_category"].dropna().unique().tolist()),
    default=sorted(df["risk_category"].dropna().unique().tolist())
)

filtered_df = df.copy()

if selected_state != "All":
    filtered_df = filtered_df[filtered_df["state"] == selected_state]

filtered_df = filtered_df[filtered_df["risk_category"].isin(selected_risk)]

# -------------------------------------------------------
# Summary Metrics
# -------------------------------------------------------
st.subheader("Summary Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Counties", len(filtered_df))

avg_risk = filtered_df["economic_risk_score"].mean() if not filtered_df.empty else 0
col2.metric("Average Risk Score", f"{avg_risk:.3f}")

high_risk_count = (filtered_df["risk_category"] == "High Risk").sum() if not filtered_df.empty else 0
col3.metric("High Risk Counties", int(high_risk_count))

# -------------------------------------------------------
# Risk Category Distribution
# -------------------------------------------------------
st.subheader("Risk Category Distribution")

if not filtered_df.empty:
    risk_counts = filtered_df["risk_category"].value_counts().reset_index()
    risk_counts.columns = ["Risk Category", "Count"]

    fig_bar = px.bar(
        risk_counts,
        x="Risk Category",
        y="Count",
        color="Risk Category",
        text="Count",
        color_discrete_map={
            "Low Risk": "green",
            "Medium Risk": "orange",
            "High Risk": "red"
        },
        title="Distribution of Counties by Risk Category"
    )

    fig_bar.update_layout(height=500)
    st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.warning("No data available for the selected filters.")

# -------------------------------------------------------
# Risk Score Distribution
# -------------------------------------------------------
st.subheader("Risk Score Distribution")

if not filtered_df.empty:
    fig_hist = px.histogram(
        filtered_df,
        x="economic_risk_score",
        nbins=40,
        title="Distribution of Economic Risk Scores"
    )

    fig_hist.update_layout(height=500)
    st.plotly_chart(fig_hist, use_container_width=True)

# -------------------------------------------------------
# Top 10 High-Risk Counties
# -------------------------------------------------------
st.subheader("Top 10 High-Risk Counties")

if not filtered_df.empty:
    top_high = filtered_df.sort_values("economic_risk_score", ascending=False).head(10)

    st.dataframe(
        top_high[["state", "county", "economic_risk_score", "risk_category"]],
        use_container_width=True
    )

# -------------------------------------------------------
# Top 10 Low-Risk Counties
# -------------------------------------------------------
st.subheader("Top 10 Low-Risk Counties")

if not filtered_df.empty:
    top_low = filtered_df.sort_values("economic_risk_score", ascending=True).head(10)

    st.dataframe(
        top_low[["state", "county", "economic_risk_score", "risk_category"]],
        use_container_width=True
    )

# -------------------------------------------------------
# Full Filtered Dataset
# -------------------------------------------------------
st.subheader("Filtered Dataset")

st.write("Dataset shape:", filtered_df.shape)
st.dataframe(filtered_df, use_container_width=True)
