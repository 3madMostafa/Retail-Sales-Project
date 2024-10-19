import streamlit as st
from streamlit_extras.colored_header import colored_header

def app():
    # Display the header
    colored_header(
        label='Welcome to :orange[Home] Page 👋🏼',
        color_name='orange-70',
        description=''
    )
    
    # Create a form to display project details and link to dataset
    with st.form(key='form', clear_on_submit=False):

        st.markdown("## :orange[*Project Title*:]")
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Retail Sales Forecasting*")
        
        st.markdown("## :orange[*Skills Takeaway from This Project*:]")
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Python scripting, Data Wrangling, EDA, Model Building, Time Series Forecasting, Streamlit , ml-flow*")
        
        st.markdown("## :orange[*Domain*:]")
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Retail, Supermarkets, Chain Stores*")
        
        st.markdown("## :orange[*Problem Statement*:]")
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *Predict department-wide sales for each store for the next year, including the impact of markdowns on holiday weeks*")
        
        st.markdown("## :orange[*Results:*]") 
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; *The model accurately predicted department-wide sales for each store, considering historical data, seasonality, and markdown effects, using advanced time series forecasting techniques.*")
        
        # Button to get dataset link
        button = st.form_submit_button('**Click here to get Dataset Link**', use_container_width=True)
        
        if button:
            url = "https://www.kaggle.com/competitions/store-sales-time-series-forecasting"
            st.markdown(f"## :orange[Dataset: [Data Link]({url})]")

# Run the app
app()
