# Import libraries 
import requests # https requests
import pandas as pd #create DataFrame
import sqlalchemy # Create the SQLAlchemy engine
import os

# Read CSV file to panda DataFrame
csv_file = 'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\continent_map.csv'
df = pd.read_csv(csv_file)

# MySQL connection parameters
username = os.getenv('MYSQL_USERNAME')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
database = os.getenv('MYSQL_DATABASE')