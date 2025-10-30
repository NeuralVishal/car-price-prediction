import streamlit as st
import pickle
import pandas as pd

# Load model
model =  pickle.load(open('carpriceprd.pkl', 'rb'))


# Load dataset for dropdown options
df = pd.read_csv('car cleaned_csv')  # your dataset file
companies = sorted(df['company'].unique())
car_names = sorted(df['name'].unique())
fuel_types = sorted(df['fuel_type'].unique())

st.title("🚗 Car Price Predictor")

# Dropdowns populated from dataset
company = st.selectbox('Company', companies)
car_name = st.selectbox('Car Name', car_names)
year = st.number_input('Year', 2000, 2025, 2018)
kms_driven = st.number_input('Kms Driven', 0, 300000, 50000)
fuel_type = st.selectbox('Fuel Type', fuel_types)

# Create DataFrame for prediction
data = pd.DataFrame({
    'name': [car_name],
    'company': [company],
    'year': [year],
    'kms_driven': [kms_driven],
    'fuel_type': [fuel_type]
})

# Predict button
if st.button('Predict Price'):
    prediction = model.predict(data)
    st.success(f"Predicted Price: ₹{prediction[0]:,.2f}")
