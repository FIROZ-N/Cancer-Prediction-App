import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.datasets import load_breast_cancer

# Load saved model
model = pickle.load(open("model.pkl", "rb"))

# Load dataset to get sample values
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Use only 5 key features
key_features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness']

st.title("🩺 Breast Cancer Prediction App (5 Key Features)")
st.write("Enter the following 5 key features to predict if the tumor is **Benign** or **Malignant**.")

# Input fields for 5 features
user_input = []
for feature in key_features:
    mean_value = float(df[feature].mean())
    value = st.number_input(f"{feature}", value=mean_value)
    user_input.append(value)

# Predict button
if st.button("Predict"):
    final_input = np.array(user_input).reshape(1, -1)
    prediction = model.predict(final_input)[0]
    result = "Benign" if prediction == 1 else "Malignant"
    
    st.success(f"Prediction: {result}")
    if result == "Benign":
        st.balloons()
    else:
        st.error("⚠️ Malignant: Please consult a doctor immediately.")
