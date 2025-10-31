import streamlit as st
import pickle
import pandas as pd

model =  pickle.load(open('carpriceprd.pkl', 'rb'))

df = pd.read_csv('car cleaned_csv') 
companies = sorted(df['company'].unique())
car_names = sorted(df['name'].unique())
fuel_types = sorted(df['fuel_type'].unique())

st.title("🚗 Car Price Predictor")

company = st.selectbox('Company', companies)
car_name = st.selectbox('Car Name', car_names)
year = st.number_input('Year', 2000, 2025, 2018)
kms_driven = st.number_input('Kms Driven', 0, 300000, 50000)
fuel_type = st.selectbox('Fuel Type', fuel_types)

data = pd.DataFrame({
    'name': [car_name],
    'company': [company],
    'year': [year],
    'kms_driven': [kms_driven],
    'fuel_type': [fuel_type]
})

if st.button('Predict Price'):
    prediction = model.predict(data)
    st.success(f"Predicted Price: ₹{prediction[0]:,.2f}")
