import pandas as pd
import streamlit as st
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime, timedelta

# Alpha Vantage API key
api_key = 'YOUR_API_KEY'

# List of stock tickers
tickers = ['RES', 'SCHW', 'SLB', 'SPR', 'STRL', 'SWBI', 'THO', 'TPR', 'NOV', 'OBTC', 'OII', 'OIS', 'ONEW', 'ORN',
           'POWL', 'PVH', 'FLR', 'FOSL', 'GBX', 'HOOD', 'JWN', 'KBAL', 'MOV', 'MRMD', 'MTRX', 'BKE', 'CLB', 'CNK',
           'CRWD', 'DECK', 'DNOW', 'DRQ', 'FLR']

# Create an empty DataFrame to hold all the recommendation data
recommendations = pd.DataFrame(columns=['Stock', 'Recommendation', 'Buy Price', 'Sell Price'])

# Function to generate recommendations
def generate_recommendations():
    # Loop through each stock ticker
    for stock in tickers:
        # Get historical data from Alpha Vantage
        ts = TimeSeries(key=api_key, output_format='pandas')
        data, _ = ts.get_daily(symbol=stock, outputsize='full')
        data['date'] = pd.to_datetime(data.index)
        data.sort_values('date', ascending=False, inplace=True)

        # Calculate the average closing price over the past 252 trading days
        data['Avg Close'] = data['4. close'].rolling(window=252).mean()

        # Get the last closing price
        current_price = data['4. close'].iloc[0]

        # Get the average closing price for the next trading week
        avg_price_next_week = data['Avg Close'].iloc[6]

        # Determine the recommendation based on the price comparison
        if current_price < avg_price_next_week:
            recommendation = 'Buy'
            buy_price = current_price
            sell_price = avg_price_next_week
        else:
            recommendation = 'Sell'
            buy_price = avg_price_next_week
            sell_price = current_price

        # Append the recommendation data to the DataFrame
        recommendations.loc[recommendations['Stock'] == stock] = [stock, recommendation, buy_price, sell_price]

    # Sort the recommendations by stock ticker
    recommendations.sort_values('Stock', inplace=True)
    recommendations.reset_index(drop=True, inplace=True)

# Generate initial recommendations
generate_recommendations()

# Streamlit app
st.title("Bagwell's Big Bag - Stock Recommendations")

# Display the recommendations
st.table(recommendations)

# Refresh the recommendations every day
if datetime.now().strftime("%H:%M:%S") == "00:00:00":
    generate_recommendations()
