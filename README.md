# ❤️ Heart Disease Prediction App

A **Streamlit web application** that predicts the likelihood of a person having heart disease based on clinical input features. This project uses multiple machine learning models to provide users with options for model selection and displays prediction results with respective model accuracies.

---

## 🚀 Features

- Interactive and user-friendly web interface using **Streamlit**
- Choose from 8 pre-trained classifiers:
  - Logistic Regression
  - Naive Bayes
  - Bagging
  - Gradient Boosting Machine (GBM)
  - Random Forest
  - Decision Tree
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
- Predicts likelihood of heart disease based on:
  - Age
  - Sex
  - Chest Pain Type
  - Resting Blood Pressure
  - Cholesterol Level
  - Fasting Blood Sugar
  - Resting ECG Results
  - Max Heart Rate
  - Exercise-induced Angina
  - ST Depression (Oldpeak)
- Displays model-specific accuracy
- Custom form inputs for patient detail collection

---

## 🧰 Tech Stack

| Category       | Technology                |
|----------------|---------------------------|
| 💻 Language     | Python 3.9                |
| 📊 Libraries    | Pandas, NumPy, Scikit-learn, Joblib |
| 🧠 ML Models    | Logistic Regression, Naive Bayes, KNN, SVM, Random Forest, Decision Tree, Bagging, GBM |
| 🖥️ Frontend     | Streamlit                |
| 🗂️ Deployment   | Localhost (via Streamlit CLI) |
| 📁 Model Format | `.pkl` (Joblib)          |

---

## 🖼️ Screenshots

### 🧾 Home Page

![Home Screenshot](https://github.com/AyushMane1229/heart-disease-prediction/blob/eeb0690e7b91373710176137a166b2cfcbc020f4/Screenshot1.png)

### 🔍 Prediction Result

![Prediction Screenshot](https://github.com/AyushMane1229/heart-disease-prediction/blob/9ffe20aaeeaf4f00a86c8aad732c96aa1c338b8e/Screenshot2.png)

---

## 🛠️ Installation & Usage

1.Clone the repository and navigate into it:

```bash
git clone https://github.com/AyushMane1229/heart-disease-prediction.git
cd heart-disease-prediction
```

2.Create and activate a virtual environment (recommended):

```bash
conda create -n heart_env python=3.9
conda activate heart_env
```

3.Install required libraries directly:

```bash
pip install streamlit pandas numpy scikit-learn joblib
```

4.Ensure you have trained model `.pkl` files placed in a `models/` folder.

5.Run the app:

```bash
streamlit run heart_disease_prediction_app.py
```

---

## 📊 Dataset Used

This project uses a cleaned and preprocessed heart disease dataset sourced from the **UCI Machine Learning Repository** or **Kaggle**. It contains essential features for cardiovascular risk assessment.

---

## 🚧 Future Improvements

- Improve UI with more visual indicators (charts, risk meters, etc.)
- Deploy to cloud platforms (e.g., Streamlit Cloud, Azure, or Heroku)

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

- Fork the repository  
- Create a new branch (`git checkout -b feature/your-feature-name`)  
- Commit your changes (`git commit -m 'Add new feature'`)  
- Push to the branch (`git push origin feature/your-feature-name`)  
- Open a **Pull Request**

---

## 🙌 Acknowledgments

- UCI Heart Disease Dataset  
- Scikit-learn  
- Streamlit  
- Pandas
