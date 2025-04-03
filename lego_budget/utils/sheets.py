"""Data loading module for LEGO Budget Analyzer."""

import os

import gspread
import pandas as pd
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials


def get_sheet_data() -> pd.DataFrame:
    """Load data directly from Google Sheet and return it as a pandas DataFrame."""
    load_dotenv()

    # Get the spreadsheet URL from environment variable
    spreadsheet_url = os.getenv("SPREADSHEET_URL")
    if not spreadsheet_url:
        raise ValueError("SPREADSHEET_URL not found in environment variables")

    # Get the credentials file path
    credentials_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS", "credentials.json")
    if not os.path.exists(credentials_path):
        raise FileNotFoundError(f"Credentials file not found at {credentials_path}")

    # Set up the credentials
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = Credentials.from_service_account_file(credentials_path, scopes=scopes)

    # Connect to Google Sheets
    gc = gspread.authorize(credentials)

    # Open the spreadsheet by URL
    sheet = gc.open_by_url(spreadsheet_url)

    # Get the first worksheet
    worksheet = sheet.get_worksheet(0)

    # Get all records
    records = worksheet.get_all_records()

    # Convert to DataFrame
    df = pd.DataFrame(records)

    # Remove rows where Set is empty or contains a total
    df = df[df["Set"].notna() & (df["Set"] != "")]

    # Clean up data
    # Remove € symbol, non-breaking spaces, and convert comma to dot
    df["Price"] = (
        df["Price"]
        .str.replace("€", "")
        .str.replace("\xa0", "")
        .str.replace(",", ".")
        .str.strip()
        .astype(float)
    )
    df["Number of pieces"] = pd.to_numeric(df["Number of pieces"], errors="coerce")

    return df
