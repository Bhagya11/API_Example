import streamlit as st
import joblib
import numpy as np
from sklearn.datasets import load_iris

# Load the trained model
model = joblib.load("iris_model.pkl")

# Load Iris target names for class interpretation
target_names = load_iris().target_names

# Streamlit App
st.title("🌸 Iris Flower Prediction App")

st.markdown("Enter the features of the flower below to predict its class:")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)

# Predict button
if st.button("Predict"):
    # Prepare input data
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    # Model prediction
    predicted_class = model.predict(input_data)[0]
    predicted_class_name = target_names[predicted_class]

    # Display result
    st.success(f"🌼 Predicted Class: {predicted_class_name} (Class Index: {predicted_class})")
