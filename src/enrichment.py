import pandas as pd
from data_loader import load_data
import os


def enrich_dataset() -> str:
    """
    Enriches the dataset with 2011 baseline and 2024 survey estimates.

    Returns:
        str: Path to the enriched CSV file.
    """
    df = load_data("ethiopia_fi_unified_data.csv")

    new_observations = [
        {
            'record_type': 'observation', 'pillar': 'access',
            'indicator': 'Account Ownership',
            'indicator_code': 'ACC_OWNERSHIP', 'value_numeric': 14.0,
            'observation_date': '2011-12-31',
            'source_type': 'survey', 'confidence': 'high'
        },
        {
            'record_type': 'observation', 'pillar': 'usage',
            'indicator': 'Digital Payment Adoption',
            'indicator_code': 'USG_DIGITAL_PAYMENT', 'value_numeric': 35.0,
            'observation_date': '2024-12-31',
            'source_type': 'survey', 'confidence': 'medium'
        }
    ]

    enrich_df = pd.DataFrame(new_observations)
    df_final = pd.concat([df, enrich_df], ignore_index=True)

    output_path = "data/processed/enriched_fi_data.csv"
    os.makedirs("data/processed", exist_ok=True)
    df_final.to_csv(output_path, index=False)
    return output_path


if __name__ == "__main__":
    enrich_dataset()
