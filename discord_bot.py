import yaml
import discord
import sqlite3
import datetime
from rich import print

'''
@author jasperan


'''
# define a variable to increment obtained messages during this session
session_messages = 0

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

API_TOKEN = config['API_TOKEN']

intents = discord.Intents.all()
client = discord.Client(intents=intents)
guild = discord.Guild

# establish connection to sqlite3 database
conn = sqlite3.connect('messages.db')
c = conn.cursor()

# create table to store messages if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS messages
             (author text, content text)''')



@client.event
async def on_ready():
    print('Hello {0.user} !'.format(client))
    await client.change_presence(activity=discord.Game('👀'))


@client.event
async def on_message(message):
    global session_messages
    #await client.wait_for('message')  # add this line to wait for a message
    #print(message.content)  # add this line
    message_content = message.content
    message_author = message.author
    print('[{}][{}][{}] {}'.format(session_messages, datetime.datetime.now(),
        message_author, message_content))

    # insert message content and author into sqlite3 database
    c.execute("INSERT INTO messages VALUES (?, ?)", (str(message_author), message_content))
    conn.commit()
    session_messages += 1

if __name__ == "__main__":
    client.run(API_TOKEN)