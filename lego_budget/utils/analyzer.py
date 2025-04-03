"""Data analysis module for LEGO Budget Analyzer."""

import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()


def analyze_sets(df: pd.DataFrame) -> None:
    """Analyze and display statistics about LEGO sets."""
    # Total spending
    total_spending = df["Price"].sum()
    total_pieces = df["Number of pieces"].sum()
    total_price_per_piece = total_spending / total_pieces

    # Calculate price per piece for all sets (for individual rows)
    df["price_per_piece"] = df["Price"] / df["Number of pieces"]

    # Status distribution with spending
    status_stats = (
        df.groupby("Status")
        .agg(
            {
                "Set": "count",
                "Number of pieces": "sum",
                "Price": "sum",
            }
        )
        .round(2)
    )
    # Calculate price per piece for each status
    status_stats["price_per_piece"] = (
        status_stats["Price"] / status_stats["Number of pieces"]
    ).round(3)

    # Product distribution with spending
    product_stats = (
        df.groupby("Product")
        .agg(
            {
                "Set": "count",
                "Number of pieces": "sum",
                "Price": "sum",
            }
        )
        .round(2)
    )
    # Calculate price per piece for each product
    product_stats["price_per_piece"] = (
        product_stats["Price"] / product_stats["Number of pieces"]
    ).round(3)

    # Technic distribution with spending
    technic_stats = (
        df.groupby("Technic")
        .agg(
            {
                "Set": "count",
                "Number of pieces": "sum",
                "Price": "sum",
            }
        )
        .round(2)
    )
    # Calculate price per piece for each type
    technic_stats["price_per_piece"] = (
        technic_stats["Price"] / technic_stats["Number of pieces"]
    ).round(3)

    # Display results
    console.print("\n[bold blue]LEGO Budget Analysis[/bold blue]")

    # Spending table
    spending_table = Table(title="Spending Overview")
    spending_table.add_column("Metric", style="cyan")
    spending_table.add_column("Value", style="green")
    spending_table.add_row("Total Spending", f"{total_spending:.2f} €")
    spending_table.add_row("Average Price per Piece", f"{total_price_per_piece:.3f} €")
    console.print(spending_table)

    # Monthly analysis
    if "Order date" in df.columns:
        # Convert Order date column to datetime
        df["Order date"] = pd.to_datetime(df["Order date"])
        # Extract month and year
        df["Month"] = df["Order date"].dt.month
        df["Year"] = df["Order date"].dt.year

        # Monthly statistics
        monthly_stats = (
            df.groupby(["Year", "Month"])
            .agg(
                {
                    "Set": "count",
                    "Number of pieces": "sum",
                    "Price": "sum",
                }
            )
            .round(2)
        )

        # Display monthly analysis
        monthly_table = Table(title="Monthly Spending and Purchases")
        monthly_table.add_column("Year", style="cyan")
        monthly_table.add_column("Month", style="green")
        monthly_table.add_column("Sets Bought", style="yellow")
        monthly_table.add_column("Total Pieces", style="magenta")
        monthly_table.add_column("Total Spent", style="red")

        # Month names for display
        month_names = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]

        # Sort by year and month
        for year, month in sorted(monthly_stats.index):
            monthly_table.add_row(
                str(year),
                month_names[month - 1],
                str(int(monthly_stats.loc[(year, month), "Set"])),
                str(int(monthly_stats.loc[(year, month), "Number of pieces"])),
                f"{monthly_stats.loc[(year, month), 'Price']:.2f} €",
            )
        # Add total row
        monthly_table.add_row(
            "[bold]Total[/bold]",
            "",
            str(int(monthly_stats["Set"].sum())),
            str(int(monthly_stats["Number of pieces"].sum())),
            f"{monthly_stats['Price'].sum():.2f} €",
        )
        console.print(monthly_table)

    # Status distribution table
    status_table = Table(title="Set Status Distribution")
    status_table.add_column("Status", style="cyan")
    status_table.add_column("Set Count", style="green")
    status_table.add_column("Piece Count", style="yellow")
    status_table.add_column("Spent", style="red")
    status_table.add_column("Avg Price/Piece", style="magenta")
    for status in status_stats.index:
        status_table.add_row(
            status,
            str(status_stats.loc[status, "Set"]),
            str(int(status_stats.loc[status, "Number of pieces"])),
            f"{status_stats.loc[status, 'Price']:.2f} €",
            f"{status_stats.loc[status, 'price_per_piece']:.3f} €",
        )
    # Add total row
    status_table.add_row(
        "[bold]Total[/bold]",
        str(status_stats["Set"].sum()),
        str(int(status_stats["Number of pieces"].sum())),
        f"{status_stats['Price'].sum():.2f} €",
        f"{total_price_per_piece:.3f} €",
    )
    console.print(status_table)

    # Product distribution table
    product_table = Table(title="Product Distribution")
    product_table.add_column("Product", style="cyan")
    product_table.add_column("Set Count", style="green")
    product_table.add_column("Piece Count", style="yellow")
    product_table.add_column("Spent", style="red")
    product_table.add_column("Avg Price/Piece", style="magenta")
    for product in product_stats.index:
        product_table.add_row(
            product,
            str(product_stats.loc[product, "Set"]),
            str(int(product_stats.loc[product, "Number of pieces"])),
            f"{product_stats.loc[product, 'Price']:.2f} €",
            f"{product_stats.loc[product, 'price_per_piece']:.3f} €",
        )
    # Add total row
    product_table.add_row(
        "[bold]Total[/bold]",
        str(product_stats["Set"].sum()),
        str(int(product_stats["Number of pieces"].sum())),
        f"{product_stats['Price'].sum():.2f} €",
        f"{total_price_per_piece:.3f} €",
    )
    console.print(product_table)

    # Technic distribution table
    technic_table = Table(title="Technic vs Regular Distribution")
    technic_table.add_column("Type", style="cyan")
    technic_table.add_column("Set Count", style="green")
    technic_table.add_column("Piece Count", style="yellow")
    technic_table.add_column("Spent", style="red")
    technic_table.add_column("Avg Price/Piece", style="magenta")
    for technic in technic_stats.index:
        technic_table.add_row(
            technic,
            str(technic_stats.loc[technic, "Set"]),
            str(int(technic_stats.loc[technic, "Number of pieces"])),
            f"{technic_stats.loc[technic, 'Price']:.2f} €",
            f"{technic_stats.loc[technic, 'price_per_piece']:.3f} €",
        )
    # Add total row
    technic_table.add_row(
        "[bold]Total[/bold]",
        str(technic_stats["Set"].sum()),
        str(int(technic_stats["Number of pieces"].sum())),
        f"{technic_stats['Price'].sum():.2f} €",
        f"{total_price_per_piece:.3f} €",
    )
    console.print(technic_table)

    # Most expensive sets
    console.print("\n[bold blue]Most Expensive Sets[/bold blue]")
    expensive_table = Table(title="Top 5 Most Expensive Sets")
    expensive_table.add_column("Set", style="cyan")
    expensive_table.add_column("Price", style="green")
    expensive_table.add_column("Pieces", style="yellow")
    expensive_table.add_column("Price/Piece", style="magenta")

    top_expensive = df.nlargest(5, "Price")
    for _, row in top_expensive.iterrows():
        expensive_table.add_row(
            row["Set"],
            f"{row['Price']:.2f} €",
            str(row["Number of pieces"]),
            f"{row['price_per_piece']:.3f} €",
        )
    console.print(expensive_table)

    # Least expensive sets
    console.print("\n[bold blue]Least Expensive Sets[/bold blue]")
    cheap_table = Table(title="Top 5 Least Expensive Sets")
    cheap_table.add_column("Set", style="cyan")
    cheap_table.add_column("Price", style="green")
    cheap_table.add_column("Pieces", style="yellow")
    cheap_table.add_column("Price/Piece", style="magenta")

    top_cheap = df.nsmallest(5, "Price")
    for _, row in top_cheap.iterrows():
        cheap_table.add_row(
            row["Set"],
            f"{row['Price']:.2f} €",
            str(row["Number of pieces"]),
            f"{row['price_per_piece']:.3f} €",
        )
    console.print(cheap_table)

    # All sets sorted by price per piece
    console.print("\n[bold blue]All Sets Sorted by Price per Piece[/bold blue]")
    all_sets_table = Table(title="All Sets (Price per Piece)")
    all_sets_table.add_column("Set", style="cyan")
    all_sets_table.add_column("Price", style="green")
    all_sets_table.add_column("Pieces", style="yellow")
    all_sets_table.add_column("Price/Piece", style="magenta")

    # Sort all sets by price per piece in descending order
    sorted_sets = df.sort_values("price_per_piece", ascending=False)
    for _, row in sorted_sets.iterrows():
        all_sets_table.add_row(
            row["Set"],
            f"{row['Price']:.2f} €",
            str(row["Number of pieces"]),
            f"{row['price_per_piece']:.3f} €",
        )
    console.print(all_sets_table)
