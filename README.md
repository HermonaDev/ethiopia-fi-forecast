# Ethiopia Financial Inclusion Forecasting System

## 🇪🇹 Project Overview
As a Data Scientist at **Selam Analytics**, I am developing a forecasting system for a consortium (National Bank of Ethiopia, Mobile Money Operators, and Development Finance Institutions). The goal is to track and predict Ethiopia's digital financial transformation using time series methods, specifically focusing on **Access** (Account Ownership) and **Usage** (Digital Payments).

## 🛠 Project Structure
```text
ethiopia-fi-forecast/
├── .github/workflows/
│   └── unittests.yml      # CI/CD pipeline for Flake8 linting
├── data/
│   ├── raw/               # Starter datasets (Unified Schema & Impact Links)
│   └── processed/         # Enriched and analysis-ready data
├── src/
│   ├── data_loader.py     # Robust multi-sheet unified data loader
│   ├── enrichment.py      # Pipeline for programmatic data enrichment
│   ├── eda_visualizer.py  # Trajectory and growth analysis
│   └── impact_modeling.py # Event-Indicator association matrix logic
├── reports/
│   └── figures/           # Generated visualizations for stakeholders
├── tests/                 # Unit tests for data integrity
├── requirements.txt       # Dependency management
└── INTERIM_REPORT.md      # Detailed analysis of Task 1-3 findings
```

## 📈 Current Progress (Interim Milestone)
- **Task 1: Data Exploration & Enrichment**
  - Implemented a unified schema loader for `observations`, `events`, and `impact_links`.
  - Enriched data with 2011 Findex baselines and 2024 Usage metrics to resolve sparse data limitations.
- **Task 2: Exploratory Data Analysis (EDA)**
  - Visualized the 13-year trajectory of account ownership.
  - Identified a significant "Access Stagnation" between 2021-2024 (+3pp growth).
- **Task 3: Event Impact Modeling**
  - Developed an **Event-Indicator Association Matrix**.
  - Quantified the impact of Telebirr, Safaricom, and M-Pesa launches on inclusion indicators.

## 🚀 Installation & Usage
1. **Clone and Setup:**
   ```bash
   git clone https://github.com/[your-username]/ethiopia-fi-forecast.git
   cd ethiopia-fi-forecast
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Run Pipeline:**
   ```bash
   python3 src/enrichment.py      # Enriches raw data
   python3 src/eda_visualizer.py  # Generates trajectory plots
   python3 src/impact_modeling.py # Generates impact heatmap
   ```

## ⚖️ Engineering Standards
- **Unified Schema Compliance:** All records share a consistent structure to ensure unbiased event impact estimation.
- **CI/CD:** Automated linting with `flake8` and testing via GitHub Actions.
- **Data Integrity:** Strict `.gitignore` policy to prevent sensitive data exposure.

---
**Author:** Hermona Dev  
**Status:** Interim Submission Complete (Task 1-3)
```
