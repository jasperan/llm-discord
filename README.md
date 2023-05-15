# llm-discord
Fine-tune an LLM to create a Discord bot that behaves like your friends


## discord_bot.py

The provided code is a Python script for a Discord bot that logs messages sent in a server to a SQLite3 database.

The script starts by importing necessary modules such as yaml, discord, sqlite3, datetime, and rich. It then reads the API token from a config.yaml file and initializes a discord.Client object with all intents enabled.

Next, the script establishes a connection to a SQLite3 database named messages.db and creates a table named messages with columns for author and content if it doesn't already exist. It also initializes a variable session_messages to keep track of the number of messages obtained during the current session.

The script then defines two event handlers for the discord.Client object. The first event handler is on_ready(), which is called when the bot is ready to start receiving events. It prints a message to the console and sets the bot's presence to "👀". The second event handler is on_message(), which is called whenever a message is sent in a server the bot is a member of. It extracts the message content and author, prints a log message to the console using the rich module, and inserts the message content and author into the messages table in the SQLite3 database.

Finally, the script checks if it is being run as the main program and starts the bot by calling client.run(API_TOKEN).

It is worth noting that the guild variable is not used in the script and can be removed. Additionally, the session_messages variable is not being used to its full potential and could be used to print a message to the console at the end of the session with the number of messages obtained.

Overall, this script provides a good starting point for a Discord bot that logs messages to a SQLite3 database.