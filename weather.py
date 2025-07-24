# weather.py
import streamlit as st
import requests

st.set_page_config(page_title="🌦️ Real-time Multi-City Weather Dashboard", layout="centered")

st.title("🌦️ Real-time Multi-City Weather Dashboard")
cities_input = st.text_input("Enter city names separated by comma (e.g., Hyderabad, Mumbai, Chennai):")

if cities_input:
    cities = [city.strip() for city in cities_input.split(",") if city.strip()]
    valid_data = []

    for city in cities:
        api_url = f"http://127.0.0.1:5000/weather?city={city}"  # Assumes Flask is running locally
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()

                # Validate data
                if all(key in data and data[key] is not None for key in ['temperature (°C)', 'humidity (%)', 'wind speed (km/h)', 'condition']):
                    valid_data.append(data)
                else:
                    st.warning(f"⚠️ Incomplete data for {city}: {data}")
            else:
                error = response.json().get("error", "Unknown error")
                st.warning(f"❌ Failed to get data for {city}: {error}")
        except Exception as e:
            st.error(f"❌ Exception while fetching data for {city}: {e}")

    if valid_data:
        st.subheader("📊 Weather Report")
        for weather in valid_data:
            st.markdown(f"### 🌆 Weather for {weather['city']} on {weather['date']}")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🌡️ Temperature (°C)", f"{weather['temperature (°C)']} °C")
            with col2:
                st.metric("💧 Humidity (%)", f"{weather['humidity (%)']} %")
            with col3:
                st.metric("🌬️ Wind Speed (km/h)", f"{weather['wind speed (km/h)']} km/h")

            st.markdown(f"**☁️ Condition:** {weather['condition']}")
            st.divider()
    else:
        st.warning("⚠️ No valid weather data available to display.")
