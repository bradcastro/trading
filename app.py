import streamlit as st
import pandas as pd
import yfinance as yf

# List of stocks
stocks = ['RES', 'SCHW', 'SLB', 'SPR', 'STRL', 'SWBI', 'THO', 'TPR', 'NOV', 'OBTC', 'OII', 'OIS', 'ONEW', 'ORN', 'POWL', 'PVH', 'FLR', 'FOSL', 'GBX', 'HOOD', 'JWN', 'KBAL', 'MOV', 'MRMD', 'MTRX', 'BKE', 'CLB', 'CNK', 'CRWD', 'DECK', 'DNOW', 'DRQ', 'FLR']

st.title('Stock Recommendations')

# Download historical data for the stocks
data = yf.download(stocks, start='2020-01-01', end='2023-12-31')

# Create an empty list to hold the recommendation data
recommendations = []

# Perform analysis and generate recommendations
for stock in stocks:
    # Perform your analysis here to generate stock recommendations
    # You can use various metrics and analysis techniques to evaluate the stocks
    
    # For demonstration purposes, let's assume a simple random recommendation
    buy_price = data['Close'][stock].iloc[-1]  # Get the latest closing price as the buy price
    sell_price = buy_price * 1.1  # Set the sell price as 10% higher than the buy price
    
    recommendation = 'Buy'
    
    recommendations.append({'Stock': stock, 'Recommendation': recommendation, 'Buy Price': buy_price, 'Sell Price': sell_price})

# Convert the recommendations list to a DataFrame
recommendations_df = pd.DataFrame(recommendations)

# Display the stock recommendations
st.subheader('Stock Recommendations')
st.dataframe(recommendations_df)
