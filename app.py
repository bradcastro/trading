import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def generate_recommendations():
    recommendations = []

    stocks = ['RES', 'SCHW', 'SLB', 'SPR', 'STRL', 'SWBI', 'THO', 'TPR', 'NOV', 'OBTC', 'OII', 'OIS', 'ONEW', 'ORN',
              'POWL', 'PVH', 'FLR', 'FOSL', 'GBX', 'HOOD', 'JWN', 'KBAL', 'MOV', 'MRMD', 'MTRX', 'BKE', 'CLB', 'CNK',
              'CRWD', 'DECK', 'DNOW', 'DRQ', 'FLR']

    for stock in stocks:
        try:
            # Perform your recommendation logic here
            recommendation = 'Buy'  # Placeholder for recommendation

            recommendations.append({'Stock': stock, 'Recommendation': recommendation})
        except Exception as e:
            print(f"Error occurred for stock {stock}: {str(e)}")

    recommendations_df = pd.DataFrame(recommendations)
    recommendations_df['Stock'] = recommendations_df['Stock'].apply(
        lambda x: f"[{x}](https://finance.yahoo.com/quote/{x})")

    return recommendations_df


# Main app code
st.title("Bagwells Big Bag")
recommendations = generate_recommendations()

if recommendations.empty:
    st.info("No recommendations available.")
else:
    recommendations = recommendations.set_index('Stock')
    st.table(recommendations)
