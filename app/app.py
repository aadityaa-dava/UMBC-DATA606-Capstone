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
st.markdown("""
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
        padding: 1.2rem 1.2rem 0.8rem 1.2rem;
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

    .stDataFrame {
        background: white;
        border-radius: 12px
