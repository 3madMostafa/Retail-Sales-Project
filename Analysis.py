import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
import plotly.express as px

def app():
    colored_header(
        label='You are in Data :green[Analysis] page',
        color_name='green-70',
        description=''
    )
    
    @st.cache_data
    def load_data():
        # Load the new dataset 'modified_subset_data.csv'
        df = pd.read_csv('modified_subset_data.csv')
        
        # Convert the 'date' column to datetime format
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        
        # Extract month and other necessary parts of the date
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day
        return df
    
    df = load_data()

    choice = st.selectbox("**Select an option to Explore their data**", ['Explore of Sales', 'Explore of Promotions'])

    if choice == 'Explore of Sales':

        st.markdown("## :rainbow[Stores and their sum of Sales]")
        sales = df.groupby(['store_nbr'])['sales'].sum().reset_index()
        st.bar_chart(sales, x='store_nbr', y='sales')

        st.markdown("## :rainbow[Top 10 Stores with Highest Sales]")
        highest_sale = df.groupby(['store_nbr'])['sales'].sum().reset_index().sort_values('sales', ascending=False).head(10)
        st.bar_chart(highest_sale, x='store_nbr', y='sales', color='#04f')

        st.markdown("## :rainbow[Top 10 Stores with Lowest Sales]")
        lowest_sale = df.groupby(['store_nbr'])['sales'].sum().reset_index().sort_values('sales', ascending=True).head(10)
        st.bar_chart(lowest_sale, x='store_nbr', y='sales', color='#fd0')

        st.markdown("## :rainbow[Sales by Product Family]")
        sales_family = df.groupby(['family'])['sales'].sum().reset_index()
        st.bar_chart(sales_family, x='family', y='sales')

        st.markdown("## :rainbow[Sum of Sales by Year]")
        total_year = df.groupby('year')['sales'].sum().reset_index()
        pie = px.pie(total_year, values='sales', names='year', width=900, height=500)
        st.plotly_chart(pie)

        col, col1 = st.columns([2, 2])
        with col:
            radio = st.radio('**Select a Year to Analyze Sales**', options=df['year'].unique(), horizontal=True)
        with col1:
            select = st.selectbox("**Select any feature**", ['onpromotion', 'transactions'])

        st.markdown(f"## :rainbow[{select} vs Sales]")
        data = df[df['year'] == radio]
        dataframe = data.groupby(select)['sales'].sum().reset_index()
        hist = px.histogram(dataframe, x=select, y='sales', width=1050)
        st.plotly_chart(hist)

        date_feature = st.selectbox("**Select a feature to explore sales periodically**", ['month', 'day', 'day_of_week', 'week_of_year'])

        st.markdown(f"## :rainbow[{date_feature} vs Sales]")
        dataframe = data.groupby(date_feature)['sales'].sum().reset_index()
        st.bar_chart(dataframe, x=date_feature, y='sales')

        st.markdown(f"## :rainbow[Date vs Sales]")
        date = data.groupby('date')['sales'].sum().reset_index()
        line = px.line(date, x='date', y='sales', title='Sum of Sales for Selected Year', width=1000, height=600)
        st.plotly_chart(line)

        st.markdown(f"## :rainbow[Holiday Type and Month vs Sales for Selected Year]")
        date = data.groupby(['month', 'holiday_type'])['sales'].sum().reset_index()
        bar = px.bar(date, x='holiday_type', y='sales', color='month', width=1000)
        st.plotly_chart(bar)

    elif choice == 'Explore of Promotions':
        st.markdown("## :rainbow[Stores and their sum of Promotions]")
        promotion = df.groupby(['store_nbr'])['onpromotion'].sum().reset_index()
        st.bar_chart(promotion, x='store_nbr', y='onpromotion')

        st.markdown("## :rainbow[Top 10 Stores with Highest Promotions]")
        highest_promotion = df.groupby(['store_nbr'])['onpromotion'].sum().reset_index().sort_values('onpromotion', ascending=False).head(10)
        st.bar_chart(highest_promotion, x='store_nbr', y='onpromotion', color='#04f')

        st.markdown("## :rainbow[Top 10 Stores with Lowest Promotions]")
        lowest_promotion = df.groupby(['store_nbr'])['onpromotion'].sum().reset_index().sort_values('onpromotion', ascending=True).head(10)
        st.bar_chart(lowest_promotion, x='store_nbr', y='onpromotion', color='#fd0')

        st.markdown("## :rainbow[Sum of Promotions by Year]")
        total_year = df.groupby('year')['onpromotion'].sum().reset_index()
        pie = px.pie(total_year, values='onpromotion', names='year', width=900, height=500)
        st.plotly_chart(pie)

        st.markdown(f"## :rainbow[Promotions by Product Family]")
        promotion_family = df.groupby(['family'])['onpromotion'].sum().reset_index()
        st.bar_chart(promotion_family, x='family', y='onpromotion')

# Run the app
app()
