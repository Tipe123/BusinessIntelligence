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


# Stores quantity and date in a dictionary for 2011
dataFor2011 = {
    "Date": [],
    "SalesAmount": []
}
# Stores quantity and date in a dictionary for 2012
dataFor2012 = {
    "Date": [],
    "SalesAmount": []
}
# Stores quantity and date in a dictionary for 2013
dataFor2013 = {
    "Date": [],
    "SalesAmount": []
}


def readData(conn , data,year):
    cursor = conn.cursor()
    cursor.execute(f"""
     SELECT 
	SUM(FRS.SalesAmount) salesAmount,
	DD.DayNumberOfYear
    FROM [dbo].[FactResellerSales] FRS
    JOIN [dbo].[DimProduct] DP ON FRS.ProductKey = DP.ProductKey
    JOIN [dbo].[DimDate] DD ON FRS.OrderDateKey=DD.DateKey OR FRS.ShipDateKey=DD.DateKey OR FRS.DueDateKey=DD.DateKey

    WHERE DD.CalendarYear = {year}
    GROUP BY DD.DayNumberOfYear
    ORDER BY DD.DayNumberOfYear
    """)
    for row in cursor:
            
            for i in range(len(row)):
                if(i%2 == 0):
                    data["SalesAmount"].append(row[i])
                else:
                    data["Date"].append(row[i])
    
    return data
readData(conn , dataFor2011,2011)
readData(conn , dataFor2012,2012)
readData(conn , dataFor2013,2013)


def sales_offline_figure():
    return html.Div(
        [
            html.Div(
                children=[
                    html.H1("Offline Sales Amount Per Day"),
                ],
                className="text-center",
            ),
            
            dcc.Graph(
                id='order-quantity-graph',
                figure={
                    'data': [
                        {'x': dataFor2011['Date'],
                        'y': dataFor2011['SalesAmount'],
                        'type': 'line',
                        'name': 'Sales Amount Per Day for 2011'},
                        {'x': dataFor2012['Date'],
                        'y': dataFor2012['SalesAmount'],
                        'type': 'line',
                        'name': 'Sales Amount Per Day for 2012'},
                        {'x': dataFor2013['Date'],
                        'y': dataFor2013['SalesAmount'],
                        'type': 'line',
                        'name': 'Sales Amount Per Day for 2013'},
                    ],
                    'layout': {
                        'title': 'Sales Amount Per day for 2011-2013',
                        'xaxis': {'title': 'Days'},
                        'yaxis': {'title': 'Sales Amount'},
                        
                    }
                },
            )
        ]
    )



if __name__ == '__main__':
    app.run_server(port=8080,debug=True)

