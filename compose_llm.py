
"""
@author jasperan
This script retrieves messages from a SQLite3 database and creates a set of question-answer prompts
(message n + message n-1).
"""


import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('messages.db')

# Read table from sqlite database
df = pd.read_sql_query('SELECT * FROM messages', conn)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove empty messages
df = df[df['content'] != '']

# dataset is already in order, the more messages we store in messages.db, the better.

print(df.tail())
pd.set_option('display.max_columns', None)
print(len(df))



df.to_csv('messages.csv', index=True)