import dash

from dash import dcc
from dash import html
# import pandas as pd
# import plotly.graph_objs as go
# from dash.dependencies import Input, Output
import pyodbc
import dash_bootstrap_components as dbc
app = dash.Dash(
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=L451\EASYTEST;"
    "Database=AdventureWorksDW2019;"
    "Trusted_Connection=yes;"
)

# Create an empty dictionary to store the data

# Stores quantity and date in a dictionary for 2011
dataFor2011 = {
    "Date": [],
    "OrderQuantity": []
}
# Stores quantity and date in a dictionary for 2012
dataFor2012 = {
    "Date": [],
    "OrderQuantity": []
}
# Stores quantity and date in a dictionary for 2013
dataFor2013 = {
    "Date": [],
    "OrderQuantity": []
}

def readDataProducts2011(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
			sum(fis.OrderQuantity) as quantity_per_day,
			dd.DayNumberOfYear
		FROM [dbo].[FactResellerSales] FIS
		JOIN [dbo].[DimProduct] DP ON DP.ProductKey = FIS.ProductKey
		JOIN [dbo].[DimDate] DD ON DD.DateKey = FIS.OrderDateKey or DD.DateKey = FIS.DueDateKey or DD.DateKey = FIS.ShipDateKey

		 where  dd.CalendarYear = 2011

		 group by dd.DayNumberOfYear 
         order by dd.DayNumberOfYear
    """)
    for row in cursor:

        for i in range(len(row)):
            if(i%2 == 0):
                dataFor2011["OrderQuantity"].append(row[i])
            else:
                dataFor2011["Date"].append(row[i])

    return dataFor2011

def readDataProducts2012(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
			sum(fis.OrderQuantity) as quantity_per_day,
			dd.DayNumberOfYear
		FROM [dbo].[FactResellerSales] FIS
		JOIN [dbo].[DimProduct] DP ON DP.ProductKey = FIS.ProductKey
		 JOIN [dbo].[DimDate] DD ON DD.DateKey = FIS.OrderDateKey or DD.DateKey = FIS.DueDateKey or DD.DateKey = FIS.ShipDateKey

		 where  dd.CalendarYear = 2012

		 group by dd.DayNumberOfYear 
         order by dd.DayNumberOfYear
    """)
    for row in cursor:

        for i in range(len(row)):
            if(i%2 == 0):
                dataFor2012["OrderQuantity"].append(row[i])
            else:
                dataFor2012["Date"].append(row[i])

    return dataFor2012

def readDataProducts2013(conn):
    cursor = conn.cursor()
    cursor.execute("""
     SELECT 
			sum(fis.OrderQuantity) as quantity_per_day,
			dd.DayNumberOfYear
		FROM [dbo].[FactResellerSales] FIS
		JOIN [dbo].[DimProduct] DP ON DP.ProductKey = FIS.ProductKey
		 JOIN [dbo].[DimDate] DD ON DD.DateKey = FIS.OrderDateKey or DD.DateKey = FIS.DueDateKey or DD.DateKey = FIS.ShipDateKey

		 where  dd.CalendarYear = 2013

		 group by dd.DayNumberOfYear 
         order by dd.DayNumberOfYear
    """)
    for row in cursor:
            
            for i in range(len(row)):
                if(i%2 == 0):
                    dataFor2013["OrderQuantity"].append(row[i])
                else:
                    dataFor2013["Date"].append(row[i])
    
    return dataFor2013


readDataProducts2011(conn) 
readDataProducts2012(conn)
readDataProducts2013(conn)


app = dash.Dash()
app.layout = html.Div(
    [
        html.H1("Group 5"),
        html.Div(
            'Dash: A web application framework for Python.'
        ),
        
        dcc.Graph(
            id='sample-graph',
            figure={
                'data': [
                    {'x': dataFor2011['Date'],
                    'y': dataFor2011['OrderQuantity'],
                    'type': 'line',
                    'name': 'Sales Per Day for 2011'},
                    {'x': dataFor2012['Date'],
                    'y': dataFor2012['OrderQuantity'],
                    'type': 'line',
                    'name': 'Sales Per Day for 2012'},
                    {'x': dataFor2013['Date'],
                    'y': dataFor2013['OrderQuantity'],
                    'type': 'line',
                    'name': 'Sales Per Day for 2013'},
                ],
                'layout': {
                    'title': 'Product Orders Per day for 2011-2013'
                }
            },
        )
    ]
)

if __name__ == '__main__':
    app.run_server(port=8080,debug=True)


