import pandas as pd
import requests
import io
import os

# Define the sectors/indices you want to download
sectors = [
    'niftyauto','niftybank','NiftyCement_','niftyChemicals_','niftyfinance',
    'niftyfinancialservices25-50','niftyfinancialservicesexbank_','niftyfmcg',
    'niftyhealthcare','niftyit','niftymedia',
    'niftymetal','niftypharma','nifty_privatebank',
    'niftypsubank','niftyrealty','niftyconsumerdurables',
    'niftyoilgas','nifty500Healthcare_','niftymidsmallfinancailservice_',
    'niftymidsmallhealthcare_','niftymidsmallitAndtelecom_', 'nifty500', 'niftymicrocap250_'
]

def download_sector_csv(index_name):
    # Standard URL pattern for Nifty Indices CSVs
    url = f"https://www.niftyindices.com/IndexConstituent/ind_{index_name}list.csv"
    
    # User-Agent is often required to avoid 403 Forbidden errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            df = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
            return df
        else:
            return None
    except Exception as e:
        return None

def fetch_data(sectors):
    all_dfs = []
    for sector in sectors:
        df = download_sector_csv(sector)
        if df is not None and not df.empty:
            df['Sector'] = sector
            all_dfs.append(df)
            
    if all_dfs:
        return pd.concat(all_dfs, ignore_index=True)
    return pd.DataFrame()

if __name__ == "__main__":
    df = fetch_data(sectors)