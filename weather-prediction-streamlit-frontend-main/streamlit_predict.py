import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from google.cloud import bigquery

# Constants
PROJECT_ID = 'balmy-apogee-404909'
DATASET_ID = 'weather_prediction'
TABLE_ID = 'weather_predictions'
MODEL_NAME = 'dnn_multitarget_20231206-002418'

# Initialize BigQuery client
client = bigquery.Client(project=PROJECT_ID)

def query_weather_predictions(model_name):
    query = f"""
        SELECT weather_date, temp_predict, precip_predict
        FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
        WHERE model_id_name = '{model_name}'
        ORDER BY weather_date
    """
    return client.query(query).to_dataframe()

# Query data
df = query_weather_predictions(MODEL_NAME)

# Streamlit app
st.title("Ljubljana Weather Prediction")

# Display latest prediction
latest_prediction = df.iloc[-1]
st.write(f"Latest prediction: {latest_prediction['weather_date'].strftime('%Y-%m-%d')}")
# print latest prediction temp_predict and precip_predict, 2 decimal places
st.write(f"Temperature: {latest_prediction['temp_predict']:.2f} C")
st.write(f"Precipitation: {latest_prediction['precip_predict']:.2f} mm")

# Plot for temperature
st.subheader("All Time Temperature Prediction")
plt.figure(figsize=(10, 4))
plt.plot(df['weather_date'], df['temp_predict'], label='Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (C)')
plt.legend()
st.pyplot(plt)

# Plot for precipitation
st.subheader("All Time Precipitation Prediction")
plt.figure(figsize=(10, 4))
plt.plot(df['weather_date'], df['precip_predict'], label='Precipitation')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.legend()
st.pyplot(plt)
