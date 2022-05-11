import dash

from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
app = dash.Dash(
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)


app.layout = html.Div(
    [
        # Header
        html.H1( 
            className="text-center", 
            children="Group 5",
            style={
                "font-size": "3rem",
                "color": "#456FBV",
                "font-weight": "bold",
            }),
        html.Div(
            className="text-center mt-3",
            style={
                "font-size": "1.5rem",
                "color": "#456FBV",
            },
            children=[
                html.P( "Dash: A web application framework for Python."),
            ]),
            #End of Header

            # Body Part
            dbc.Container(
            dcc.Graph(
                id='sampleChart',

                figure={
                    'data': [
                        {'x':[4,8,12,16,20],'y':[8,12,16,20,24],'type':'bar','name':'First Chart'},
                        {'x':[4,8,12,16,20],'y':[12,16,20,24,28],'type':'bar','name':'Second Chart'},
                    ],
                    'layout': {
                        'plot_bgcolor':'#D3D3D3',
                        'paper_bgcolor':'Blue',
                        'font':{
                            'color':'red'
                        },
                        'title': 'Sample Chart'
                    }
                }
            ),
            ),
        # End Of Body
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)