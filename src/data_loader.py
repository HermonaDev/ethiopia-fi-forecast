import pandas as pd
import os

def load_data(filename: str) -> pd.DataFrame:
    """Helper to load csv from data/raw."""
    filepath = os.path.join("data/raw", filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Missing file: {filepath}")
    return pd.read_csv(filepath)

def get_full_dataset():
    """Returns both the unified data and the impact links."""
    data = load_data("ethiopia_fi_unified_data.csv")
    links = load_data("ethiopia_fi_impact_links.csv")
    return data, links

if __name__ == "__main__":
    try:
        df_data, df_links = get_full_dataset()
        print("\n--- Sheet 1: Unified Data ---")
        print(df_data['record_type'].value_counts())
        
        print("\n--- Sheet 2: Impact Links ---")
        print(f"Total Impact Links: {len(df_links)}")
        if 'impact_direction' in df_links.columns:
            print(df_links['impact_direction'].value_counts())
            
    except Exception as e:
        print(f"Error loading data: {e}")