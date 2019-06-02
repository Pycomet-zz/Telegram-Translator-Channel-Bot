# This code written by codefredy 

# This script is built for python 3

# This bot scraped content from a Hebrew channel
# Translate the extracted text to English
# And also posts the english verion of the text to a different channel

# Importing necessary modules for this software
import telepot
from telethon import TelegramClient, sync, events
from telethon.tl.types import InputPeerChannel
from googletrans import Translator

# Defining all the needed variables for full functionality
token = '' # Input your bot here
api_id = '' # Input your api_id here
api_hash = '' # Input your api_hash here

translator = Translator()
channel_id = -1001158360927
access_hash = 0

# Connecting telegram api and 
client = TelegramClient('Connected', api_id, api_hash)
client.start()
bot = telepot.Bot(token)
print("YOUR TELEGRAM BOT IS ACTIVE!")

# Accessing channel
chat = InputPeerChannel(channel_id=channel_id, access_hash=access_hash)

# Grabbing any new post on amitsegal channel
@client.on(events.NewMessage(chat, incoming=True)) # For every post this function is called
def my_event_handler(event):
    '''For every new post, this function is executed'''

    msg = event.message.message
    post = translator.translate(msg).text # Traslating the post to english
    print(post) # print the post to console
    bot.sendMessage(chat_id=-1001346220934, text=post) # Post to channel

client.add_event_handler(my_event_handler)
client.run_until_disconnected()


