# Import libraries 
import requests # https requests
import pandas as pd #create DataFrame
from sqlalchemy import create_engine # Create the SQLAlchemy engine
import mysql.connector

# Read CSV file to panda DataFrame
csv_files = [r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\continent_map.csv',
r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\continents.csv',
r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\countries.csv',
r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\per_capita.csv']

# Transform into DataFrame
dataframes = [pd.read_csv(csv_file) for csv_file in csv_files]

print(dataframes)