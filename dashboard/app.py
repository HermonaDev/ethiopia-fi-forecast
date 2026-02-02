import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# --- Page Config ---
st.set_page_config(
    page_title="Selam Analytics: FI Intelligence",
    layout="wide"
)


# --- Data Loading ---
@st.cache_data
def load_data():
    """Loads and caches processed datasets."""
    df = pd.read_csv("data/processed/enriched_fi_data.csv")
    fc = pd.read_csv("data/processed/forecast_results.csv")
    df['observation_date'] = pd.to_datetime(df['observation_date'])
    return df, fc


df, fc = load_data()


# --- Sidebar Navigation ---
st.sidebar.title("Selam Analytics")
page = st.sidebar.radio(
    "Dashboard Navigation",
    ["Executive Overview", "Historical Trends", "Inclusion Projections"]
)


# --- Page 1: Executive Overview ---
if page == "Executive Overview":
    st.title("🇪🇹 National Financial Inclusion Progress")

    st.subheader("1. Progress Toward 60% National Target")
    target_code = 'ACC_OWNERSHIP'
    latest_val = df[df['indicator_code'] == target_code].iloc[-1]
    val = latest_val['value_numeric']

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=val,
        title={'text': "Current Account Ownership Rate (%)"},
        delta={'reference': 60, 'increasing': {'color': "green"}},
        gauge={'axis': {'range': [None, 100]},
               'threshold': {'line': {'color': "red", 'width': 4},
                             'value': 60}}))
    st.plotly_chart(fig_gauge, use_container_width=True)
    st.write(
        "**Analysis:** This gauge tracks Ethiopia's current status "
        "against the NFIS-II target of 60%. As of 2024, "
        "an 11-point gap remains."
    )


# --- Page 2: Historical Trends ---
elif page == "Historical Trends":
    st.title("📈 Multi-Channel Trend Analysis")

    col1, col2 = st.columns(2)
    with col1:
        opts = df['indicator'].unique().tolist()
        defs = [opt for opt in opts if "Ownership" in opt]
        selected_inds = st.multiselect("Select Indicators", opts, defs)
    with col2:
        min_date = df['observation_date'].min().date()
        max_date = df['observation_date'].max().date()
        date_range = st.slider(
            "Select Date Range", min_date, max_date,
            (min_date, max_date)
        )

    mask = (df['indicator'].isin(selected_inds)) & \
           (df['observation_date'].dt.date.between(*date_range))

    fig_trend = px.line(
        df[mask], x='observation_date', y='value_numeric',
        color='indicator', markers=True
    )
    st.plotly_chart(fig_trend, use_container_width=True)
    st.write(
        "**Insight:** This chart allows stakeholders to compare "
        "different inclusion channels (e.g., Mobile Money vs. "
        "Banking) across custom time windows."
    )


# --- Page 3: Inclusion Projections ---
elif page == "Inclusion Projections":
    st.title("🔮 Forecasting & Policy Scenarios (2025-2027)")

    st.subheader("3. Strategic Scenario Forecast")
    scenario = st.selectbox(
        "Select Policy Scenario",
        ["Base", "Optimistic"]
    )

    fig_fc = go.Figure()
    hist = df[df['indicator_code'] == 'ACC_OWNERSHIP']

    fig_fc.add_trace(go.Scatter(
        x=hist['year'], y=hist['value_numeric'],
        name="Historical Data", mode='lines+markers'
    ))
    fig_fc.add_trace(go.Scatter(
        x=fc['year'], y=fc[scenario],
        name=f"{scenario} Forecast",
        line=dict(dash='dash', width=4)
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
    st.write(
        f"**Forecast Note:** The {scenario} scenario projects "
        "the impact of current interventions. Shaded areas "
        "represent model uncertainty."
    )

    st.subheader("4. Event Evidence & Data Quality")
    impact_df = df[df['record_type'] == 'event'].copy()
    fig_strip = px.strip(
        impact_df, x='confidence', y='indicator',
        color='source_type', title="Evidence Provenance"
    )
    st.plotly_chart(fig_strip, use_container_width=True)
    st.write(
        "**Evidence Basis:** This plot displays the distribution "
        "of qualitative events by sourcing confidence."
    )
