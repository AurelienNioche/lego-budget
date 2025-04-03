"""Main script to run LEGO Budget analysis."""

from rich.console import Console
from rich.panel import Panel

from lego_budget.utils import analyze_sets, get_sheet_data

console = Console()


def main() -> None:
    """Main function to run the LEGO Budget analysis."""
    try:
        console.print(
            Panel.fit(
                "[bold blue]LEGO Budget Analyzer[/bold blue]\n"
                "Analyzing your LEGO collection...",
                title="Welcome",
                border_style="blue",
            )
        )

        # Get data from Google Sheets
        df = get_sheet_data()

        # Analyze the data
        analyze_sets(df)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e!s}")
        raise


if __name__ == "__main__":
    main()
