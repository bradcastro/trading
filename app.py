import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def generate_recommendations():
    recommendations = []

    stocks = ['RES', 'SCHW', 'SLB', 'SPR', 'STRL', 'SWBI', 'THO', 'TPR', 'NOV', 'OBTC', 'OII', 'OIS', 'ONEW', 'ORN',
              'POWL', 'PVH', 'FLR', 'FOSL', 'GBX', 'HOOD', 'JWN', 'KBAL', 'MOV', 'MRMD', 'MTRX', 'BKE', 'CLB', 'CNK',
              'CRWD', 'DECK', 'DNOW', 'DRQ', 'FLR']

    for stock in stocks:
        data = yf.download(stock, start=(datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d"),
                           end=datetime.now().strftime("%Y-%m-%d"), progress=False)

        if data.empty:
            continue

        # Calculate buy and sell prices based on the previous day's close price
        buy_price = data['Close'].iloc[-2]
        sell_price = data['Close'].iloc[-1]

        # Perform your recommendation logic here
        recommendation = 'Buy' if sell_price > buy_price else 'Sell'

        recommendations.append({'Stock': stock, 'Buy Price': buy_price,
                                'Sell Price': sell_price, 'Recommendation': recommendation})

    recommendations_df = pd.DataFrame(recommendations)
    recommendations_df['Stock'] = recommendations_df['Stock'].apply(lambda x: f"[{x}](https://finance.yahoo.com/quote/{x})")

    return recommendations_df


# Main app code
st.title("Bagwells Big Bag Recommendations")
recommendations = generate_recommendations()

if recommendations.empty:
    st.info("No recommendations available.")
else:
    recommendations['Stock'] = recommendations['Stock'].apply(lambda x: f"[{x}](https://finance.yahoo.com/quote/{x})")
    st.table(recommendations)
