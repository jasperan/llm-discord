
"""
@author jasperan
This script retrieves messages from a SQLite3 database and creates a set of question-answer prompts
(message n + message n-1).
"""


import sqlite3
import pandas as pd
import ujson as json
# Connect to the database
conn = sqlite3.connect('messages.db')


def db_to_csv(conn):

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

    return df


def json_format(df):
    result = list()

    for index, row in df.iterrows():
        try:
            response = df.iloc[index]['content']
            question = df.iloc[index-1]['content']
            desired_format = {"question": question, "response": response}
            result.append(desired_format)
        except IndexError:
            continue

    return result


def write_to_json_file(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


df = db_to_csv(conn)
result = json_format(df)
print(result)

write_to_json_file(result, 'output.json')