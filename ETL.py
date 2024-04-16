# Import libraries 
import requests # https requests
import pandas as pd #create DataFrame
import sqlalchemy # Create the SQLAlchemy engine
import os

# Read CSV file to panda DataFrame
csv_file = r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\continent_map.csv'
csv_file2 = r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\continents.csv'
csv_file3 = r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\countries.csv'
csv_file4 = r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\per_capita.csv'

df = pd.read_csv(csv_file)
df2 = pd.read_csv(csv_file2)
df3 = pd.read_csv(csv_file3)
df4 = pd.read_csv(csv_file4)

# MySQL connection parameters
username = os.getenv('MYSQL_USERNAME')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
database = os.getenv('MYSQL_DATABASE')

# Transform

print(df)
print(df2)
print(df3)
print(df4)


