import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

def generate_forecasts():
    # 1. Load Data
    df = pd.read_csv("data/processed/enriched_fi_data.csv")
    df['year'] = pd.to_datetime(df['observation_date']).dt.year
    
    # 2. Prepare Historical Baseline for ACC_OWNERSHIP
    hist = df[df['indicator_code'] == 'ACC_OWNERSHIP'].sort_values('year')
    X_hist = hist['year'].values.reshape(-1, 1)
    y_hist = hist['value_numeric'].values
    
    # 3. Fit Baseline Trend
    model = LinearRegression()
    model.fit(X_hist, y_hist)
    
    # 4. Forecast 2025-2027
    future_years = np.array([2025, 2026, 2027]).reshape(-1, 1)
    base_forecast = model.predict(future_years)
    
    # 5. Scenario Augmentation (Based on Task 3 Matrix)
    # Optimistic: NFIS-II implementation + Fayda adoption (Add +2pp per year)
    # Pessimistic: Slower adoption + inflation (Subtract -1pp per year)
    forecast_df = pd.DataFrame({
        'year': [2025, 2026, 2027],
        'Base': base_forecast,
        'Optimistic': base_forecast + np.array([2, 4, 6]),
        'Pessimistic': base_forecast - np.array([1, 2, 3])
    })
    
    # 6. Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(hist['year'], hist['value_numeric'], 'ko-', label='Historical Data')
    plt.plot(forecast_df['year'], forecast_df['Base'], 'b--', label='Base Scenario')
    plt.fill_between(forecast_df['year'], forecast_df['Pessimistic'], 
                     forecast_df['Optimistic'], color='blue', alpha=0.1, label='Scenario Range')
    
    plt.axhline(y=60, color='red', linestyle=':', label='NBE 60% Target')
    plt.title("Ethiopia Account Ownership Forecast (2025-2027)")
    plt.ylabel("Inclusion Rate (%)")
    plt.legend()
    plt.savefig("reports/figures/inclusion_forecast.png")
    
    os.makedirs("data/processed", exist_ok=True)
    forecast_df.to_csv("data/processed/forecast_results.csv", index=False)
    print("Forecasts generated and saved to data/processed/forecast_results.csv")
    return forecast_df

if __name__ == "__main__":
    generate_forecasts()