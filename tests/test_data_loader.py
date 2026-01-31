import pytest
import pandas as pd
import numpy as np
from src.data_loader import get_data_summary

def test_data_summary_logic():
    # Mock data to test the logic
    mock_df = pd.DataFrame({
        'record_type': ['observation', 'observation', 'event', 'target'],
        'pillar': ['access', 'usage', 'infrastructure', 'access']
    })
    summary = get_data_summary(mock_df)
    assert summary['total_records'] == 4
    assert summary['by_type']['observation'] == 2
    assert summary['by_type']['event'] == 1