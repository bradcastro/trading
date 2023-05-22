import streamlit as st
import yfinance as yf
import pandas as pd

# Function to download historical stock data
def download_historical_data(tickers, start_date, end_date):
    all_data = pd.DataFrame()

    for ticker in tickers:
        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            data['Ticker'] = ticker
            all_data = all_data.append(data)
        except Exception as e:
            st.write(f"Failed to download data for {ticker}: {e}")

    return all_data

# Define the list of ticker symbols
tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'JPM', 'BABA', 'WMT', 'V', 'JNJ', 'PG', 'MA', 'UNH', 'DIS', 'NFLX', 'ADBE', 'CRM', 'XOM', 'CVS',
    'ABT', 'NKE', 'BAC', 'IBM', 'CMCSA', 'KO', 'PEP', 'PFE', 'INTC', 'TM', 'GE', 'HPQ', 'COST', 'ORCL', 'UPS', 'VZ', 'AXP', 'FDX', 'GILD', 'CAT', 'AMGN', 'BA',
    'MCD', 'MRK', 'MO', 'TMUS', 'LMT', 'MMM', 'MS', 'T', 'NVS', 'QCOM', 'SBUX', 'SAP', 'TXN', 'WFC', 'WBA', 'CSCO', 'ABBV', 'AVGO', 'MDT', 'PM', 'CHL', 'SNAP',
    'NEE', 'AMT', 'SNE', 'C', 'GSK', 'DHR', 'AMAT', 'BLK', 'SBAC', 'SPGI', 'ISRG', 'CSX', 'TMO', 'BMY', 'NOW', 'BKNG', 'LRCX', 'ZTS', 'CTSH', 'BHP', 'COF', 'USB',
    'CI', 'LVS', 'ADP', 'RTX', 'ANTM', 'EQIX', 'SYK', 'VRTX', 'TMX', 'DE', 'CTAS', 'BIIB', 'CB', 'ADSK', 'AME', 'RIO', 'SO', 'TEL', 'MU', 'HON', 'LOW', 'SOON',
    'MDLZ', 'APD', 'TWTR', 'TGT', 'TJX', 'BDX', 'OXY', 'CCL', 'EBAY', 'GD', 'YUM', 'ICE', 'ATVI', 'D', 'AON', 'PAYX', 'TRV', 'SYY', 'ITW', 'PPG', 'ZBH', 'TDG',
    'DG', 'SWKS', 'FIS', 'PCAR', 'SWK', 'SYF', 'WELL', 'FOX', 'CERN', 'INFO', 'DLTR', 'XEL', 'BAX', 'ROST', 'FCX', 'EXC', 'HLT', 'VLO', 'OMC', 'ADBE', 'EBAY', 'CSCO',
    'GOOG', 'NFLX', 'SBUX', 'TSLA', 'VRSN', 'TXN', 'GOOGL', 'CME', 'CTXS', 'CHKP', 'CTSH', 'QCOM', 'AAPL', 'COST', 'NVDA', 'NLOK', 'XRX', 'YHOO', 'CTXS', 'KHC',
    'CSRA', 'HPE', 'HPQ', 'ABBV', 'PYPL', 'MNK', 'FOX', 'FOXA', 'LMT', 'UTX', 'UT'
    # Add more ticker symbols here as needed
]

# Define the date range for data
start_date = '2020-01-01'
end_date = '2023-12-31'

# Download the historical stock data
all_data = download_historical_data(tickers, start_date, end_date)

# Save the data to a CSV file
all_data.to_csv('historical_stock_data.csv', index=False)

# Display the data
st.dataframe(all_data)
