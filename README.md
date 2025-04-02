# LEGO Budget Analyzer

A Python tool to analyze LEGO set purchases and track building progress.

## Features

- Read and analyze LEGO set data from Google Sheets
- Track set status (Built, In Progress, Ordered, Stored)
- Calculate total spending and statistics
- Analyze Technic vs Regular sets distribution
- Track building progress

## Setup

### 1. Clone and Install

```bash
# Clone the repository
git clone <repository-url>
cd lego-budget

# Create and activate virtual environment using uv
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows

# Install dependencies
uv pip install -e .
```

### 2. Google Sheets API Setup

1. Go to the Google Cloud Console:
   - Visit https://console.cloud.google.com/
   - Sign in with your Google account

2. Create a new project:
   - Click on the project dropdown at the top of the page
   - Click "New Project"
   - Name it something like "lego-budget"
   - Click "Create"

3. Enable the Google Sheets API:
   - In the left sidebar, click on "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click on it and then click "Enable"

4. Create a service account:
   - In the left sidebar, click on "APIs & Services" > "Credentials"
   - Click "Create Credentials" at the top
   - Select "Service Account"
   - Fill in the details:
     - Service account name: "lego-budget"
     - Service account ID: will auto-generate
     - Description: "Service account for LEGO Budget Analyzer"
   - Click "Create and Continue"
   - For the role, select "Viewer" (since we only need read access)
   - Click "Continue"
   - Click "Done"

5. Create and download the key:
   - In the Credentials page, find your new service account
   - Click on the service account email
   - Go to the "Keys" tab
   - Click "Add Key" > "Create new key"
   - Choose "JSON" format
   - Click "Create"
   - The JSON file will automatically download

### 3. Project Configuration

1. Move the downloaded JSON file to your project directory and rename it:
```bash
mv ~/Downloads/your-credentials.json credentials.json
```

2. Create and configure environment variables:
```bash
cp .env.example .env
```

3. Edit `.env` to add your Google Sheet URL:
```
SPREADSHEET_URL=your-google-sheet-url
```

4. Share your Google Sheet:
   - Open your Google Sheet
   - Click "Share" button
   - Add the service account email (it looks like `something@project-id.iam.gserviceaccount.com`)
   - Give it "Viewer" access
   - Click "Share"

## Usage

Run the analysis:
```bash
python -m lego_budget.run_stats
```

This will display:
- Total spending
- Set status distribution
- Product distribution (Lego vs Lepin)
- Technic vs Regular distribution
- Most expensive sets
- Price per piece statistics

## Development

For development, install additional tools:
```bash
uv pip install -e ".[dev]"
```

Run linting:
```bash
ruff check .
ruff format .
```

Run tests:
```bash
pytest
```

## Project Structure

- `lego_budget/`: Main package directory
  - `__init__.py`: Package initialization
  - `run_stats.py`: Main script to run analysis
  - `utils/`: Utility modules
    - `__init__.py`: Utils package initialization
    - `sheets.py`: Google Sheets integration
    - `analyzer.py`: Data analysis logic
- `tests/`: Test files
- `pyproject.toml`: Project configuration and dependencies
- `.env`: Environment variables (not in git)
- `.gitignore`: Git ignore rules 