# Heart Disease Prediction

An end-to-end machine learning web app built with Python, Streamlit, and scikit-learn to predict heart disease risk based on patient health indicators.

## Overview

This project loads a trained logistic regression model and a scaler to predict whether a patient is likely to have heart disease. The app accepts medical parameters such as age, sex, cholesterol, blood pressure, and other clinical features through a simple UI.

## Repository Structure

```text
heart-disease-prediction/
├── README.md
├── LICENSE
├── app.py
├── Logistic_heart.pkl
├── columns.pkl
├── scaler.pkl
├── Data/
│   └── heart.csv
├── Notebook/
│   └── Heart.ipynb
├── assests/
│   └── Screenshot 2026-10-01 143227.png
└── .gitignore
```

## Files and Folders

- `app.py` — Streamlit app for user input and prediction
- `Logistic_heart.pkl` — trained machine learning model
- `scaler.pkl` — preprocessing scaler used for model input
- `columns.pkl` — expected feature columns for the model
- `Data/heart.csv` — dataset used for training and analysis
- `Notebook/Heart.ipynb` — notebook containing the exploratory and model-building workflow
- `assests/` — screenshots or images related to the project
- `LICENSE` — MIT license for the repository

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Sahilbisht12/heart-disease-prediction.git
cd heart-disease-prediction
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install streamlit pandas scikit-learn joblib
```

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- scikit-learn
- Joblib
- Jupyter Notebook

## Model Details

The app uses a logistic regression model trained on heart disease-related patient data. It predicts the likelihood of heart disease based on the selected health indicators and standardized feature values.

## Notes

This application is intended for educational and informational use only. It should not replace professional medical advice or diagnosis.

## License

This project is licensed under the MIT License.
