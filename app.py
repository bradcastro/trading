import pandas as pd
import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta

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
        # Get historical data from Yahoo Finance
        try:
            data = yf.download(stock, start=(datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d"),
                               end=datetime.now().strftime("%Y-%m-%d"))
            
            if data.empty:
                continue

            data['Avg Close'] = data['Close'].rolling(window=252).mean()

            # Get the last closing price
            current_price = data['Close'].iloc[-1]

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

            # Append the recommendation data to the DataFrame
            recommendations = recommendations.append({'Stock': stock, 'Recommendation': recommendation,
                                                      'Buy Price': buy_price, 'Sell Price': sell_price},
                                                     ignore_index=True)
        except Exception as e:
            print(f"Error retrieving data for {stock}: {str(e)}")

    # Sort the recommendations by stock ticker
    recommendations['Stock'] = recommendations['Stock'].astype(str)  # Convert to string type
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
