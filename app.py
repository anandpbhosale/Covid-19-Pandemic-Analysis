# first we are going to install all necessary Libraries
# pip install numpy
# pip install pandas
# falsk is installing to deploy the project on local host i.e. for url
# pip install flask
# pip install dash
# pip install plotly

# The Dash Core Components are "flask", "React.js", and "plotly.js"


# Now we are going to import all the necessary Libraries
# 1. For Creating Arrays and Manipulation of Numerical Data
import numpy as np

# 2. For Analyzing, Cleaning, Exploring and Manipulating Data
import pandas as pd

# 3. For Visualization using different Graphs
import plotly.graph_objs as go
import plotly.express as px

# 4. To build Analytical Web Application
import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


external_stylesheets = [
    {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
        "rel": "stylesheet",
        "integrity": "sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
        "crossorigin": "anonymous"
    },
    {
        "href": "/assets/styles.css",
        "rel": "stylesheet"
    }
]

# Load data
patients = pd.read_csv("state_wise_daily_data.csv")
total = patients.shape[0]
active = patients[patients['Status'] == 'Confirmed'].shape[0]
recovered = patients[patients['Status'] == 'Recovered'].shape[0]
deaths = patients[patients['Status'] == 'Deceased'].shape[0]

# Dropdown options
options1 = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Hospitalized', 'value': 'Hospitalized'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}
]

options2 = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Mask', 'value': 'Mask'},
    {'label': 'Sanitizer', 'value': 'Sanitizer'},
    {'label': 'Oxygen', 'value': 'Oxygen'}
]

options3 = [
    {'label': 'Red Zone', 'value': 'Red Zone'},
    {'label': 'Blue Zone', 'value': 'Blue Zone'},
    {'label': 'Green Zone', 'value': 'Green Zone'},
    {'label': 'Orange Zone', 'value': 'Orange Zone'}
]

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'COVID-19 Pandemic'

app.layout = html.Div([
    html.H1('COVID-19 Pandemic', style={'color': '#2C3E50', 'text-align': 'center', 'margin-bottom': '30px'}),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases', className='text-light'),
                    html.H4(total, className='text-light')
                ], className='card-body')
            ], className='card shadow-lg', style={'background': 'linear-gradient(45deg, #2193b0, #6dd5ed)'})
        ], className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases", className='text-light'),
                    html.H4(active, className='text-light')
                ], className='card-body')
            ], className='card shadow-lg', style={'background': 'linear-gradient(45deg, #fc4a1a, #f7b733)'})
        ], className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3('Recovered Cases', className='text-light'),
                    html.H4(recovered, className='text-light')
                ], className='card-body')
            ], className='card shadow-lg', style={'background': 'linear-gradient(45deg, #56ab2f, #a8e063)'})
        ], className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Deaths', className='text-light'),
                    html.H4(deaths, className='text-light')
                ], className='card-body')
            ], className='card shadow-lg', style={'background': 'linear-gradient(45deg, #e53935, #e35d5b)'})
        ], className='col-md-3')
    ], className='row mt-3'),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='plot-graph', options=options2, value='All', className='mb-3'),
                    dcc.Graph(id='line-graph')
                ], className='card-body')
            ], className='card shadow-lg', style={'background': 'linear-gradient(45deg, #8e2de2, #4a00e0)'})
        ], className='col-md-6'),

        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown', options=options3, value='Red Zone', className='mb-3'),
                    dcc.Graph(id='pie-chart')
                ], className='card-body')
            ], className='card shadow-lg', style={'background': 'linear-gradient(45deg, #ff6a00, #ee0979)'})
        ], className='col-md-6')
    ], className='row mt-3'),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker', options=options1, value='All', className='mb-3'),
                    dcc.Graph(id='bar')
                ], className='card-body')
            ], className='card shadow-lg', style={'background': 'linear-gradient(45deg, #0099f7, #f11712)'})
        ], className='col-md-12')
    ], className='row mt-3')
], className='container-fluid main-background')


@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
def update_graph(type):
    data = []
    if type == 'All':
        data = go.Bar(x=patients['State'], y=patients['Total'], marker_color='#FF6347')
    elif type == 'Hospitalized':
        data = go.Bar(x=patients['State'], y=patients['Hospitalized'], marker_color='#4CAF50')
    elif type == 'Recovered':
        data = go.Bar(x=patients['State'], y=patients['Recovered'], marker_color='#FFD700')
    elif type == 'Deceased':
        data = go.Bar(x=patients['State'], y=patients['Deceased'], marker_color='#FF4500')

    return {'data': [data], 'layout': go.Layout(title='State Total Cases', plot_bgcolor='#F0F8FF')}


@app.callback(Output('line-graph', 'figure'), [Input('plot-graph', 'value')])
def generate_graph(type):
    data = []
    if type == 'All':
        data = go.Scatter(x=patients['Date'], y=patients['Total'], mode='lines', line=dict(color='#FF6347'))
    elif type == 'Mask':
        data = go.Scatter(x=patients['Date'], y=patients['Mask'], mode='lines', line=dict(color='#4CAF50'))
    elif type == 'Sanitizer':
        data = go.Scatter(x=patients['Date'], y=patients['Sanitizer'], mode='lines', line=dict(color='#1E90FF'))
    elif type == 'Oxygen':
        data = go.Scatter(x=patients['Date'], y=patients['Oxygen'], mode='lines', line=dict(color='#FFD700'))

    return {'data': [data], 'layout': go.Layout(title='Commodities Total Count', plot_bgcolor='#F0F8FF')}


@app.callback(Output('pie-chart', 'figure'), [Input('my_dropdown', 'value')])
def generate_graph(my_dropdown):
    piechart = px.pie(data_frame=patients, names=my_dropdown, hole=0.3,
                      color_discrete_sequence=px.colors.sequential.RdBu)
    return piechart


if __name__ == "__main__":
    app.run_server(debug=True)
