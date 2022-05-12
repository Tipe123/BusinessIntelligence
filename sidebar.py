import dash
import dash_bootstrap_components as dbc

from dash import html
from dash import dcc

import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import pyodbc

# File imports for other functions

    # the function that contains online data
from products_online_data import product_figure
    # the function that contains reseller data
from products_reseller_data import product_figure_reseller
# data source: https://www.kaggle.com/chubak/iranian-students-from-1968-to-2017
# data owner: Chubak Bidpaa
df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Group 5", className="display-4 font-weight-bold text-center"),
        html.Hr(),
        html.P(
            "DashBoard For Database Project ", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Products", href="/", active="exact"),
                dbc.NavLink("Sales", href="/Sales", active="exact"),
                dbc.NavLink("Orders", href="/Orders", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return[
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-md-6",
                    children=[
                        product_figure()
                    ]
                ),
                html.Div(
                    className="col-md-6",
                    children=[
                        product_figure_reseller()
                    ]
                ),
                
            ]
        )
       
    ]
        
    elif pathname == "/Sales":
        return [
                html.H1('Grad School in Iran',
                        style={'textAlign':'center'}),
                        # Begining of the graph
                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Years',
                         y=['Girls Grade School', 'Boys Grade School'])
                         )
                         #  End of the graph
                ]
    elif pathname == "/Orders":
        return [
                html.H1('High School in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Years',
                         y=['Girls High School', 'Boys High School']))
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__=='__main__':
    app.run_server(debug=True, port=8000)
