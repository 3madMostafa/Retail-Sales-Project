import streamlit as st
from streamlit_extras.colored_header import colored_header
import pandas as pd
import xgboost as xgb

def app():
    colored_header(
        label='Welcome to Data :red[Prediction] page 👋🏼',
        color_name='red-70',
        description='Weekly Sales Prediction'
    )

    @st.cache_data
    def load_data():
        try:
            # Load the updated dataset
            df = pd.read_csv('modified_subset_data.csv')  # Ensure correct dataset is loaded
            return df
        except FileNotFoundError:
            st.error("Data file not found. Please ensure 'updated_subset_data.csv' is in the correct directory.")
            return None

    df = load_data()

    if df is not None:
        with st.form(key='form', clear_on_submit=False):
            is_weekend = st.selectbox(
                "**Is it a weekend?**",
                options=[0, 1]  # 0 for no, 1 for yes
            )

            year = st.selectbox(
                "**Select a Year**",
                options=df['year'].unique(),
            )

            month = st.selectbox(
                "**Select a Month**",
                options=df['month'].unique(),
            )

            day_of_week = st.selectbox(
                "**Select Day of the Week**",
                options=df['day_of_week'].unique(),
            )

            week_of_year = st.selectbox(
                "**Select Week of the Year**",
                options=df['week_of_year'].unique(),
            )

            store_nbr = st.selectbox(
                "**Select a Store Number**",
                options=df['store_nbr'].unique(),
            )

            cluster = st.selectbox(
                "**Select a Store Cluster**",
                options=df['cluster'].unique(),
            )

            # Submit button (ensuring it's included)
            button = st.form_submit_button('**Predict**', use_container_width=True)

            # Perform prediction only when the form is submitted
            if button:
                try:
                    # Load the XGBoost model using load_model
                    model = xgb.XGBRegressor()
                    model.load_model('new_model (1).pkl')  # Load the newly trained model

                    # Prepare the input in the same structure as the model expects (7 features)
                    input_features = [[
                        is_weekend,     # Is it a weekend?
                        year,           # Year
                        month,          # Month
                        day_of_week,    # Day of the week
                        week_of_year,   # Week of the year
                        store_nbr,      # Store number
                        cluster         # Store cluster
                    ]]

                    # Perform prediction
                    result = model.predict(pd.DataFrame(input_features, columns=[
                        'is_weekend', 'year', 'month', 'day_of_week', 'week_of_year',
                        'store_nbr', 'cluster'
                    ]))

                    st.markdown(f"## :green[*Predicted Sales is {result[0]}*]")

                except FileNotFoundError:
                    st.error("Model file not found. Please ensure 'new_model.pkl' is in the correct directory.")
                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")
