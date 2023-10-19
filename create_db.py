import sqlite3
import csv
import requests
import pandas as pd


# Create and connect to the database
conn = sqlite3.connect('Currency_db.db')
cursor = conn.cursor()

# Create Bitcoin table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Bitcoin (
        Month_Year DATE,
        Closing_Price REAL,
        Volume INTEGER
    )
''')

# Create Gold table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Gold (
        Month_Year DATE,
        Closing_Price REAL,
        Volume INTEGER
    )
''')

# Create Silver table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Silver (
        Month_Year DATE,
        Closing_Price REAL,
        Volume INTEGER
    )
''')

# Connect to the SQLite database
conn = sqlite3.connect('Currency_db.db')

# Read the CSV data into a pandas DataFrame
bitcoin_df = pd.read_csv('currency_csvs/bitcoin.csv')
gold_df = pd.read_csv('currency_csvs/gold.csv')
silver_df = pd.read_csv('currency_csvs/silver.csv')


# Insert data from the DataFrame into the tables
bitcoin_df.to_sql('Bitcoin', conn, if_exists='replace', index=False)
gold_df.to_sql('Gold', conn, if_exists='replace', index=False)
silver_df.to_sql('Silver', conn, if_exists='replace', index=False)




# Commit changes and close the database connection
conn.commit()
conn.close()
