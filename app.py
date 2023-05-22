import streamlit as st
import pandas as pd
import yfinance as yf

# List of stock tickers
tickers = ['RES', 'SCHW', 'SLB', 'SPR', 'STRL', 'SWBI', 'THO', 'TPR', 'NOV', 'OBTC', 'OII', 'OIS', 'ONEW', 'ORN', 'POWL', 'PVH', 'FLR', 'FOSL', 'GBX', 'HOOD', 'JWN', 'KBAL', 'MOV', 'MRMD', 'MTRX', 'BKE', 'CLB', 'CNK', 'CRWD', 'DECK', 'DNOW', 'DRQ', 'FLR']

# Function to generate future recommendations based on trailing 7-day performance
def generate_recommendations():
    recommendations = []

    # Iterate through each stock ticker
    for stock in tickers:
        # Download historical data for the stock
        data = yf.download(stock, period='7d', interval='1d', progress=False)
        
        if data.empty:
            continue
        
        # Calculate the purchase price as the closing price of the last trading day
        purchase_price = data['Close'][-1]

        # Calculate the sell price as the mean of the high and low prices of the last trading day
        sell_price = (data['High'][-1] + data['Low'][-1]) / 2

        # Determine the recommendation based on the purchase and sell prices
        if sell_price > purchase_price:
            recommendation = 'Buy'
        else:
            recommendation = 'Sell'

        recommendations.append({'Stock': stock, 'Recommendation': recommendation, 'Purchase Price': purchase_price, 'Sell Price': sell_price})

    return recommendations

# Generate recommendations
recommendations = generate_recommendations()

# Display recommendations in Streamlit app
st.set_page_config(layout="wide")
st.header("Bagwells Big Bag - Stock Recommendations for the Next Trading Day")

if recommendations:
    df = pd.DataFrame(recommendations)
    st.dataframe(df.style.format({'Purchase Price': '{:.2f}', 'Sell Price': '{:.2f}'}), height=800)
else:
    st.write("No recommendations available")
