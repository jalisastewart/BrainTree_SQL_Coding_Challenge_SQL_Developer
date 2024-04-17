# Import libraries 
import requests # https requests
import pandas as pd #create DataFrame
from sqlalchemy import create_engine # Create the SQLAlchemy engine
import mysql.connector
import configparser

# Read CSV file to panda DataFrame
csv_files = [r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\continent_map.csv',
r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\continents.csv',
r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\countries.csv',
r'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\per_capita.csv']

# Transform into DataFrame
dataframes = [pd.read_csv(csv_file) for csv_file in csv_files]

# Load MySQL credentials from config.ini
config = configparser.ConfigParser()
config.read('config.ini')


# #MySQL connection parameters
username = config['mysql']['MYSQL_USERNAME']
password = config['mysql']['MYSQL_PASSWORD']
host = config['mysql']['MYSQL_HOST']
database = config['mysql']['MYSQL_DATABASE']



# Create SQLAlchemy engine
mysql_credentials = f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
engine = create_engine(mysql_credentials)

# Table names
table_names = ['continent_map', 'continents', 'countries', 'per_capita']

# Insert DataFrames into MySQL
for df, table_name in zip(dataframes, table_names):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    
print("Data inserted into MySQL tables successfully!")