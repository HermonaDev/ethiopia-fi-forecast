import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os
import config


def generate_forecasts() -> pd.DataFrame:
    """
    Generates forecasts with residual-based confidence intervals.
    """
    path = os.path.join(config.PROCESSED_DATA_DIR, "enriched_fi_data.csv")
    df = pd.read_csv(path)
    df['year'] = pd.to_datetime(df['observation_date']).dt.year

    hist = df[df['indicator_code'] == config.TARGET_COLUMN].sort_values('year')
    x_h = hist['year'].values.reshape(-1, 1)
    y_h = hist['value_numeric'].values

    model = LinearRegression()
    model.fit(x_h, y_h)

    # Calculate Residuals for Confidence Intervals
    y_pred_h = model.predict(x_h)
    residuals = y_h - y_pred_h
    std_error = np.std(residuals)

    future_years = np.array([2025, 2026, 2027]).reshape(-1, 1)
    base_forecast = model.predict(future_years)

    # 95% Confidence Interval (approx 1.96 * std_error)
    ci = 1.96 * std_error

    forecast_df = pd.DataFrame({
        'year': [2025, 2026, 2027],
        'Base': base_forecast,
        'Lower_CI': base_forecast - ci,
        'Upper_CI': base_forecast + ci,
        'Optimistic': base_forecast + np.array([2, 4, 6])
    })

    out_path = os.path.join(config.PROCESSED_DATA_DIR, "forecast_results.csv")
    forecast_df.to_csv(out_path, index=False)
    return forecast_df


if __name__ == "__main__":
    generate_forecasts()
