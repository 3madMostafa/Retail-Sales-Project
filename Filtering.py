import streamlit as st
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header

def app():
    # Display colored header
    colored_header(
        label='You are in Data :blue[Filtering] page',
        color_name='blue-70',
        description=''
    )
    
    # Load the available data (subset_data.csv)
    @st.cache_data
    def load_data():
        df = pd.read_csv('subset_data.csv')
        return df

    df = load_data()

    # Optional: If you need to perform any transformations like date conversion
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Use dataframe_explorer for filtering the dataframe
    filtered_df = dataframe_explorer(df)

    # Submit button to display filtered data
    button = st.button('**SUBMIT**', use_container_width=True)
    if button:
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

# Run the app
app()
