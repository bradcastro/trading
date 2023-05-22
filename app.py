import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# List of stock tickers
tickers = ['RES', 'SCHW', 'SLB', 'SPR', 'STRL', 'SWBI', 'THO', 'TPR', 'NOV', 'OBTC', 'OII', 'OIS', 'ONEW', 'ORN', 'POWL', 'PVH', 'FLR', 'FOSL', 'GBX', 'HOOD', 'JWN', 'KBAL', 'MOV', 'MRMD', 'MTRX', 'BKE', 'CLB', 'CNK', 'CRWD', 'DECK', 'DNOW', 'DRQ', 'FLR']

# Function to generate future recommendations
def generate_recommendations():
    recommendations = []

    # Iterate through each stock ticker
    for stock in tickers:
        try:
            # Download historical data for the current stock
            data = yf.download(stock, start=datetime.now() - timedelta(days=365), end=datetime.now(), progress=False)

            # Train your prediction model using the historical data

            # Make future price predictions for the next 24 hours

            # Determine buy and sell thresholds based on the predicted prices

            # Get the latest price for the stock
            latest_price = data['Close'].iloc[-1]

            # Generate buy or sell recommendation based on the thresholds
            recommendation = 'Buy' if latest_price < buy_threshold else 'Sell'

            # Append the recommendation to the list
            recommendations.append({'Stock': stock, 'Recommendation': recommendation})

        except Exception as e:
            print(f"Failed to generate recommendation for {stock}: {e}")

    return recommendations

# Generate recommendations
recommendations = generate_recommendations()

# Display recommendations in Streamlit app
st.header("Bagwells Big Bag - Stock Recommendations for the Next 24 Hours")

if recommendations:
    df = pd.DataFrame(recommendations)
    st.dataframe(df)
else:
    st.write("No recommendations available")

