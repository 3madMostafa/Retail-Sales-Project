import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import streamlit as st

def train_and_log_model():
    st.title("MLflow Model Training & Logging")

    st.markdown("""
    **Hello everyone!** This part we will explain it locally.
    """)
