
"""
@author jasperan
This script retrieves messages from a SQLite3 database and creates a set of question-answer prompts
(message n + message n-1).
"""


import json
import sqlite3

import pandas as pd


def db_to_csv(conn):

    # Read table from sqlite database
    df = pd.read_sql_query('SELECT * FROM messages', conn)

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove empty messages
    df = df[df['content'] != '']

    # dataset is already in order, the more messages we store in messages.db, the better.

    print(df.tail())
    pd.set_option('display.max_columns', None)
    print(len(df))

    df.to_csv('messages.csv', index=True)

    return df


def json_format(df):
    # Pair each message with the one before it, by position: the index has gaps
    # after the cleanup in db_to_csv, so label-based lookups would skip pairs.
    contents = df['content'].tolist()
    return [{"question": q, "response": r} for q, r in zip(contents, contents[1:])]


def write_to_json_file(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    conn = sqlite3.connect('messages.db')
    df = db_to_csv(conn)
    result = json_format(df)
    print(result)

    write_to_json_file(result, 'output.json')
