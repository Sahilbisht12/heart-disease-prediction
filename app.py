import streamlit as st
import pandas as pd
import joblib 

model = joblib.load("Logistic_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns  = joblib.load("columns.pkl")

st.title("Heart Disease Prediction App")
st.markdown("Provide the following details.") 

age = st.slider("Age",18,100,40)
sex = st.selectbox("Sex",["Male","Female"])
chest_pain = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
Fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
max_heart_rate = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
exercise_induced_angina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST depression induced by exercise relative to rest)", 0.0, 10.0, 1.0)
stelevation_slope = st.selectbox("ST Segment Slope", ["Upsloping", "Flat", "Downsloping"])


if st.button("Predict"):
    raw_input = {
        'Age': age,
        'Resting Blood Pressure': resting_bp,
        'Cholesterol': cholesterol,
        'Fasting Blood Sugar': Fasting_blood_sugar,
        'Maximum Heart Rate Achieved': max_heart_rate,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'Chest Pain Type_' + chest_pain: 1,
        'Resting Electrocardiographic Results_' + resting_ecg: 1,
        'Exercise Induced Angina_' + exercise_induced_angina: 1,
        'ST Segment Slope_' + stelevation_slope: 1
        }
    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
            st.error("The model predicts that you have heart disease. Please consult a healthcare professional for further evaluation.")
    else:
            st.success("The model predicts that you do not have heart disease. However, please consult a healthcare professional for a comprehensive assessment.")