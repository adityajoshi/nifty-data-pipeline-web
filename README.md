# Nifty Data Pipeline Web

A Streamlit web application that downloads and consolidates Nifty indices constituent data from the [niftyindices.com](https://niftyindices.com/) website directly into memory, exporting it as an Excel `.xlsx` file.

## Features
- Fetches the latest stock constituents for various Nifty indices (e.g., NIFTY AUTO, NIFTY BANK, NIFTY IT).
- **Fully in-memory processing**: No intermediate CSV or Excel files are dumped onto your system. Everything runs completely in memory.
- User-friendly web interface powered by Streamlit.
- Provides a clean, consolidated Excel dataset for all selected indices.

## Requirements

Ensure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application by running the following command in your terminal:
```bash
streamlit run app.py
```

## Usage
1. Open your browser to the local URL provided by Streamlit (usually `http://localhost:8501`).
2. Select the desired Nifty indices from the multi-select dropdown.
3. Click **Generate Consolidated Data**.
4. Once processing finishes, click **Download Excel** to get your combined `.xlsx` file!

## Structure
- `app.py`: The main Streamlit frontend application. Handles UI rendering, user selections, and combining the data into an `.xlsx` download.
- `pull_nse_data.py`: The backend data-fetching module. Issues web requests to the Nifty indices portal and processes the raw string data into pandas DataFrames on the fly.
