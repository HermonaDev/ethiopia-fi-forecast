import pandas as pd
import os
from typing import Tuple, Dict, Any

def load_data(filename: str) -> pd.DataFrame:
    """
    Loads a CSV file from the data/raw directory.
    
    Args:
        filename: Name of the file (e.g., 'reference_codes.csv')
    Returns:
        pd.DataFrame: The loaded data
    """
    filepath = os.path.join("data/raw", filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Missing file: {filepath}")
    return pd.read_csv(filepath)

def get_data_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generates a systematic exploration of the dataset by pillar and record type.
    """
    return {
        "record_counts": df['record_type'].value_counts().to_dict(),
        "pillar_distribution": df['pillar'].value_counts().to_dict() if 'pillar' in df.columns else {},
        "confidence_levels": df['confidence'].value_counts().to_dict() if 'confidence' in df.columns else {}
    }