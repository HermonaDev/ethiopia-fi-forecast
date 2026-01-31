# Interim Report: Ethiopia Financial Inclusion Forecasting

## 1. Data Enrichment Summary
The starter dataset was enriched to address sparse coverage in key indicators:
- **Baseline Addition:** Added 2011 Account Ownership (14%) from the Findex historical trajectory to provide a proper starting point for trend modeling.
- **Usage Metrics:** Injected 2024 estimates for Digital Payment Adoption (~35%) and Mobile Money ownership (9.45%) to enable Usage-pillar forecasting.
- **Why:** These points are essential to capture the full 13-year trajectory and calibrate the impact of recent digital transformations (Telebirr/M-Pesa).

## 2. Key Insights from EDA
1. **The 2021-2024 Stagnation:** Despite massive mobile money expansion (Telebirr/M-Pesa), account ownership grew only +3pp. This suggests a shift from "Access" growth to "Usage" depth.
2. **Infrastructure Lag:** 4G coverage and smartphone penetration show a high correlation with Usage, but a lower-than-expected direct impact on initial Account Ownership.
3. **Gender Gap Persistence:** Preliminary data suggests the male-female account ownership gap remains a significant barrier to the 60% national target.
4. **Interoperability Impact:** The crossover of P2P transfers surpassing ATM withdrawals marks a transition to a "Digital-First" economy.
5. **Data Sparsity:** The 3-year Findex cycle creates significant blind spots between 2017-2021, requiring event-augmented interpolation.

## 3. Preliminary Event-Indicator Relationships
Initial impact modeling shows:
- **Telebirr Launch (2021):** Shows a "High Positive" relationship with Mobile Money Accounts but a "Medium" impact on traditional Bank Account Ownership.
- **National Financial Inclusion Strategy (NFIS):** Appears as a high-magnitude driver for broad policy targets but with a significant implementation lag.

## 4. Identified Data Limitations
- Sparse frequency of Findex survey data (every 3 years).
- Discrepancy between "Registered" mobile money users (Telebirr reports) and "Active/Survey-reported" usage.