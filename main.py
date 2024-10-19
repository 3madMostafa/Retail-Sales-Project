import streamlit as st
from streamlit_option_menu import option_menu
import Home, Filtering, Analysis, Prediction, ML_Flow
from PIL import Image

# Set up the Streamlit page configuration
st.set_page_config(page_title='Retail Sales Forecasting', layout='wide')

# Define the multiapp class
class MultiApp:
    def __init__(self):
        self.apps = []  # List to hold all apps
        
    def add_app(self, title, function):
        self.apps.append({'title': title, 'function': function})  # Add each app with its function
        
    def run(self):
        # Sidebar menu to switch between pages
        with st.sidebar:
            app_choice = option_menu('Retail Sales Forecasting', 
                                     ["Home", "Data Filtering", "Data Analysis", "Data Prediction", "MLflow"], 
                                     icons=['house', 'search', "reception-4", "dice-5-fill", "clipboard-data"], 
                                     menu_icon='cash-coin', default_index=0, orientation="vertical",
                                     styles={
                                         "container": {"padding": "0!important", "background-color": "#A95C68"},
                                         "icon": {"color": "violet", "font-size": "20px"}, 
                                         "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#C4A484"},
                                         "nav-link-selected": {"background-color": "#C04000"},
                                     })

        # Run the selected app based on the sidebar choice
        for app in self.apps:
            if app['title'] == app_choice:
                app['function']()

# Create an instance of the multiapp class
app = MultiApp()

# Add apps to the multiapp instance
app.add_app("Home", Home.app)
app.add_app("Data Filtering", Filtering.app)
app.add_app("Data Analysis", Analysis.app)
app.add_app("Data Prediction", Prediction.app)
app.add_app("MLflow", ML_Flow.train_and_log_model)  # Adding the MLflow functionality

# Run the multiapp
app.run()
