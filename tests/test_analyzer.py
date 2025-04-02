"""Tests for the analyzer module."""

import pandas as pd
import pytest

from lego_budget.utils.analyzer import analyze_sets

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        "Set": ["Set1", "Set2", "Set3"],
        "Product": ["Lego", "Lepin", "Lego"],
        "Technic": ["Regular", "Technic", "Regular"],
        "Number of pieces": [1000, 2000, 1500],
        "Status": ["Built", "In progress", "Ordered"],
        "Price": [100.0, 50.0, 75.0]
    })

def test_analyze_sets(sample_data, capsys):
    """Test that analyze_sets runs without errors."""
    analyze_sets(sample_data)
    captured = capsys.readouterr()
    assert "LEGO Budget Analysis" in captured.out
    assert "Spending Overview" in captured.out
    assert "Set Status Distribution" in captured.out
    assert "Product Distribution" in captured.out
    assert "Technic vs Regular Distribution" in captured.out
    assert "Most Expensive Sets" in captured.out 