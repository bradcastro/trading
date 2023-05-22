import pandas as pd
import streamlit as st
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime, timedelta

# List of stock tickers
tickers = ['RES', 'SCHW', 'SLB', 'SPR', 'STRL', 'SWBI', 'THO', 'TPR', 'NOV', 'OBTC', 'OII', 'OIS', 'ONEW', 'ORN',
           'POWL', 'PVH', 'FLR', 'FOSL', 'GBX', 'HOOD', 'JWN', 'KBAL', 'MOV', 'MRMD', 'MTRX', 'BKE', 'CLB', 'CNK',
           'CRWD', 'DECK', 'DNOW', 'DRQ', 'FLR']

# Create an empty DataFrame to hold all the recommendation data
recommendations = pd.DataFrame(columns=['Stock', 'Recommendation', 'Buy Price', 'Sell Price'])

# Function to generate recommendations
def generate_recommendations():
    # Create a new DataFrame for recommendations
    new_recommendations = pd.DataFrame(columns=['Stock', 'Recommendation', 'Buy Price', 'Sell Price'])

    # Initialize Alpha Vantage API
    ts = TimeSeries(key='PUT3TG5YWCXSZU6G', output_format='pandas')

    # Loop through each stock ticker
    for stock in tickers:
        # Get historical data from Alpha Vantage
        try:
            data, _ = ts.get_daily_adjusted(stock, outputsize='full')

            if data.empty:
                continue

            data['Avg Close'] = data['close'].rolling(window=252).mean()

            # Get the last closing price
            current_price = data['close'].iloc[-1]

            # Get the average closing price for the next trading week
            avg_price_next_week = data['Avg Close'].iloc[-6]

            # Determine the recommendation based on the price comparison
            if current_price < avg_price_next_week:
                recommendation = 'Buy'
                buy_price = current_price
                sell_price = avg_price_next_week
            else:
                recommendation = 'Sell'
                buy_price = avg_price_next_week
                sell_price = current_price

            # Append the recommendation data to the new DataFrame
            new_recommendations = new_recommendations.append({'Stock': stock, 'Recommendation': recommendation,
                                                              'Buy Price': buy_price, 'Sell Price': sell_price},
                                                             ignore_index=True)
        except Exception as e:
            print(f"Error retrieving data for {stock}: {str(e)}")

    # Sort the recommendations by stock ticker
    new_recommendations['Stock'] = new_recommendations['Stock'].astype(str)  # Convert to string type
    new_recommendations.sort_values('Stock', inplace=True)
    new_recommendations.reset_index(drop=True, inplace=True)

    return new_recommendations

# Generate initial recommendations
recommendations = generate_recommendations()

# Streamlit app
st.title("Bagwell's Big Bag - Stock Recommendations")

# Display the recommendations
st.table(recommendations)
