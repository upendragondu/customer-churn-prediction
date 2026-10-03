# Customer Churn Prediction & Retention Intelligence Platform

An end-to-end machine learning application that predicts customer churn probability and provides actionable retention recommendations.

## Problem

Customer churn can negatively affect business revenue.

This project uses customer demographic, service, contract, and billing information to predict whether a customer is likely to churn.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

## Machine Learning Workflow

1. Data loading
2. Data cleaning
3. Exploratory Data Analysis
4. Feature engineering
5. Train-test split
6. Categorical encoding
7. Feature scaling
8. Model training
9. Hyperparameter tuning
10. Model evaluation
11. Model serialization
12. Streamlit deployment

## Models

- Logistic Regression
- Decision Tree
- Random Forest

Hyperparameter tuning was performed using GridSearchCV with 5-fold cross-validation.

## Final Model Comparison

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Balanced Logistic Regression | 0.738 | 0.504 | 0.783 | 0.614 | 0.842 |
| Tuned Logistic Regression | 0.742 | 0.509 | 0.786 | 0.618 | 0.841 |
| Tuned Random Forest | 0.767 | 0.547 | 0.722 | 0.622 | 0.839 |

## Application

The Streamlit application accepts customer information and produces:

- Churn probability
- Churn risk level
- Retention recommendation

### Risk levels

- 70%+ → High risk
- 40–70% → Medium risk
- Below 40% → Low risk

## Project Structure

customer_churn_project/

├── app/
│   └── app.py
├── data/
├── models/
│   └── churn_model.pkl
├── notebooks/
│   └── 01_data_understanding.ipynb
├── src/
│   └── predict.py
└── README.md

## Run Locally

Install dependencies:

pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit

Run the application:

streamlit run app/app.py

## Future Improvements

- Customer retention cost optimization
- Explainable AI using SHAP
- Batch prediction
- Customer segmentation
- Model monitoring
- Cloud deployment