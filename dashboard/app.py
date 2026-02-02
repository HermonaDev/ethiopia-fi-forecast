import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Selam Analytics: FI Intelligence",
    layout="wide"
)


@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/enriched_fi_data.csv")
    fc = pd.read_csv("data/processed/forecast_results.csv")
    return df, fc


df, fc = load_data()

st.title("🇪🇹 Ethiopia Financial Inclusion Intelligence")

# --- Sidebar ---
page = st.sidebar.selectbox(
    "Navigate",
    ["Strategic Overview", "Scenario Sandbox"]
)

if page == "Strategic Overview":
    # 1. Gauge Chart (Progress to 60%)
    target_code = "ACC_OWNERSHIP"
    latest = df[df['indicator_code'] == target_code].iloc[-1]
    val = latest['value_numeric']

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=val,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Progress to 60% National Target"},
        delta={'reference': 60, 'increasing': {'color': "green"}},
        gauge={'axis': {'range': [None, 100]},
               'steps': [{'range': [0, 49], 'color': "lightgray"},
                         {'range': [49, 60], 'color': "gray"}],
               'threshold': {'line': {'color': "red", 'width': 4},
                             'thickness': 0.75, 'value': 60}}))
    st.plotly_chart(fig_gauge, use_container_width=True)

    # 2. Historical Multi-Channel Trends
    st.subheader("Multi-Channel Penetration (2011-2024)")
    options = df['indicator'].unique().tolist()
    defaults = [opt for opt in options if "Ownership" in opt]

    indicators = st.multiselect("Select Channels", options, default=defaults)

    mask = df['indicator'].isin(indicators)
    fig_trend = px.line(
        df[mask], x='observation_date', y='value_numeric',
        color='indicator', markers=True
    )
    st.plotly_chart(fig_trend, use_container_width=True)

elif page == "Scenario Sandbox":
    st.header("Forecasting & Scenarios (2025-2027)")

    # 3. Forecast Chart with Confidence Intervals
    fig_fc = go.Figure()

    # Historical
    hist = df[df['indicator_code'] == 'ACC_OWNERSHIP']
    fig_fc.add_trace(go.Scatter(
        x=hist['year'], y=hist['value_numeric'],
        name="Historical", mode='lines+markers'
    ))

    # Forecast
    fig_fc.add_trace(go.Scatter(
        x=fc['year'], y=fc['Base'],
        name="Base Forecast", line=dict(dash='dash')
    ))

    # Confidence Bands
    x_ci = pd.concat([fc['year'], fc['year'][::-1]])
    y_ci = pd.concat([fc['Upper_CI'], fc['Lower_CI'][::-1]])
    fig_fc.add_trace(go.Scatter(
        x=x_ci, y=y_ci, fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line_color='rgba(255,255,255,0)',
        name='95% Confidence Interval'
    ))
    st.plotly_chart(fig_fc, use_container_width=True)

    # 4. Impact Summary
    st.subheader("Event Data Distribution")
    impact_df = df[df['record_type'] == 'event'].copy()
    fig_impact = px.strip(
        impact_df, x='confidence', y='indicator',
        color='source_type', title="Event Sourcing Confidence"
    )
    st.plotly_chart(fig_impact, use_container_width=True)
