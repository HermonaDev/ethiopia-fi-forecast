import pandas as pd
from data_loader import load_data

def analyze_coverage():
    df = load_data("ethiopia_fi_unified_data.csv")
    
    # Filter only observations (the actual measured points)
    obs = df[df['record_type'] == 'observation'].copy()
    
    # Clean the year/date
    # Some dates might be years (2011) or full dates (2011-01-01)
    obs['year'] = pd.to_datetime(obs['observation_date']).dt.year
    
    print("\n--- Unique Indicators and Year Coverage ---")
    coverage = obs.groupby('indicator_code')['year'].unique().apply(sorted)
    print(coverage)
    
    # Check the core targets specifically
    targets = ['ACC_OWNERSHIP', 'USG_DIGITAL_PAYMENT']
    print("\n--- Target Indicator Coverage ---")
    for t in targets:
        years = obs[obs['indicator_code'] == t]['year'].unique()
        print(f"{t}: {sorted(years)}")

if __name__ == "__main__":
    analyze_coverage()