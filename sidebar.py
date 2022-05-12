import dash
import dash_bootstrap_components as dbc

from dash import html
from dash import dcc

import plotly.express as px
from dash.dependencies import Input, Output


# File imports for other functions
from ProductSales.salesType import all_sales_figure
    # the function that contains online data
from ProductOrders.products_online_data import product_figure
    # the function that contains reseller data
from ProductOrders.products_reseller_data import product_figure_reseller
    # the function that contains reseller data

    # the function that contains offline sale amount data
from ProductSales.product_sales_offline import sales_offline_figure ,sales_yaerly_offline_figure
from ProductSales.product_sales_online import sales_online_figure ,sales_yaerly_online_figure



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
            "DashBoard For Database Project ", className="lead mt-4 mb-4"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Product Orders", href="/", active="exact"),
                dbc.NavLink("Sales", href="/Sales", active="exact"),
                dbc.NavLink("Orders", href="/Orders", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
    className="bg-dark text-white",
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
        ),
        
    ]
        
    elif pathname == "/Sales":
        return[
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-md-5 card shadow p-3 mb-5 bg-body rounded align-middle m-auto rounded-3",
                    children=[
                        
                       sales_online_figure()
                    ]
                ),
                html.Div(
                    className="col-md-5 card shadow p-3 mb-5 bg-body rounded align-middle m-auto rounded-3",
                    children=[
                       sales_offline_figure()
                    ]
                ),
                
            ]
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-md-5 card shadow p-3 mb-5 bg-body rounded align-middle m-auto rounded-3",
                    children=[
                        
                       sales_yaerly_online_figure()
                    ]
                ),
                html.Div(
                    className="col-md-5 card shadow p-3 mb-5 bg-body rounded align-middle m-auto rounded-3",
                    children=[
                       sales_yaerly_offline_figure()
                    ]
                ),
                
            ]
        ),
        html.Div(
            className="row",
            children=[

                html.Div(
                    className="w-50 card shadow p-3 mb-5 bg-body rounded align-middle m-auto rounded-3 bg-dark text-white",
                    children=[
                        all_sales_figure()
                    ]
                ),
                
            ]
        )
       
    ]
    elif pathname == "/Orders":
        return [
                # sales_all_figure()
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


