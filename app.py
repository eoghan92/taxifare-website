import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# Set up the title and description
st.title("TaxiFareModel Frontend")

st.markdown('''
Taxi Fare Prediction!!!

Please enter your trip details to get an estimation.
''')

# Input fields for user to enter ride details
pickup_datetime = st.text_input("Pickup datetime (YYYY-MM-DD HH:MM:SS)", "2014-07-06 19:18:00")
pickup_longitude = st.number_input("Pickup longitude", value=-73.950655)
pickup_latitude = st.number_input("Pickup latitude", value=40.783282)
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.984365)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.769802)
passenger_count = st.number_input("Passenger count", min_value=1, max_value=6, value=1)

# URL of the prediction API
url = 'https://taxifare.lewagon.ai/'  # Use your own API URL here

if st.button('Get Fare Prediction'):
    # Prepare the parameters for the API request
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    try:
        # Make the API request
        response = requests.get(url, params=params)

        # Check the response status and parse the result
        if response.status_code == 200:
            fare = response.json().get('fare')
            st.write(f"Estimated fare: ${fare:.2f}")
        else:
            st.write("Error: Unable to get a response from the API.")
            st.write(f"Response status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        st.write("An error occurred while trying to fetch the prediction.")
        st.write(str(e))

# Display the map for pickup location
st.subheader("Pickup Location")
pickup_data = pd.DataFrame({'lat': [pickup_latitude], 'lon': [pickup_longitude]})
st.map(pickup_data)

# Display the map for dropoff location
st.subheader("Dropoff Location")
dropoff_data = pd.DataFrame({'lat': [dropoff_latitude], 'lon': [dropoff_longitude]})
st.map(dropoff_data)
