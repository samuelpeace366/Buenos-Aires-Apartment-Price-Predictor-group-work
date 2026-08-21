import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

# Title
st.title("Buenos Aires Apartment Price Predictor")

# Description
st.write("Enter the apartment area to estimate its price.")

# Get area from the user
area = st.number_input(
    "Apartment Area (m²)",
    min_value=31.0,
    max_value=100.0,
    value=50.0
)

# Prediction button
if st.button("Predict Price"):

    # Prepare the input in the same format used to train the model
    input_data = pd.DataFrame({
        "surface_covered_in_m2": [area]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    st.success(f"Estimated Apartment Price: ${prediction:,.2f}")