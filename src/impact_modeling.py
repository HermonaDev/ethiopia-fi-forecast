import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from typing import Optional


def build_impact_matrix() -> Optional[pd.DataFrame]:
    """
    Builds the Event-Indicator Association Matrix.

    Returns:
        Optional[pd.DataFrame]: Impact matrix or None if empty.
    """
    # 1. Load data
    df_data = pd.read_csv("data/processed/enriched_fi_data.csv")
    df_links = pd.read_csv("data/raw/ethiopia_fi_impact_links.csv")

    # 2. Extract events
    events = df_data[df_data['record_type'] == 'event']
    events = events[['record_id', 'indicator', 'observation_date']]
    events = events.rename(
        columns={'record_id': 'parent_id', 'indicator': 'event_name'}
    )

    # 3. Force join keys to string
    events['parent_id'] = events['parent_id'].astype(str)
    df_links['parent_id'] = df_links['parent_id'].astype(str)

    # 4. Join events with impact links
    impact_joined = pd.merge(df_links, events, on='parent_id', how='inner')

    if impact_joined.empty:
        return None

    # 5. Create numeric magnitude
    mag_map = {'high': 3, 'medium': 2, 'low': 1}
    impact_joined['numeric_magnitude'] = (
        impact_joined['impact_magnitude'].str.lower().map(mag_map)
    )

    # Adjust sign based on direction
    is_dec = impact_joined['impact_direction'].str.lower() == 'decrease'
    impact_joined.loc[is_dec, 'numeric_magnitude'] *= -1

    # 6. Pivot into Matrix
    matrix = impact_joined.pivot_table(
        index='event_name',
        columns='related_indicator',
        values='numeric_magnitude',
        aggfunc='mean',
        fill_value=0
    )

    # 7. Visualization
    plt.figure(figsize=(12, 8))
    sns.heatmap(matrix, annot=True, cmap="RdYlGn", center=0)
    plt.title("Event-Indicator Association Matrix")
    plt.tight_layout()

    os.makedirs("reports/figures", exist_ok=True)
    plt.savefig("reports/figures/impact_matrix.png")
    return matrix


if __name__ == "__main__":
    build_impact_matrix()
