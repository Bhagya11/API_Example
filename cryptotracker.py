# crypto_tracker.py
import requests
import streamlit as st

# Set your CoinMarketCap API key
API_KEY = "ca4a4fe1-b3df-4aa9-847d-110a1bb20ca9"
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY
}

params = {
    "start": "1",
    "limit": "10",
    "convert": "USD"
}

# Streamlit UI
st.set_page_config(page_title="Crypto Tracker", layout="wide")
st.title("💰 Real-Time Cryptocurrency Tracker")

# Fetch data
response = requests.get(url, headers=headers, params=params)
data = response.json()

if response.status_code == 200:
    for coin in data['data']:
        name = coin['name']
        price = coin['quote']['USD']['price']
        st.metric(label=name, value=f"${price:,.2f}")
else:
    st.error("Failed to fetch data from CoinMarketCap API.")
