# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
style={'textAlign': 'center', 'color': '#503D36',
'font-size': 40}),

# TASK 1: Add a Launch Site Drop-down Input Component

dcc.Dropdown(id='site-dropdown',
options=[
{'label': 'ALL SITES', 'value': 'ALL'},
{'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
{'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
{'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
{'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
],
value='ALL',
placeholder="Select a Launch Site here",
searchable=True),
html.Br(),

# TASK 2: Add a callback function to render success-pie-chart based on selected site dropdown

html.Div(dcc.Graph(id='success-pie-chart')),
html.Br(),

html.P("Payload range (Kg):"),


# TASK 3: Add a Range Slider to Select Payload

dcc.RangeSlider(id='payload-slider',
min=0,max=10000,step=1000,
value=[min_payload,max_payload],
marks={0: '0', 2500:'2500',5000:'5000',
7500:'7500', 10000: '10000'}),

# TASK 4: Add a callback function to render the success-payload-scatter-chart scatter plot
html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# Run the app
if __name__ == '__main__':
app.run_server()