import yfinance as yf
import pandas as pd

# List of ticker symbols for which to download data
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'JPM', 'BABA', 'WMT, 'V', 'JNJ', 'PG', 'MA', 'UNH', 'DIS', 'NFLX', 'ADBE', 'CRM', 'XOM', 'CVS',
    'ABT', 'NKE', 'BAC', 'IBM', 'CMCSA', 'KO', 'PEP', 'PFE', 'INTC', 'TM', 'GE',
    'HPQ', 'COST', 'ORCL', 'UPS', 'VZ', 'AXP', 'FDX', 'GILD', 'CAT', 'AMGN', 'BA',
    'MCD', 'MRK', 'MO', 'TMUS', 'LMT', 'MMM', 'MS', 'T', 'NVS', 'QCOM', 'SBUX',
    'SAP', 'TXN', 'WFC', 'WBA', 'CSCO', 'ABBV', 'AVGO', 'MDT', 'PM', 'CHL', 'SNAP',
    'NEE', 'AMT', 'SNE', 'C', 'GSK', 'DHR', 'AMAT', 'BLK', 'SBAC', 'SPGI', 'ISRG',
    'CSX', 'TMO', 'BMY', 'NOW', 'BKNG', 'LRCX', 'ZTS', 'CTSH', 'BHP', 'COF', 'USB',
    'CI', 'LVS', 'ADP', 'RTX', 'ANTM', 'EQIX', 'SYK', 'VRTX', 'TMX', 'DE', 'CTAS',
    'BIIB', 'CB', 'ADSK', 'AME', 'RIO', 'SO', 'TEL', 'MU', 'HON', 'LOW', 'SOON',
    'MDLZ', 'APD', 'TWTR', 'TGT', 'TJX', 'BDX', 'OXY', 'CCL', 'EBAY', 'GD', 'YUM',
    'ICE', 'ATVI', 'D', 'AON', 'PAYX', 'TRV', 'SYY', 'ITW', 'PPG', 'ZBH', 'TDG',
    'DG', 'SWKS', 'FIS', 'PCAR', 'SWK', 'SYF', 'WELL', 'FOX', 'CERN', 'INFO', 'DLTR',
    'XEL', 'BAX', 'ROST', 'FCX', 'EXC', 'HLT', 'VLO', 'OMC', 'ADBE', 'EBAY', 'CSCO',
    'GOOG', 'NFLX', 'SBUX', 'TSLA', 'VRSN', 'TXN', 'GOOGL', 'CME', 'CTXS', 'CHKP',
    'CTSH', 'QCOM', 'AAPL', 'COST', 'NVDA', 'NLOK', 'XRX', 'YHOO', 'CTXS', 'KHC',
    'CSRA', 'HPE', 'HPQ', 'ABBV', 'PYPL', 'MNK', 'FOX', 'FOXA', 'LMT', 'UTX',    'UTX', 'PNC', 'KO', 'DIS', 'WMT', 'GS', 'TGT', 'JPM', 'MA', 'AFL', 'MET', 'SYF',
    'AXP', 'V', 'DFS', 'C', 'COF', 'BBT', 'USB', 'SCHW', 'TROW', 'AMP', 'CBOE', 'STT',
    'NDAQ', 'ETFC', 'ZION', 'FITB', 'CFG', 'FRC', 'HIG', 'BK', 'AON', 'MMC', 'CB',
    'MTB', 'CI', 'HUM', 'ANTM', 'UNH', 'WBA', 'CVS', 'RAD', 'MRK', 'LLY', 'PFE', 'ABBV',
    'GILD', 'JNJ', 'ABT', 'AMGN', 'BIIB', 'CELG', 'VRTX', 'MDT', 'SYK', 'BSX', 'ZBH',
    'COO', 'ISRG', 'EW', 'REGN', 'BMY', 'AET', 'HCA', 'DHR', 'ALXN', 'ILMN', 'RHHBY',
    'GSK', 'NVS', 'AZN', 'SNY', 'PCLN', 'EXPE', 'BKNG', 'MNST', 'KO', 'PEP', 'CCEP',
    'DPS', 'MDLZ', 'STZ', 'BF-B', 'TAP', 'PM', 'MO', 'PM', 'RAI', 'SBUX', 'MCD', 'DPZ',
    'YUM', 'WEN', 'CMG', 'DNKN', 'SBUX', 'NKE', 'UA', 'ADDYY', 'LULU', 'RL', 'VFC',
    'GPS', 'ANF', 'LB', 'FL', 'KSS', 'TJX', 'ROST', 'BURL', 'AEO', 'URBN', 'HBI', 'JWN',
    'TIF', 'DDS', 'PVH', 'GCO', 'SIG', 'CHS', 'EXPE', 'BKNG', 'PCLN', 'CTRP', 'TRIP',
    'TRVG', 'CAR', 'H', 'MAR', 'HLT', 'WYN', 'HOT', 'RLH', 'WH', 'CHH', 'STAY', 'ABNB',
    'SIX', 'FUN', 'SEAS', 'DIS', 'NFLX', 'AMZN', 'AAPL', 'GOOGL', 'FB', 'GOOG', 'TWTR',
    'SNAP', 'PINS', 'SPOT', 'YELP', 'P', 'Z', 'GRUB', 'YUM', 'DPZ', 'MCD', 'SBUX', 'CMG',
    'WEN', 'SHAK', 'DNKN', 'BKW', 'TACO', 'WMT', 'COST', 'TGT', 'KR', 'SYY', 'CAG',
    'ADM', 'GIS', 'CPB', 'KHC', 'MDLZ', 'TSN', 'HRL', 'MKC', 'SFM', 'NWL', 'CLX', 'PG',
    'CL', 'UL', 'EL', 'COTY', 'COT', 'REV', 'COTY', 'NVO',    'NVO', 'UNH', 'TMO', 'MDT', 'BMY', 'ABBV', 'ABT', 'SNY', 'AMGN', 'LLY', 'GSK',
    'PFE', 'JNJ', 'MRK', 'AZN', 'NVS', 'CELG', 'BIIB', 'GILD', 'VRTX', 'ALXN', 'REGN',
    'VRTX', 'CBG', 'CCI', 'DLR', 'EQIX', 'HCP', 'IRM', 'MAC', 'PLD', 'PSA', 'SPG',
    'VTR', 'BXP', 'SLG', 'ARE', 'EQR', 'AVB', 'UDR', 'MAA', 'ESS', 'AIV', 'SUI',
    'CLX', 'CL', 'KMB', 'PG', 'EL', 'CHD', 'NWL', 'CHRW', 'FDX', 'UPS', 'EXPD',
    'LSTR', 'ODFL', 'JBHT', 'R', 'XPO', 'KNX', 'CNI', 'CSX', 'NSC', 'UNP', 'WAB',
    'VFC', 'PVH', 'RL', 'HBI', 'NKE', 'UAA', 'UA', 'LULU', 'COLM', 'GCO', 'FL',
    'DSW', 'BURL', 'ANF', 'URBN', 'AEO', 'EXPR', 'ASNA', 'GPS', 'LB', 'TJX', 'ROST',
    'BURL', 'HAIN', 'SAFM', 'TSN', 'HRL', 'FLO', 'MKC', 'CAG', 'APRN', 'ADM', 'CPB',
    'GIS', 'COST', 'WMT', 'KR', 'MCK', 'CAH', 'CVS', 'WBA', 'ABC', 'ESRX', 'HSIC',
    'OMI', 'PDCO', 'ABC', 'BRK-A', 'BRK-B', 'WFC', 'JPM', 'BAC', 'C', 'GS', 'MS',
    'USB', 'PNC', 'COF', 'AXP', 'MET', 'AIG', 'TRV', 'ALL', 'CB', 'HIG', 'PRU',
    'AFL', 'LNC', 'TMK', 'MMC', 'AON', 'AJG', 'CTAS', 'CDW', 'FAST', 'AVY', 'PKG',
    'RHI', 'MCO', 'SPGI', 'TSS', 'VRSK', 'MA', 'V', 'AXP', 'PYPL', 'DFS', 'PAYX',
    'FLT', 'GPN', 'ADS', 'FIS', 'JKHY', 'NDAQ', 'ICE', 'CBOE', 'MSCI', 'SCHW', 'BK',
    'STT', 'BLK', 'IVZ', 'AON', 'MS', 'SIVB', 'KEY', 'CFG', 'FITB', 'CMA', 'RF',
    'PNC', 'HBAN', 'STI', 'MTB', 'FRC', 'PBCT', 'WAL', 'BEN', 'AMP', 'WFC', 'USB',
    'C', 'COF', 'MS', 'AXP', 'DFS',    'DFS', 'SYF', 'MET', 'AIG', 'PRU', 'AFL', 'HIG', 'LNC', 'CINF', 'UNM', 'GL', 'PGR',
    'AJG', 'ALL', 'TRV', 'WRB', 'MCY', 'TMK', 'CNO', 'ORI', 'RE', 'HII', 'VMI', 'CE',
    'IFF', 'IP', 'ALB', 'PPG', 'SHW', 'NUE', 'X', 'CLF', 'RS', 'AKS', 'STLD', 'WOR',
    'CRS', 'NUE', 'AA', 'PKX', 'MT', 'STLD', 'AKS', 'CLF', 'X', 'RS', 'CENX', 'PKX',
    'CE', 'VAL', 'HUN', 'NWL', 'KMB', 'CL', 'PG', 'CHD', 'CLX', 'EL', 'CHRW', 'UPS',
    'FDX', 'XPO', 'EXPD', 'JBHT', 'KNX', 'LSTR', 'ODFL', 'R', 'SAIA', 'UAL', 'AAL',
    'DAL', 'ALK', 'JBLU', 'MGM', 'LVS', 'WYNN', 'MGP', 'CZR', 'PENN', 'BYD', 'MLCO',
    'DKNG', 'PENN', 'WYNN', 'CZR', 'MGM', 'GPN', 'TSS', 'VNTV', 'FISV', 'JKHY', 'FIS',
    'FLT', 'MA', 'PYPL', 'V', 'AXP', 'DFS', 'WEX', 'COOP', 'PYPL', 'COOP', 'COF', 'ALLY',
    'SYF', 'ETFC', 'PNC', 'MTB', 'CFG', 'USB', 'STT', 'KEY', 'RF', 'BK', 'HBAN', 'FITB',
    'ZION', 'BOKF', 'CMA', 'BPOP', 'WAL', 'C', 'JPM', 'BAC', 'WFC', 'GS', 'MS', 'SPGI',
    'MMC', 'CB', 'AON', 'AJG', 'ALL', 'TRV', 'CINF', 'MET', 'AIG', 'PRU', 'AFL', 'HIG',
    'LNC', 'TMK', 'RE', 'CNO', 'UNM', 'GL', 'PGR', 'ORI', 'MCY', 'WU', 'PRA', 'MCO',
    'TSS', 'ACN', 'ATVI', 'GOOGL', 'ADBE', 'AMZN', 'AAPL', 'CRM', 'INTU', 'EA', 'FB',
    'GOOG', 'IBM', 'MSFT', 'NFLX', 'NVDA', 'ORCL', 'SAP', 'SNAP', 'TWTR', 'T', 'VZ',
    'CMCSA', 'DIS', 'ATVI', 'CHTR', 'CSCO', 'AMT', 'AVGO', 'TMUS', 'QCOM', 'TMUS', 'CCI',
    'COST', 'CVS', 'HD', 'KR', 'LOW', 'TGT', 'WMT', 'ACN



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
