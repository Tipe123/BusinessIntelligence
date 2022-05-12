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



conn = connection()

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



def readData(conn , data,year):
    cursor = conn.cursor()
    cursor.execute(f"""
      SELECT 
		sum(frs.OrderQuantity) orderQuantity,
		dd.DayNumberOfYear
    FROM dbo.FactResellerSales frs
	INNER JOIN dbo.DimProduct dp ON frs.ProductKey = dp.ProductKey
	INNER JOIN dbo.DimDate dd ON frs.OrderDateKey = dd.DateKey OR frs.ShipDateKey = dd.DateKey Or frs.DueDateKey = dd.DateKey
	 
    where  dd.CalendarYear = {year}

    group by dd.DayNumberOfYear 
    order by dd.DayNumberOfYear
		 
    """)
    for row in cursor:
            
            for i in range(len(row)):
                if(i%2 == 0):
                    data["OrderQuantity"].append(row[i])
                else:
                    data["Date"].append(row[i])
    
    return data


readData(conn,dataFor2011,2011) 
readData(conn,dataFor2012,2012)
readData(conn,dataFor2013,2013)


def product_figure_reseller():
    return html.Div(
        [
            html.Div(
                children=[
                    html.H1("Ofline Products Order Quantity"),
                ],
                className="text-center",
            ),
            
            dcc.Graph(
                id='order-quantity-graph',
                figure={
                    'data': [
                        {'x': dataFor2011['Date'],
                        'y': dataFor2011['OrderQuantity'],
                        'type': 'bar',
                        'name': 'order quantity Per Day for 2011'},
                        {'x': dataFor2012['Date'],
                        'y': dataFor2012['OrderQuantity'],
                        'type': 'bar',
                        'name': 'order quantity Per Day for 2012'},
                        {'x': dataFor2013['Date'],
                        'y': dataFor2013['OrderQuantity'],
                        'type': 'bar',
                        'name': 'order quantity Per Day for 2013'},
                    ],
                    'layout': {
                        'title': 'Product Orders Per day for 2011-2013',
                        'xaxis': {'title': 'Day'},
                        'yaxis': {'title': 'Order Quantity'},
                        
                    }
                },
            )
        ]
    )



if __name__ == '__main__':
    app.run_server(port=8080,debug=True)


