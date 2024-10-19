import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import streamlit as st

def train_and_log_model():
    st.title("MLflow Model Training & Logging")

    # Load dataset
    try:
        df = pd.read_csv('modified_subset_data.csv')
    except FileNotFoundError:
        st.error("Dataset not found. Please ensure 'modified_subset_data.csv' is available.")
        return

    # Select features and target
    X = df[['is_weekend', 'year', 'month', 'day_of_week', 'week_of_year', 'store_nbr', 'cluster']]
    y = df['sales']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # End any active MLflow run to avoid conflict
    if mlflow.active_run():
        mlflow.end_run()

    # Set experiment name or create it if it doesn't exist
    experiment_name = "Retail_Sales_Prediction"
    mlflow.set_experiment(experiment_name)

    # Start a new MLflow run
    with mlflow.start_run() as run:
        # Train the XGBoost model
        model = XGBRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Predictions and metrics
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)

        # Log model parameters, metrics, and the model itself
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "xgboost_model")

        # Display metrics in Streamlit
        st.write(f"Model logged with MSE: {mse}")
        st.write(f"MLflow Run ID: {run.info.run_id}")
        st.write(f"Experiment ID: {run.info.experiment_id}")

        # Provide a link to the MLflow run in the Streamlit UI
        st.markdown(f"[View Run in MLflow](http://127.0.0.1:5000/#/experiments/{run.info.experiment_id}/runs/{run.info.run_id})")

    st.success("Model training and logging completed.")
