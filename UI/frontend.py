import streamlit as st
import requests

# ---- SET YOUR API URL HERE ----
API_URL = "http://localhost:8000/prediction"  # change to your deployed URL if needed
HEALTH_URL = "http://localhost:8000/health"

st.title("Insurance Premium Prediction App")
st.markdown("Enter the details below to get a prediction from the ML model API.")

# Check API Health
try:
    health = requests.get(HEALTH_URL).json()
    st.sidebar.success(f"API Status: {health['status']} (v{health['version']})")
except Exception as e:
    st.sidebar.error("API Health Check Failed")
    st.stop()

# Input Form
with st.form(key="input_form"):
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    income_lpa = st.number_input("Annual Income (in LPA)", min_value=0.0, value=5.0)
    smoker = st.selectbox("Smoker", options=[True, False])
    occupation = st.selectbox("Occupation", options=[
        'retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed' or 'private_job'
    ])
    height = st.number_input("Height", min_value=0.5, max_value=5.0, value=3.0)
    weight = st.number_input("weight", min_value=0.5, value=30.0)
    city = st.selectbox("City", options=['delhi', 'mumbai', 'bangalore', 'kolkata', 'pune', 'hyderabad' ])

    submit = st.form_submit_button("Predict")

if submit:
    input_data = {
        "age": age,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "occupation": occupation,
        "height": height,
        "weight": weight,
        "city": city
    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            prediction = response.json()["response"]
            st.success(f"Prediction: {prediction}")
        else:
            st.error(f"API Error: {response.text}")
    except Exception as e:
        st.error(f"Request Failed: {e}")
