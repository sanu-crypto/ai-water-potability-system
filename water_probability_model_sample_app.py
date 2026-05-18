import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(page_title="Water Potability Prediction App", page_icon="💧", layout="centered")

@st.cache_resource
def load_files():
    with open("water_potability_rf_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("water_potability_imputer.pkl", "rb") as f:
        imputer = pickle.load(f)
    return model, imputer

model, imputer = load_files()

st.title("💧 Water Potability Prediction App")
st.write("Enter the water quality values below to predict whether the water is safe for drinking or not.")

# User input fields
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=200.0)
solids = st.number_input("Solids", min_value=0.0, value=20000.0)
chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0)
sulfate = st.number_input("Sulfate", min_value=0.0, value=300.0)
conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=14.0)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=70.0)
turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)

if st.button("Predict"):
    # Step 1: original 9 features
    input_df = pd.DataFrame([{
        "ph": ph,
        "Hardness": hardness,
        "Solids": solids,
        "Chloramines": chloramines,
        "Sulfate": sulfate,
        "Conductivity": conductivity,
        "Organic_carbon": organic_carbon,
        "Trihalomethanes": trihalomethanes,
        "Turbidity": turbidity
    }])

    # Step 2: apply same imputer used during training
    input_imputed = pd.DataFrame(
        imputer.transform(input_df),
        columns=input_df.columns
    )

    # Step 3: create same engineered features used during training
    input_imputed["ph_Hardness"] = input_imputed["ph"] * input_imputed["Hardness"]
    input_imputed["Solids_Conductivity"] = input_imputed["Solids"] * input_imputed["Conductivity"]
    input_imputed["Chloramines_Turbidity"] = input_imputed["Chloramines"] * input_imputed["Turbidity"]
    input_imputed["Organic_Trihalo"] = input_imputed["Organic_carbon"] * input_imputed["Trihalomethanes"]

    # Step 4: prediction
    prediction = model.predict(input_imputed)[0]
    prediction_proba = model.predict_proba(input_imputed)[0]

    if prediction == 1:
        st.success("✅ Water is Safe for Drinking")
    else:
        st.error("❌ Water is Not Safe for Drinking")

    st.write("### Prediction Probability")
    st.write(f"Not Safe: **{prediction_proba[0] * 100:.2f}%**")
    st.write(f"Safe: **{prediction_proba[1] * 100:.2f}%**")