import json
from pathlib import Path
from urllib.request import urlopen

import pandas as pd
import plotly.express as px
import streamlit as st

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------
st.set_page_config(
    page_title="County Economic Risk Dashboard",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------------
# Constants
# -------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parent / "data" / "county_risk_app_ready.csv"
COUNTY_GEOJSON_URL = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"

RISK_ORDER = ["Low Risk", "Medium Risk", "High Risk"]
RISK_COLORS = {
    "Low Risk": "#22c55e",
    "Medium Risk": "#f59e0b",
    "High Risk": "#ef4444",
}

TEXT_COLOR = "#12344d"
PLOT_BG = "#ffffff"
PAPER_BG = "#ffffff"

# -------------------------------------------------------
# Custom CSS
# -------------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(180deg, #f8fafc 0%, #eef4fb 100%);
            color: #12344d;
        }

        .block-container {
            padding-top: 0rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
            max-width: 1400px;
        }

        /* Sidebar spacing fixes */
        section[data-testid="stSidebar"] {
            padding-top: 0rem !important;
        }

        section[data-testid="stSidebar"] > div {
            padding-top: 0.8rem !important;
        }

        section[data-testid="stSidebar"] > div:first-child {
            padding-top: 0rem !important;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #eef4fb 0%, #f8fbff 100%);
            border-right: 1px solid #dbe7f3;
        }

        .hero {
            padding: 1rem 2rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #12344d 0%, #1d4f73 60%, #3b82f6 100%);
            color: white;
            box-shadow: 0 12px 30px rgba(18, 52, 77, 0.18);
            margin-bottom: 1rem;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.15);
        }

        .hero h1 {
            margin: 0;
            font-size: 2.2rem;
            font-weight: 800;
            color: white !important;
        }

        .hero p {
            margin: 0.6rem 0 0 0;
            font-size: 1rem;
            color: rgba(255,255,255,0.92);
            line-height: 1.6;
        }

        .mini-note {
            color: #64748b;
            font-size: 0.92rem;
            margin-top: -0.2rem;
            margin-bottom: 1rem;
        }

        [data-testid="stMetric"] {
            background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
            border: 1px solid #e2e8f0;
            padding: 16px;
            border-radius: 18px;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
        }

        [data-testid="stMetricLabel"] {
            color: #64748b !important;
            font-weight: 600;
        }

        [data-testid="stMetricValue"] {
            color: #12344d !important;
        }

        .sidebar-card {
            background: white;
            padding: 16px;
            border-radius: 16px;
            border: 1px solid #dbe7f3;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
            margin-bottom: 14px;
        }

        .sidebar-card h3 {
            margin: 0 0 8px 0;
            color: #12344d !important;
            font-size: 1.25rem;
            font-weight: 800;
        }

        .sidebar-card p {
            color: #334155;
            margin: 0 0 10px 0;
            line-height: 1.45;
            font-size: 0.96rem;
        }

        h2, h3 {
            color: #12344d !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    df_ = pd.read_csv(path)
    df_ = df_.dropna(subset=["risk_category"]).copy()
    df_["state"] = df_["state"].astype(str)
    df_["county"] = df_["county"].astype(str)
    df_["risk_category"] = pd.Categorical(
        df_["risk_category"],
        categories=RISK_ORDER,
        ordered=True,
    )
    df_["county_fips"] = df_["county_fips"].astype(str).str.zfill(5)
    return df_


@st.cache_data(show_spinner=False)
def load_geojson() -> dict:
    with urlopen(COUNTY_GEOJSON_URL) as response:
        return json.load(response)


def apply_plot_layout(fig, height=420, title=None):
    layout_kwargs = dict(
        height=height,
        margin=dict(l=20, r=20, t=50 if title else 20, b=20),
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(color=TEXT_COLOR),
        legend_title_text="",
    )
    if title is not None:
        layout_kwargs["title"] = title
    fig.update_layout(**layout_kwargs)
    return fig


try:
    df = load_data(DATA_PATH)
    counties_geojson = load_geojson()
except Exception as e:
    st.error(f"Failed to load app resources: {e}")
    st.stop()

# -------------------------------------------------------
# Header
# -------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>U.S. County Economic Risk Dashboard</h1>
        <p>
            Interactive county-level analysis built from ACS 5-year socioeconomic indicators
            and a transparent composite economic risk score.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------
st.sidebar.markdown(
    """
    <div class="sidebar-card">
        <h3>Project Overview</h3>
        <p><strong>Project Title</strong><br>Identifying U.S. Counties at Risk of Economic Decline</p>
        <p><strong>Author</strong><br>Aadityaa Dava</p>
        <p><strong>Purpose</strong><br>Identify counties that may be at greater risk of economic decline using publicly available socioeconomic indicators.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar.expander("Research Questions", expanded=False):
    st.markdown("""
- Which U.S. counties are at the highest risk of economic decline?
- How do key socioeconomic indicators influence economic risk?
- Are there geographic patterns in economic risk across states or regions?
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
""")

with st.sidebar.expander("Data Source", expanded=False):
    st.markdown("""
U.S. Census Bureau  
American Community Survey (ACS) 5-Year Estimates
""")

st.sidebar.markdown("---")
st.sidebar.subheader("Filters")

state_options = ["All"] + sorted(df["state"].unique().tolist())
selected_state = st.sidebar.selectbox("State", state_options)

selected_risk = st.sidebar.selectbox(
    "Risk Category",
    ["All"] + RISK_ORDER,
)

filtered_df = df.copy()

if selected_state != "All":
    filtered_df = filtered_df[filtered_df["state"] == selected_state]

if selected_risk != "All":
    filtered_df = filtered_df[filtered_df["risk_category"] == selected_risk]

# -------------------------------------------------------
# Summary Metrics
# -------------------------------------------------------
st.subheader("Summary Metrics")
st.markdown(
    '<div class="mini-note">A quick overview of the currently filtered counties.</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

total_counties = len(filtered_df)
avg_risk = filtered_df["economic_risk_score"].mean() if not filtered_df.empty else 0.0
high_risk_count = int((filtered_df["risk_category"] == "High Risk").sum()) if not filtered_df.empty else 0

col1.metric("Total Counties", f"{total_counties:,}")
col2.metric("Average Risk Score", f"{avg_risk:.3f}")
col3.metric("High Risk Counties", f"{high_risk_count:,}")

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------------
# Risk Map
# -------------------------------------------------------
st.subheader("County Economic Risk Map")
st.markdown(
    '<div class="mini-note">Explore how risk levels vary geographically across counties.</div>',
    unsafe_allow_html=True,
)

if filtered_df.empty:
    st.warning("No counties match the selected filters.")
else:
    fig_map = px.choropleth(
        filtered_df,
        geojson=counties_geojson,
        locations="county_fips",
        featureidkey="id",
        color="risk_category",
        hover_name="county",
        scope="usa",
        category_orders={"risk_category": RISK_ORDER},
        color_discrete_map=RISK_COLORS,
        hover_data={
            "state": True,
            "economic_risk_score": ":.3f",
            "median_household_income": ":,.0f",
            "poverty_rate": ":.2%",
            "unemployment_rate": ":.2%",
            "bachelors_or_higher_pct": ":.2%",
            "homeownership_rate": ":.2%",
            "county_fips": False,
            "risk_category": True,
        },
    )

    fig_map.update_traces(marker_line_color="#ffffff", marker_line_width=0.2)

    geo_kwargs = dict(
        visible=True,
        showland=True,
        landcolor="#f8fafc",
        bgcolor="white",
        showcountries=False,
        showcoastlines=False,
        showsubunits=True,
        subunitcolor="#94a3b8",
        showlakes=False,
    )

    if selected_state == "All":
        fig_map.update_geos(fitbounds=False, subunitwidth=0.6, **geo_kwargs)
    else:
        fig_map.update_geos(fitbounds="locations", subunitwidth=0.7, **geo_kwargs)

    fig_map.update_layout(
        height=680,
        margin=dict(l=0, r=0, t=20, b=0),
        paper_bgcolor="white",
        plot_bgcolor="white",
        legend_title_text="Risk Category",
    )

    st.plotly_chart(fig_map, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------------
# Charts
# -------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Risk Score Distribution")

    if filtered_df.empty:
        st.info("No data available for the selected filters.")
    else:
        fig_hist = px.histogram(
            filtered_df,
            x="economic_risk_score",
            nbins=40,
            color_discrete_sequence=["#1d4f73"],
        )
        apply_plot_layout(fig_hist, height=420)
        st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    st.subheader("Risk Category Breakdown")

    if filtered_df.empty:
        st.info("No data available for the selected filters.")
    else:
        counts = (
            filtered_df["risk_category"]
            .value_counts()
            .reindex(RISK_ORDER, fill_value=0)
            .rename_axis("Risk")
            .reset_index(name="Count")
        )

        fig_bar = px.bar(
            counts,
            x="Risk",
            y="Count",
            text="Count",
            color="Risk",
            color_discrete_map=RISK_COLORS,
            category_orders={"Risk": RISK_ORDER},
        )
        apply_plot_layout(fig_bar, height=420)
        fig_bar.update_traces(textposition="outside")
        st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------------
# Tables
# -------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top High-Risk Counties")

    if filtered_df.empty:
        st.info("No counties to display.")
    else:
        high = filtered_df.sort_values("economic_risk_score", ascending=False).head(10)
        st.dataframe(
            high[["state", "county", "economic_risk_score", "risk_category"]],
            use_container_width=True,
            hide_index=True,
        )

with col2:
    st.subheader("Top Low-Risk Counties")

    if filtered_df.empty:
        st.info("No counties to display.")
    else:
        low = filtered_df.sort_values("economic_risk_score", ascending=True).head(10)
        st.dataframe(
            low[["state", "county", "economic_risk_score", "risk_category"]],
            use_container_width=True,
            hide_index=True,
        )

# -------------------------------------------------------
# Dataset Preview
# -------------------------------------------------------
with st.expander("Preview Filtered Dataset", expanded=False):
    st.markdown(
        f'<div class="mini-note">Current shape: {filtered_df.shape[0]:,} rows × {filtered_df.shape[1]} columns</div>',
        unsafe_allow_html=True,
    )
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

# -------------------------------------------------------
# Download Button
# -------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="Download Filtered Data",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_county_risk_data.csv",
    mime="text/csv",
)
