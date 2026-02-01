import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Ethiopia FI Dashboard", layout="wide")

st.title("🇪🇹 Financial Inclusion Forecasting System")
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Trends", "Scenarios"])

# Load Data
@st.cache_data
def load_all_data():
    df = pd.read_csv("data/processed/enriched_fi_data.csv")
    forecast = pd.read_csv("data/processed/forecast_results.csv")
    return df, forecast

df, forecast = load_all_data()

if page == "Overview":
    st.header("Consortium Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Access (2024)", "49%", "3pp")
    col2.metric("NBE Target", "60%", "-11pp")
    col3.metric("Digital Usage", "35%", "High")

    st.subheader("P2P vs ATM Ratio indicator")
    st.info("Interoperable P2P digital transfers have surpassed ATM cash withdrawals for the first time in 2024.")

elif page == "Trends":
    st.header("Historical Trajectories")
    indicator = st.selectbox("Select Indicator", df['indicator'].unique())
    subset = df[df['indicator'] == indicator].sort_values('observation_date')
    fig = px.line(subset, x='observation_date', y='value_numeric', markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif page == "Scenarios":
    st.header("Forecast & Policy Scenarios (2025-2027)")
    scenario = st.selectbox("Select Scenario", ["Base", "Optimistic", "Pessimistic"])
    
    # Combined plot
    hist_data = df[df['indicator_code'] == 'ACC_OWNERSHIP']
    st.write(f"Current selection: **{scenario}**")
    # (Plotly code here to show historical + selected scenario)