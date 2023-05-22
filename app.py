import yfinance as yf
import pandas as pd

# List of ticker symbols for which to download data
tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'JPM', 'BABA', 'WMT', 'V', 'JNJ', 'PG', 'MA', 'UNH', 'DIS', 'NFLX', 'ADBE', 'CRM', 'XOM', 'CVS',
    'ABT', 'NKE', 'BAC', 'IBM', 'CMCSA', 'KO', 'PEP', 'PFE', 'INTC', 'TM', 'GE',
    # Add more tickers here...
]

# Create an empty DataFrame to hold all the data
all_data = pd.DataFrame()

for ticker in tickers:
    try:
        # Download historical data for the current ticker symbol
        data = yf.download(ticker, start='2020-01-01', end='2023-12-31')

        # Add a column to identify the ticker symbol
        data['Ticker'] = ticker

        # Append the data to the master DataFrame
        all_data = all_data.append(data)
    except Exception as e:
        print(f"Failed to download data for {ticker}: {e}")

# Save the data to a CSV file
all_data.to_csv('historical_stock_data.csv')
