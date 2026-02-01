import pandas as pd
from data_loader import load_data


def analyze_coverage():
    df = load_data("ethiopia_fi_unified_data.csv")
    obs = df[df['record_type'] == 'observation'].copy()
    obs['year'] = pd.to_datetime(obs['observation_date']).dt.year

    print("\n--- Unique Indicators and Year Coverage ---")
    coverage = obs.groupby('indicator_code')['year'].unique()
    print(coverage.apply(sorted))

    targets = ['ACC_OWNERSHIP', 'USG_DIGITAL_PAYMENT']
    print("\n--- Target Indicator Coverage ---")
    for t in targets:
        years = obs[obs['indicator_code'] == t]['year'].unique()
        print(f"{t}: {sorted(years)}")


if __name__ == "__main__":
    analyze_coverage()
