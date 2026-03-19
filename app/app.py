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
# Custom CSS Styling
# -------------------------------------------------------
st.markdown(
    """
    <style>
        .main {
            background-color: #f7f9fc;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        h1, h2, h3 {
            color: #1f2d3d;
        }

        .dashboard-title {
            font-size: 2.4rem;
            font-weight: 700;
            color: #12344d;
            margin-bottom: 0.2rem;
        }

        .dashboard-subtitle {
            font-size: 1rem;
            color: #5b6b7a;
            margin-bottom: 1.5rem;
        }

        .section-card {
            background: white;
            padding: 1.2rem;
            border-radius: 14px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
            margin-bottom: 1rem;
        }

        [data-testid="stMetric"] {
            background: white;
            border: 1px solid #e6ecf2;
            padding: 16px;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        [data-testid="stSidebar"] {
            background-color: #eef3f8;
        }

        .small-note {
            color: #6b7c93;
            font-size: 0.9rem;
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

# Keep displayed/filter fields consistent
df["state"] = df["state"].astype(str)
df["county"] = df["county"].astype(str)
df["risk_category"] = df["risk_category"].astype(str)

# -------------------------------------------------------
# Sidebar: Project Info
# -------------------------------------------------------
st.sidebar.title("📘 Project Details")

st.sidebar.markdown("""
**Project Title:**  
Identifying U.S. Counties at Risk of Economic Decline  

**Author:**  
Aadityaa Dava  

**Purpose:**  
Identify counties vulnerable to economic decline using ACS indicators.
""")

with st.sidebar.expander("Methodology"):
    st.markdown("""
- Data from ACS 5-Year Estimates  
- Features normalized using Min-Max scaling  
- Risk score built from five indicators  
- Counties grouped into Low, Medium, and High Risk using quantiles
""")

# -------------------------------------------------------
# Sidebar: Filters
# -------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.header("Filters")

state_options = ["All"] + sorted(df["state"].dropna().astype(str).unique().tolist())
selected_state = st.sidebar.selectbox("State", state_options)

risk_options = sorted(df["risk_category"].dropna().astype(str).unique().tolist())
selected_risk = st.sidebar.multiselect(
    "Risk Category",
    options=risk_options,
    default=risk_options
)

filtered_df = df.copy()

if selected_state != "All":
    filtered_df = filtered_df[filtered_df["state"].astype(str) == selected_state]

filtered_df = filtered_df[filtered_df["risk_category"].astype(str).isin(selected_risk)]

# -------------------------------------------------------
# Metrics
# -------------------------------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.metric("Total Counties", len(filtered_df))

avg_risk = filtered_df["economic_risk_score"].mean() if not filtered_df.empty else 0
col2.metric("Avg Risk Score", f"{avg_risk:.3f}")

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
            category_orders={"Risk": ["Low Risk", "Medium Risk", "High Risk"]}
        )
        fig.update_layout(height=420, margin=dict(l=20, r=20, t=20, b=20))
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
            nbins=40
        )
        fig.update_layout(height=420, margin=dict(l=20, r=20, t=20, b=20))
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
