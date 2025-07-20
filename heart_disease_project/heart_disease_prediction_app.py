import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ----------------------------
# 🩺 Heart Disease Prediction App
# ----------------------------

st.title("❤️ Heart Disease Prediction App")

# ----------------------------
# Sidebar – Model Selection
# ----------------------------

st.sidebar.header("Select Classifier")
model_choice = st.sidebar.selectbox(
    "Choose model:",
    [
        "Logistic Regression",
        "Naive Bayes",
        "Bagging",
        "Gradient Boosting Machine",
        "Random Forest",
        "Decision Tree",
        "KNeighbors",
        "Support Vector Machine",
    ],
)

# ----------------------------
# Model Accuracy (Static Table)
# ----------------------------

accuracy_dict = {
    "Logistic Regression": 86,
    "Naive Bayes": 84,
    "Bagging": 84,
    "Gradient Boosting Machine": 84,
    "Random Forest": 82,
    "Decision Tree": 76,
    "KNeighbors": 74,
    "Support Vector Machine": 73,
}

# ----------------------------
# Model File Mapping
# ----------------------------

model_files = {
    "Logistic Regression": "models/logistic_regression_model.pkl",
    "Naive Bayes": "models/naive_bayes_model.pkl",
    "Bagging": "models/bagging_model.pkl",
    "Gradient Boosting Machine": "models/gradient_boosting_model.pkl",
    "Random Forest": "models/random_forest_model.pkl",
    "Decision Tree": "models/decision_tree_model.pkl",
    "KNeighbors": "models/knn_model.pkl",
    "Support Vector Machine": "models/svm_model.pkl",
}


# Load the selected model once (cached for performance)
@st.cache_resource
def load_model(path: str):
    return joblib.load(path)

model = load_model(model_files[model_choice])

# ----------------------------
# Input Form
# ----------------------------

st.header("Enter Patient Details")

# Friendly dropdown mappings
sex_map = {"Male": 1, "Female": 0}
cp_map = {"ATA": 0, "NAP": 1, "ASY": 2, "TA": 3}
restecg_map = {"Normal": 0, "ST": 1, "LVH": 2}
angina_map = {"Yes": 1, "No": 0}

# Collect user inputs
age = st.number_input("Age", min_value=1, max_value=120, step=1)
sex = st.selectbox("Sex", options=list(sex_map.keys()))
chest_pain = st.selectbox("Chest Pain Type", options=list(cp_map.keys()))
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, step=1)
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=50, max_value=600, step=1)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", options=[0, 1])
resting_ecg = st.selectbox("Resting ECG", options=list(restecg_map.keys()))
max_hr = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, step=1)
exercise_angina = st.selectbox("Exercise‑Induced Angina", options=list(angina_map.keys()))
oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=0.0, max_value=10.0, step=0.1)

# ----------------------------
# Prepare data & Predict
# ----------------------------

input_data = np.array([
    [
        age,
        sex_map[sex],
        cp_map[chest_pain],
        resting_bp,
        cholesterol,
        fasting_bs,
        restecg_map[resting_ecg],
        max_hr,
        angina_map[exercise_angina],
        oldpeak,
    ]
])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "🛑 Heart Disease Detected" if prediction == 1 else "✅ No Heart Disease"

    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error(result)
    else:
        st.success(result)

    st.info(f"Model Used: {model_choice}  |  Accuracy: {accuracy_dict[model_choice]}%")
