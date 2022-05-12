# This is a model file used to connect with the database and the file is imported to the files connection doing database manupulations.
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

# Function to select data from the database
# The function is imported by other files
