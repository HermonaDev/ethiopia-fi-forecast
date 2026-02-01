import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def generate_forecasts() -> pd.DataFrame:
    """
    Builds a scenario-based forecast for Account Ownership.

    Returns:
        pd.DataFrame: Forecasted values for 2025-2027.
    """
    df = pd.read_csv("data/processed/enriched_fi_data.csv")
    df['year'] = pd.to_datetime(df['observation_date']).dt.year

    hist = df[df['indicator_code'] == 'ACC_OWNERSHIP'].sort_values('year')
    x_h = hist['year'].values.reshape(-1, 1)
    y_h = hist['value_numeric'].values

    model = LinearRegression()
    model.fit(x_h, y_h)

    future_years = np.array([2025, 2026, 2027]).reshape(-1, 1)
    base_forecast = model.predict(future_years)

    forecast_df = pd.DataFrame({
        'year': [2025, 2026, 2027],
        'Base': base_forecast,
        'Optimistic': base_forecast + np.array([2, 4, 6]),
        'Pessimistic': base_forecast - np.array([1, 2, 3])
    })

    plt.figure(figsize=(10, 6))
    plt.plot(hist['year'], hist['value_numeric'], 'ko-', label='Hist')
    plt.plot(forecast_df['year'], forecast_df['Base'], 'b--', label='Base')
    plt.fill_between(
        forecast_df['year'], forecast_df['Pessimistic'],
        forecast_df['Optimistic'], color='blue', alpha=0.1, label='Range'
    )

    plt.axhline(y=60, color='red', linestyle=':', label='Target')
    plt.savefig("reports/figures/inclusion_forecast.png")
    forecast_df.to_csv("data/processed/forecast_results.csv", index=False)
    return forecast_df


if __name__ == "__main__":
    generate_forecasts()
