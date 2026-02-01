# Ethiopia Financial Inclusion Forecasting System

## Project Overview
This system tracks and forecasts Ethiopia's progress toward national financial inclusion targets (Digital Ethiopia 2025). Developed for **Selam Analytics**, the system models the impact of policy and infrastructure interventions on **Account Ownership** and **Digital Payment Adoption**.

## Features
- **Unified Schema Analysis**: Integration of hard observations with qualitative event impacts.
- **Scenario-Based Forecasting**: Generates Optimistic, Base, and Pessimistic trajectories for 2025-2027.
- **Impact Modeling**: Quantitative association matrix mapping events (e.g., Telebirr Launch) to inclusion indicators.
- **Interactive Dashboard**: Streamlit interface for stakeholders to explore trends and policy scenarios.

## Project Structure
- `src/`: Core logic for data ingestion, enrichment, and modeling.
- `dashboard/`: Streamlit application files.
- `data/raw/`: Starter datasets (Unified Schema).
- `data/processed/`: Analysis-ready and enriched datasets.
- `reports/figures/`: Visualizations for stakeholders.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
1. **Data Enrichment**: `python src/enrichment.py`
2. **Impact Modeling**: `python src/impact_modeling.py`
3. **Forecasting**: `python src/forecaster.py`
4. **Launch Dashboard**: `streamlit run dashboard/app.py`

## Engineering Standards
- **PEP 8 Compliance**: Enforced via flake8.
- **Documentation**: Google-style docstrings and Python Type Hints throughout the codebase.
