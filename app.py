import streamlit as st
import pandas as pd
import io

import pull_nse_data
import merge_csvs
import os

# 1. Replace this with your actual niftyindeces.com scraping logic
def fetch_sector_data(sectors):
    return pull_nse_data.fetch_data(sectors)

# 2. Convert DataFrame to in-memory Excel file
def convert_df_to_excel(df):
    # Call the refactored merge_csvs function to generate formatted Excel with summary
    return merge_csvs.generate_excel_from_dataframe(df, output_target=None)

# --- Streamlit UI ---
st.title("Nifty Sector Data Downloader")

# Update this list with all available indices from your script
available_indices = ['NIFTY AUTO','NIFTY BANK','NIFTY CEMENT','NIFTY CHEMICALS','NIFTY FINANCE',
    'NIFTY FINANCIAL SERVICES 25-50','NIFTY FINANCIAL SERVICES EX-BANK','NIFTY FMCG',
    'NIFTY HEALTHCARE','NIFTY IT','NIFTY MEDIA',
    'NIFTY METAL','NIFTY PHARMA','NIFTY PRIVATE BANK',
    'NIFTY PSU BANK','NIFTY REALTY','NIFTY CONSUMER DURABLES',
    'NIFTY OIL & GAS','NIFTY 500 HEALTHCARE','NIFTY MID SMALL FINANCIAL SERVICE',
    'NIFTY MID SMALL HEALTHCARE','NIFTY MID SMALL IT & TELECOM']

sectors = [
    'niftyauto','niftybank','NiftyCement_','niftyChemicals_','niftyfinance',
    'niftyfinancialservices25-50','niftyfinancialservicesexbank_','niftyfmcg',
    'niftyhealthcare','niftyit','niftymedia',
    'niftymetal','niftypharma','nifty_privatebank',
    'niftypsubank','niftyrealty','niftyconsumerdurables',
    'niftyoilgas','nifty500Healthcare_','niftymidsmallfinancailservice_',
    'niftymidsmallhealthcare_','niftymidsmallitAndtelecom_'
]

sector_mapping = dict(zip(available_indices, sectors))

selected_indices = st.multiselect("Select the indices you want to download:", list(sector_mapping.keys()))

if st.button("Generate Consolidated Data"):
    if not selected_indices:
        st.error("Please select at least one sector.")
    else:
        selected_sectors = [sector_mapping[idx] for idx in selected_indices]
        with st.spinner('Pulling data...'):
            df = fetch_sector_data(selected_sectors)
            excel_data = convert_df_to_excel(df)
            
        st.success("File ready!")
        
        # 3. Serve the file to the user
        st.download_button(
            label="Download Excel",
            data=excel_data,
            file_name="nifty_consolidated.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )