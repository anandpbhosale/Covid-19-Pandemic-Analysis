# For Creating Arrays and Manipulation of Numerical Data
import dash
import numpy as np

# For Analyzing, Cleaning, Exploring and Manipulating Data
import pandas as pd

# For Visualization of Different Graphs
import plotly.graph_objs as go
import plotly.express as px

# The Dash-Core-Components are "Flask", "React.js", and "plotly.js"

# To build Analytical Web Application
# import dash_html_components as html
from dash import Dash, html, dcc
from dash.dependencies import Input, Output


""" In Python, external stylesheets are used to apply CSS styling to Dash Applications. 
Dash is a Python framework for building 'Analytical Web Application'. 
It uses 'plotly.js' for 'Data Visualization' and 'React.js' for the 'user interface'. """

external_stylesheet = [
    {
        "href" : "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
        "rel" : "stylesheet",
        "integrity" : "sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
        "crossorigin" : "anonymous"
    }
]


patients = pd.read_csv('state_wise_daily_data.csv')
total = patients.shape[0]
active = patients[patients['Status'] == 'Confirmed'].shape[0]
recovered = patients[patients['Status'] == 'Recovered'].shape[0]
deaths = patients[patients['Status'] == 'Deceased'].shape[0]


options = [
    {'label':'All', 'value':'All'},
    {'label':'Hospitalized', 'value':'Hospitalized'},
    {'label':'Recovered', 'value':'Recovered'},
    {'label':'Deceased', 'value':'Deceased'}
]



app = dash.Dash(__name__, external_stylesheets = external_stylesheet)


app.layout = html.Div([
    html.H1("Corona Virus Pandemic", style={'color':'#fff', 'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", style={'color': '#ffff'}),
                    html.H4(total, style={'color':'#ffff'})
                ], className= 'card-body')
            ], className= 'card bg-danger')
        ], className= 'col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases", style={'color':'#ffff'}),
                    html.H4(active, style={'color':'#ffff'})
                ], className= 'card-body')
            ], className= 'card, bg-info')
        ], className= 'col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases", style={'color':'#ffff'}),
                    html.H4(recovered, style={'color':'#ffff'})
                ], className='card-body')
            ], className= 'card bg-warning')
        ], className= 'col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Deaths", style={'color':'#ffff'}),
                    html.H4(deaths, style={'color':'#ffff'})
                ], className= 'card-body')
            ], className= 'card bg-success')
        ], className= 'col-md-3')
    ], className= 'row'),
    html.Div([
        html.Div([], className = 'col-md-6'),
        html.Div([], className = 'col-md-6')
    ], className= 'row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id = 'picker', options = options, value = 'All'),
                    dcc.Graph(id = 'bar')
                ], className = 'card-body')
            ], className = 'card')
        ], className = 'col-md-12')
    ], className= 'row')
], className= 'Container')



@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
def update_graph(type):

    if type == 'All':
        return{'data':[go.Bar(x=patients['State'], y=patients['Total'])],
               'layout': go.Layout(title = 'State Total Cases', plot_bgcolor='orange')
               }

    if type == 'Hospitalized':
        return {'data': [go.Bar(x=patients['State'], y=patients['Hospitalized'])],
                'layout': go.Layout(title='State Total Cases', plot_bgcolor='orange')
                }

    if type == 'Recovered':
        return{'data':[go.Bar(x=patients['Status'], y=patients['Recovered'])],
               'layout': go.Layout(title = "State Total Cases", plot_bgcolor='orange')
               }

    if type == 'Deceases':
        return{'data':[go.Bar(x=patients['Status'], y=patients['Deceases'])],
               'layout': go.Layout(title = "State  Total Cases", plot_bgcolor='orange')
               }



if __name__ == '__main__':
    app.run_server(debug = True)