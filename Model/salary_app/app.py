import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("salary_prediction_model.pkl")

st.title("AI Job Salary Prediction")

# Collect inputs
job_title = st.text_input("Job Title", "Machine Learning Engineer")
company_location = st.text_input("Company Location (e.g., US)", "US")
employee_residence = st.text_input("Employee Residence", "US")
industry = st.text_input("Industry", "Tech")
employment_type = st.selectbox("Employment Type", ["FT","PT","CT","FL"])
experience_level = st.selectbox("Experience Level", ["EN","MI","SE","EX"])
company_size = st.selectbox("Company Size", ["S","M","L"])
education_required = st.text_input("Education Required", "Bachelor")
required_skills = st.text_area("Required Skills", "Python, Machine Learning")
years_experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=3)
salary_currency = st.text_input("Salary Currency", "USD")
remote_ratio = st.slider("Remote Ratio (%)", 0, 100, 100)
job_description_length = st.number_input("Job Description Length", min_value=10, value=500)
benefits_score = st.number_input("Benefits Score", min_value=0.0, max_value=1.0, value=0.8)
posting_date = pd.to_datetime("2025-01-01")
application_deadline = "2025-12-31"
year = 2025

# Prepare DataFrame with **same columns as training**
if st.button("Predict Salary"):
    input_df = pd.DataFrame([{
        "job_id": "101",
        "job_title": job_title,
        "company_name": "Demo",
        "company_location": company_location,
        "employee_residence": employee_residence,
        "industry": industry,
        "employment_type": employment_type,
        "experience_level": experience_level,
        "company_size": company_size,
        "education_required": education_required,
        "required_skills": required_skills,
        "years_experience": years_experience,
        "salary_currency": salary_currency,
        "remote_ratio": remote_ratio,
        "job_description_length": job_description_length,
        "benefits_score": benefits_score,
        "posting_date": posting_date,
        "application_deadline": application_deadline,
        "year": year
    }])

    salary_usd = model.predict(input_df)[0]
    salary_inr = salary_usd * 83  # approx USD→INR

    st.success(f"Predicted Salary: ${salary_usd:,.2f} (~₹{salary_inr:,.0f})")
