from turtle import title
import dash

from dash import dcc
from dash import html
import plotly.express as px
import dash_bootstrap_components as dbc
import pyodbc
# This is a connecttion
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=L451\EASYTEST;"
    "Database=AdventureWorksDW2019;"
    "Trusted_Connection=yes;"
)

# This is a function to store the connection
# The function is imported by other files
def connection():
    return conn

app = dash.Dash(
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)



conn = connection()

salesOnline = {
    "name": "online",
    "amount": []
}
salesReseller = {
    "name": "reseller",
    "amount": []
}

# Get the data from the database
def readData(conn,data,table):
    cursor = conn.cursor()
    cursor.execute(f"""
      SELECT 
	SUM(FRS.SalesAmount) salesAmount
FROM [dbo].[{table}] FRS
JOIN [dbo].[DimProduct] DP ON FRS.ProductKey = DP.ProductKey
JOIN [dbo].[DimDate] DD ON FRS.OrderDateKey=DD.DateKey OR FRS.ShipDateKey=DD.DateKey OR FRS.DueDateKey=DD.DateKey



		 
    """)
    for row in cursor:
            for i in range(len(row)):
                data["amount"].append(row[i])
    
    return data

readData(conn,salesOnline,"FactInternetSales")
readData(conn,salesReseller,"FactResellerSales")




def all_sales_figure():
    return html.Div([
        html.H1("Sales of Online and Reseller",
                style={"text-align": "center"}),
        dcc.Graph(figure={
            'data': [
                {'x': salesOnline["name"],
                'y': salesOnline["amount"],
                'type': 'bar',
                'name': 'Sales of Online'},
                {'x': salesReseller["name"],
                'y': salesReseller["amount"],
                'type': 'bar',
                'name': 'Sales of Reseller'},
            ],
            'layout': {
                'title': 'Sales of Online and Reseller',
                'xaxis': {'title': 'category'},
                'yaxis': {'title': 'Sales Amount'},
            },
        })
    ])



