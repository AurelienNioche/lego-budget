"""Data analysis module for LEGO Budget Analyzer."""

import pandas as pd
from rich.console import Console

from .tables import (
    all_sets_table,
    lego_vs_lepin_table,
    monthly_spending_table,
    overview_table,
    status_table,
)

console = Console()


def analyze_sets(df: pd.DataFrame) -> None:
    """Analyze and display statistics about LEGO sets."""
    # Total spending
    total_spending = df["Price"].sum()
    total_pieces = df["Number of pieces"].sum()
    total_price_per_piece = total_spending / total_pieces

    # Calculate price per piece for all sets (for individual rows)
    df["price_per_piece"] = df["Price"] / df["Number of pieces"]

    overview_table(
        console=console,
        total_spending=total_spending,
        total_price_per_piece=total_price_per_piece,
    )

    monthly_spending_table(console=console, df=df)

    status_table(
        console=console,
        df=df,
        total_price_per_piece=total_price_per_piece,
    )

    lego_vs_lepin_table(
        console=console,
        df=df,
        total_price_per_piece=total_price_per_piece,
    )

    all_sets_table(console=console, df=df)
