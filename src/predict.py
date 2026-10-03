import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "churn_model.pkl"

model = joblib.load(MODEL_PATH)
def predict_churn(customer_data):
    '''Predict whether a customer is likely to churn
    '''
    customer_df=pd.DataFrame([customer_data])
    prediction=model.predict(customer_df)[0]
    probability=model.predict_proba(customer_df)[0][1]
    return{
        "churn_prediction":int(prediction),
        "churn_probability":float(probability)
    }
    