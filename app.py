import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# List of stock tickers
tickers = ['RES', 'SCHW', 'SLB', 'SPR', 'STRL', 'SWBI', 'THO', 'TPR', 'NOV', 'OBTC', 'OII', 'OIS', 'ONEW', 'ORN', 'POWL', 'PVH', 'FLR', 'FOSL', 'GBX', 'HOOD', 'JWN', 'KBAL', 'MOV', 'MRMD', 'MTRX', 'BKE', 'CLB', 'CNK', 'CRWD', 'DECK', 'DNOW', 'DRQ', 'FLR']

# Function to generate future recommendations for the next week
def generate_recommendations():
    recommendations = []

    # Get the current date
    current_date = datetime.now()

    # Calculate the end date as one week from the current date
    end_date = current_date + timedelta(days=7)

    # Iterate through each stock ticker
    for stock in tickers:
        try:
            # Download historical data for the stock
            data = yf.download(stock, start=current_date, end=end_date, progress=False)
            
            if data.empty:
                continue
            
            # Calculate the purchase price as the closing price of the current day
            purchase_price = data['Close'][current_date.strftime('%Y-%m-%d')]

            # Calculate the sell price as the mean of the high and low prices of the current day
            sell_price = (data['High'][current_date.strftime('%Y-%m-%d')] + data['Low'][current_date.strftime('%Y-%m-%d')]) / 2

            # Determine the recommendation based on the purchase and sell prices
            if sell_price > purchase_price:
                recommendation = 'Buy'
            else:
                recommendation = 'Sell'

            recommendations.append({'Stock': stock, 'Recommendation': recommendation, 'Purchase Price': purchase_price, 'Sell Price': sell_price})
        except Exception as e:
            print(f"Failed to generate recommendation for {stock}: {e}")

    return recommendations

# Generate recommendations
recommendations = generate_recommendations()

# Display recommendations in Streamlit app
st.set_page_config(layout="wide")
st.header("Bagwells Big Bag - Stock Recommendations for the Next Week")

if recommendations:
    df = pd.DataFrame(recommendations)
    
    # Format the dataframe to include hyperlinks
    df['Stock'] = df['Stock'].apply(lambda x: f"[{x}](https://finance.yahoo.com/quote/{x})")
    
    # Display the dataframe
    st.dataframe(df.style.format({'Purchase Price': '{:.2f}', 'Sell Price': '{:.2f}'}), height=800)
else:
    st.write("No recommendations available")
