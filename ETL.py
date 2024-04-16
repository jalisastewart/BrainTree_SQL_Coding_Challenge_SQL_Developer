# Import libraries 
import requests # https requests
import pandas as pd #create DataFrame
import sqlalchemy # Create the SQLAlchemy engine

# Read CSV file to panda DataFrame
csv_file = 'C:\Users\jstew\DE_projects\BrainTree_SQL_Coding_Challenge\BrainTree_SQL_Coding_Challenge_SQL_Developer\data_csv\continent_map.csv'
df = pd.read_csv(csv_file)

