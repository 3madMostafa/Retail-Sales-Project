import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load your data
train = pd.read_csv(r'D:\DepiTasks\Retail-Sales-Project\store-sales-time-series-forecasting/train.csv')
train['date'] = pd.to_datetime(train['date'])

# Pre-compute data to avoid repeated calculations in callbacks
# Group by family and store n° for total sales by category
category_sales = train.groupby('family')['sales'].sum().reset_index()

# Group by date and store n° for sales trends
sales_trend = train.groupby(['date', 'store_nbr'])['sales'].sum().reset_index()

# Group by date and family for promotions
promotion_heatmap_data = train.groupby(['date', 'family'])['onpromotion'].sum().reset_index()

# Initialize Dash app
app = dash.Dash(__name__)

# App layout with multiple visualizations
app.layout = html.Div([
    html.H1("Promotions and Sales Dashboard"),

    # Dropdown for selecting store (ordered)
    dcc.Dropdown(
        id='store-dropdown',
        options=[{'label': str(store), 'value': store} for store in sorted(train['store_nbr'].unique())],
        value=sorted(train['store_nbr'].unique())[0],
        multi=False
    ),

    # Graphs
    dcc.Graph(id='sales-promotion-graph'),
    dcc.Graph(id='category-sales-bar'),
    dcc.Graph(id='sales-trend-line'),
    dcc.Graph(id='promotion-heatmap'),
    dcc.Graph(id='sales-boxplot'),
])

# Callback to update all graphs based on selected store
@app.callback(
    [Output('sales-promotion-graph', 'figure'),
     Output('category-sales-bar', 'figure'),
     Output('sales-trend-line', 'figure'),
     Output('promotion-heatmap', 'figure'),
     Output('sales-boxplot', 'figure')],
    [Input('store-dropdown', 'value')]
)
def update_graphs(selected_store):
    # Filter data for the selected store
    filtered_data = train[train['store_nbr'] == selected_store]

    # 1. Sales vs. Promotions by Store (Line Chart)
    sales_promotion_fig = px.line(
        filtered_data, 
        x='date', 
        y='sales', 
        color='onpromotion',
        title=f"Sales vs. Promotions for Store {selected_store}"
    )

    # 2. Total Sales by Product Category (Bar Chart)
    category_sales_fig = px.bar(
        category_sales, 
        x='family', 
        y='sales',
        title="Total Sales by Product Category"
    )

    # 3. Sales Trend by Date for Different Stores (Line Chart)
    sales_trend_fig = px.line(
        sales_trend, 
        x='date', 
        y='sales', 
        color='store_nbr',
        title="Sales Trend by Date for Different Stores"
    )

    # 4. Promotions by Product Category Over Time (Heatmap)
    promotion_heatmap_fig = px.density_heatmap(
        promotion_heatmap_data, 
        x='date', 
        y='family', 
        z='onpromotion',
        title="Promotions by Product Category Over Time"
    )

    # 5. Sales Distribution Across Stores (Box Plot)
    sales_boxplot_fig = px.box(
        train, 
        x='store_nbr', 
        y='sales', 
        title="Sales Distribution Across Stores"
    )

    return sales_promotion_fig, category_sales_fig, sales_trend_fig, promotion_heatmap_fig, sales_boxplot_fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
