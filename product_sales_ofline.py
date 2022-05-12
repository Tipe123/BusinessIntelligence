import dash

from dash import dcc
from dash import html
# import pandas as pd
# import plotly.graph_objs as go
# from dash.dependencies import Input, Output

from model import connection

import dash_bootstrap_components as dbc
app = dash.Dash(
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)


# The imported function is called to connect with the database
conn = connection()

# Create an empty dictionary to store the data


