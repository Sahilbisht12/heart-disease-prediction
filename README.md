# Heart Disease Prediction

An end-to-end Machine Learning web app built with Scikit-learn and Streamlit to predict heart disease risk.

## Overview

This project is designed to predict the likelihood of heart disease using patient health parameters such as age, sex, blood pressure, cholesterol, fasting blood sugar, ECG results, and more. The application uses a trained machine learning model and presents an interactive interface built with Streamlit.

## Features

- User-friendly Streamlit web app
- Real-time risk prediction
- Medical feature input form
- Model-based classification of heart disease risk
- Clean and readable UI
- Easy setup and deployment

## App Screenshots

Add your app screenshots into the `assets/screenshots/` folder and reference them here.

### Main Prediction Interface

![Heart Disease Prediction App](assets/screenshots/heart-disease-app.png)

### Prediction Result Section

![Prediction Result](assets/screenshots/prediction-result.png)

## File Structure

```text
heart-disease-prediction/
├── README.md
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── data/
│   ├── raw/
│   │   └── heart_disease.csv
│   └── processed/
│       └── heart_disease_processed.csv
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── 06_final_model.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│   ├── train_model.py
│   └── utils.py
├── app/
│   ├── streamlit_app.py
│   ├── styles.css
│   └── assets/
│       └── images/
│           └── app_icon.png
├── assets/
│   └── screenshots/
│       ├── heart-disease-app.png
│       └── prediction-result.png
├── models/
│   ├── trained_model.pkl
│   ├── scaler.pkl
│   └── feature_names.pkl
├── tests/
│   ├── test_preprocessing.py
│   └── test_model.py
├── docs/
│   ├── project_summary.md
│   └── usage_guide.md
└── LICENSE
```

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

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app/streamlit_app.py
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
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Model Overview

The app uses a supervised machine learning model trained on heart disease-related patient data. It predicts whether a patient is likely to have heart disease based on their health indicators.

## Notes

This application is intended for educational and informational use only. It should not replace medical advice or professional diagnosis.

## License

This project is licensed under the MIT License.
