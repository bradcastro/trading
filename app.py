import streamlit as st
import pandas as pd
import yfinance as yf

# List of renewable energy stocks
renewable_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']  # Add more renewable energy stocks here

st.title('Renewable Energy Stock Recommendations')

# Download historical data for renewable energy stocks
data = yf.download(renewable_stocks, start='2020-01-01', end='2023-12-31')

# Create an empty list to hold the recommendation data
recommendations = []

# Initialize session state for stock preferences
if 'stock_preferences' not in st.session_state:
    st.session_state.stock_preferences = {}
    for stock in renewable_stocks:
        st.session_state.stock_preferences[stock] = False

# Perform analysis and generate recommendations
for stock in renewable_stocks:
    # Perform your analysis here to generate stock recommendations
    # You can use various metrics and analysis techniques to evaluate the stocks
    
    # For demonstration purposes, let's assume a simple random recommendation
    recommendation = 'Buy' if st.session_state.stock_preferences[stock] else 'Sell'
    
    recommendations.append({'Stock': stock, 'Recommendation': recommendation})

# Convert the recommendations list to a DataFrame
recommendations_df = pd.DataFrame(recommendations)

# Display the stock recommendations
st.subheader('Stock Recommendations')
st.dataframe(recommendations_df)

# Allow users to customize their preferences
st.subheader('Customize Preferences')

for stock in renewable_stocks:
    st.sidebar.markdown(f"**{stock}**")
    st.sidebar.checkbox('Buy', key=stock, value=st.session_state.stock_preferences[stock], on_change=lambda value, stock=stock: st.session_state.stock_preferences.update({stock: value}))
