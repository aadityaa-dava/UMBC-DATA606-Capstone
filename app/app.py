import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import json
import urllib.request

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------
st.set_page_config(
    page_title="County Economic Risk Dashboard",
    page_icon="🇺🇸",
    layout="wide"
)

# -------------------------------------------------------
# Custom CSS Styling - Light Theme
# -------------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f7f9fc;
            color: #1f2937;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        h1, h2, h3 {
            color: #12344d !important;
        }

        .dashboard-title {
            font-size: 2.5rem;
            font-weight: 800;
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
            border-radius: 16px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 14px rgba(0,0,0,0.06);
            margin-bottom: 1rem;
        }

        [data-testid="stMetric"] {
            background: white;
            border: 1px solid #e5e7eb;
            padding: 16px;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        [data-testid="stMetricLabel"] {
            color: #64748b !important;
        }

        [data-testid="stMetricValue"] {
            color: #12344d !important;
        }

        [data-testid="stSidebar"] {
            background-color: #eef3f8;
            border-right: 1px solid #dde6ef;
        }

        .small-note {
            color: #64748b;
            font-size: 0.9rem;
        }

        .sidebar-card {
            background-color: #ffffff;
            padding: 16px;
            border-radius: 14px;
            border: 1px solid #dde6ef;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 15px;
        }

        .sidebar-card h3 {
            margin: 0 0 10px 0;
            color: #12344d !important;
            font-size: 1.55rem;
            font-weight: 700;
        }

        .sidebar-card p {
            color: #334155;
            margin: 0 0 12px 0;
            line-height: 1.5;
            font-size: 0.98rem;
        }

        .sidebar-card strong {
            color: #12344d;
        }

        details {
            background-color: #ffffff;
            border: 1px solid #dde6ef;
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

@st.cache_data
def load_geojson():
    url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    with urllib.request.urlopen(url) as response:
        return json.load(response)

df = load_data()
counties_geojson = load_geojson()

# -------------------------------------------------------
# Clean Data
# -------------------------------------------------------
df = df.dropna(subset=["risk_category"]).copy()
df["state"] = df["state"].astype(str)
df["county"] = df["county"].astype(str)
df["risk_category"] = df["risk_category"].astype(str)
df["county_fips"] = df["county_fips"].astype(str).str.zfill(5)

# -------------------------------------------------------
# Sidebar: Project Details
# -------------------------------------------------------
st.sidebar.markdown(
    """
<div class="sidebar-card">
    <h3>Project Details</h3>
    <p><strong>Project Title</strong><br>Identifying U.S. Counties at Risk of Economic Decline</p>
    <p><strong>Author</strong><br>Aadityaa Dava</p>
    <p><strong>Purpose</strong><br>Identify counties that may be at greater risk of economic decline using publicly available socioeconomic indicators.</p>
</div>
    """,
    unsafe_allow_html=True
)

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

with st.sidebar.expander("Data Source", expanded=False):
    st.markdown("""
U.S. Census Bureau  
American Community Survey (ACS) 5-Year Estimates
""")

# -------------------------------------------------------
# Sidebar: Filters
# -------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.header("Filters")

state_options = ["All"] + sorted(df["state"].unique().tolist())
selected_state = st.sidebar.selectbox("State", state_options)

selected_risk = st.sidebar.selectbox(
    "Risk Category",
    ["All", "Low Risk", "Medium Risk", "High Risk"],
    index=0
)

filtered_df = df.copy()

if selected_state != "All":
    filtered_df = filtered_df[filtered_df["state"] == selected_state]

if selected_risk != "All":
    filtered_df = filtered_df[filtered_df["risk_category"] == selected_risk]

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
# U.S. County Risk Map
# -------------------------------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("U.S. County Economic Risk Map")

if not filtered_df.empty:
    fig_map = px.choropleth(
        filtered_df,
        geojson=counties_geojson,
        locations="county_fips",
        featureidkey="id",
        color="risk_category",
        scope="usa",
        hover_name="county",
        hover_data={
            "state": True,
            "economic_risk_score": ":.3f",
            "median_household_income": ":,.0f",
            "poverty_rate": ":.2%",
            "unemployment_rate": ":.2%",
            "bachelors_or_higher_pct": ":.2%",
            "homeownership_rate": ":.2%",
            "county_fips": False,
            "risk_category": True
        },
        color_discrete_map={
            "Low Risk": "green",
            "Medium Risk": "orange",
            "High Risk": "red"
        },
        category_orders={"risk_category": ["Low Risk", "Medium Risk", "High Risk"]},
        title="County-Level Economic Risk Across the United States"
    )

    fig_map.update_traces(
        marker_line_color="#ffffff",
        marker_line_width=0.25
    )

    if selected_state == "All":
        fig_map.update_geos(
            visible=True,
            showland=True,
            landcolor="#f8fafc",
            bgcolor="white",
            showcountries=False,
            showcoastlines=False,
            showsubunits=True,
            subunitcolor="#94a3b8",
            subunitwidth=0.6,
            showlakes=False,
            fitbounds=False
        )
    else:
        fig_map.update_geos(
            visible=True,
            fitbounds="locations",
            showland=True,
            landcolor="#f8fafc",
            bgcolor="white",
            showcountries=False,
            showcoastlines=False,
            showsubunits=True,
            subunitcolor="#94a3b8",
            subunitwidth=0.7,
            showlakes=False
        )

    fig_map.update_layout(
        height=650,
        margin=dict(l=0, r=0, t=50, b=0),
        paper_bgcolor="white",
        plot_bgcolor="white",
        legend_title_text="Risk Category"
    )

    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.warning("No counties match the selected filters.")

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------
# Charts
# Show risk category distribution only when a specific state is selected
# -------------------------------------------------------
if selected_state != "All":
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
            fig.update_layout(
                height=420,
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor="white",
                plot_bgcolor="white",
                font=dict(color="#12344d")
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
                color_discrete_sequence=["#12344d"]
            )
            fig.update_layout(
                height=420,
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor="white",
                plot_bgcolor="white",
                font=dict(color="#12344d")
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No data available for the selected filters.")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Risk Score Distribution")

    if not filtered_df.empty:
        fig = px.histogram(
            filtered_df,
            x="economic_risk_score",
            nbins=40,
            color_discrete_sequence=["#12344d"]
        )
        fig.update_layout(
            height=420,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="#12344d")
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
# Filtered Dataset Dropdown / Preview
# -------------------------------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)

with st.expander("Preview Filtered Dataset", expanded=False):
    st.markdown(
        f'<div class="small-note">Shape: {filtered_df.shape}</div>',
        unsafe_allow_html=True
    )
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------
# Sidebar: Download Filtered Data
# -------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="Download Filtered Data",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_county_risk_data.csv",
    mime="text/csv"
)
