import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------
st.set_page_config(
    page_title="County Economic Risk Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------
# Custom CSS Styling - Dark Theme
# -------------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background-color: #0f172a;
            color: #e2e8f0;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        h1, h2, h3 {
            color: #f8fafc !important;
        }

        p, div, label, span {
            color: #cbd5e1;
        }

        .dashboard-title {
            font-size: 2.5rem;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 0.2rem;
        }

        .dashboard-subtitle {
            font-size: 1rem;
            color: #94a3b8;
            margin-bottom: 1.5rem;
        }

        .section-card {
            background: #111827;
            padding: 1.2rem;
            border-radius: 16px;
            border: 1px solid #1f2937;
            box-shadow: 0 4px 14px rgba(0,0,0,0.25);
            margin-bottom: 1rem;
        }

        [data-testid="stMetric"] {
            background: #111827;
            border: 1px solid #1f2937;
            padding: 16px;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.25);
        }

        [data-testid="stMetricLabel"] {
            color: #94a3b8 !important;
        }

        [data-testid="stMetricValue"] {
            color: #f8fafc !important;
        }

        [data-testid="stSidebar"] {
            background-color: #111827;
            border-right: 1px solid #1f2937;
        }

        .small-note {
            color: #94a3b8;
            font-size: 0.9rem;
        }

        .sidebar-card {
            background-color: #0b1220;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #1f2937;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
            margin-bottom: 15px;
        }

        .sidebar-card h3 {
            margin-top: 0;
            margin-bottom: 8px;
            color: #f8fafc !important;
        }

        .sidebar-card p {
            color: #cbd5e1;
            margin-bottom: 10px;
        }

        .stDataFrame, div[data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
        }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div {
            background-color: #0b1220 !important;
            color: #f8fafc !important;
            border: 1px solid #334155 !important;
        }

        .stMultiSelect div[data-baseweb="tag"] {
            background-color: #1e293b !important;
            color: #f8fafc !important;
        }

        details {
            background-color: #0b1220;
            border: 1px solid #1f2937;
            border-radius: 10px;
            padding: 0.35rem 0.6rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------
# Header
# -------------------------------------------------------
st.markdown(
    '<div class="dashboard-title">📊 U.S. County Economic Risk Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">Built from ACS 5-year county-level indicators and a transparent composite risk score.</div>',
    unsafe_allow_html=True
)

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
# Clean Data
# -------------------------------------------------------
df = df.dropna(subset=["risk_category"]).copy()
df["state"] = df["state"].astype(str)
df["county"] = df["county"].astype(str)
df["risk_category"] = df["risk_category"].astype(str)

# -------------------------------------------------------
# Sidebar: Project Details
# -------------------------------------------------------
st.sidebar.markdown(
    """
    <div class="sidebar-card">
        <h3>📘 Project Details</h3>
        <p><b>Project Title</b><br>
        Identifying U.S. Counties at Risk of Economic Decline</p>

        <p><b>Author</b><br>
        Aadityaa Dava</p>

        <p><b>Purpose</b><br>
        Identify counties that may be at greater risk of economic decline using publicly available socioeconomic indicators from the American Community Survey (ACS).</p>
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar.expander("📊 Research Questions", expanded=False):
    st.markdown("""
- Which U.S. counties are at the highest risk of economic decline?  
- How do income, poverty, unemployment, education, and homeownership influence economic risk?  
- Are there noticeable patterns in economic risk across counties?  
- Can multiple indicators be combined into a clear and interpretable economic risk score?
""")

with st.sidebar.expander("📌 Indicators Used", expanded=False):
    st.markdown("""
- Median Household Income  
- Poverty Rate  
- Unemployment Rate  
- Bachelor's Degree or Higher (%)  
- Homeownership Rate
""")

with st.sidebar.expander("⚙️ Risk Score Methodology", expanded=False):
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

with st.sidebar.expander("📂 Data Source", expanded=False):
    st.markdown("""
U.S. Census Bureau  
American Community Survey (ACS) 5-Year Estimates
""")

# -------------------------------------------------------
# Sidebar: Filters
# -------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.header("🎛️ Filters")

state_options = ["All"] + sorted(df["state"].unique().tolist())
selected_state = st.sidebar.selectbox("State", state_options)

risk_options = ["Low Risk", "Medium Risk", "High Risk"]
selected_risk = st.sidebar.multiselect(
    "Risk Category",
    options=risk_options,
    default=risk_options
)

filtered_df = df.copy()

if selected_state != "All":
    filtered_df = filtered_df[filtered_df["state"] == selected_state]

filtered_df = filtered_df[filtered_df["risk_category"].isin(selected_risk)]

# -------------------------------------------------------
# Summary Metrics
# -------------------------------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)

st.subheader("Summary Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Counties", len(filtered_df))

avg_risk = filtered_df["economic_risk_score"].mean() if not filtered_df.empty else 0
col2.metric("Average Risk Score", f"{avg_risk:.3f}")

high_risk = (filtered_df["risk_category"] == "High Risk").sum() if not filtered_df.empty else 0
col3.metric("High Risk Counties", int(high_risk))

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------
# Charts
# -------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Risk Category Distribution")

    if not filtered_df.empty:
        counts = filtered_df["risk_category"].value_counts().reset_index()
        counts.columns = ["Risk", "Count"]

        fig = px.bar(
            counts,
            x="Risk",
            y="Count",
            color="Risk",
            text="Count",
            color_discrete_map={
                "Low Risk": "green",
                "Medium Risk": "orange",
                "High Risk": "red"
            },
            category_orders={"Risk": ["Low Risk", "Medium Risk", "High Risk"]},
            template="plotly_dark"
        )
        fig.update_layout(
            height=420,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="#e2e8f0")
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Risk Score Distribution")

    if not filtered_df.empty:
        fig = px.histogram(
            filtered_df,
            x="economic_risk_score",
            nbins=40,
            template="plotly_dark"
        )
        fig.update_layout(
            height=420,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="#e2e8f0")
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------
# Tables
# -------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Top High-Risk Counties")

    if not filtered_df.empty:
        high = filtered_df.sort_values("economic_risk_score", ascending=False).head(10)
        st.dataframe(
            high[["state", "county", "economic_risk_score", "risk_category"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No counties to display.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Top Low-Risk Counties")

    if not filtered_df.empty:
        low = filtered_df.sort_values("economic_risk_score", ascending=True).head(10)
        st.dataframe(
            low[["state", "county", "economic_risk_score", "risk_category"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No counties to display.")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------
# Full Data
# -------------------------------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)

st.subheader("Filtered Dataset")
st.markdown(
    f'<div class="small-note">Shape: {filtered_df.shape}</div>',
    unsafe_allow_html=True
)

st.dataframe(filtered_df, use_container_width=True, hide_index=True)

st.markdown('</div>', unsafe_allow_html=True)
