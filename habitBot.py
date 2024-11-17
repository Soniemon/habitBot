#habitBot.py

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://officialbrandongomez:TrNDQVKztinNMINs@habittracker.3yibe.mongodb.net/?retryWrites=true&w=majority&appName=HabitTracker"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.logs 

#all permissions
intents = discord.Intents.all()
#gives discord bot all permissions
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    print("We're Here!")
    db.server_opened.insert_one(
        {
            "Time": "1"
        }
    )

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})'
    )
    
    #print names of all guild members
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hello' in message.content.lower():
        await message.channel.send(message.author.display_name)



client.run(TOKEN)