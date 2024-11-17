#habitBot.py

import os
import discord
from discord.ext import commands #Implements detection and functionality for / commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#all permissions
#intents = discord.Intents.all()
#gives discord bot all permissions
#client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break


#     print(f'{client.user} is connected to the following guild:\n'
#           f'{guild.name}(id: {guild.id})'
#     )
    
#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if 'hello' in message.content.lower():
#         await message.channel.send(message.author.display_name)

guildBot = commands.Bot(command_prefix="/", intents = discord.Intents.all()) #Flags anything beginning with a / as a command

@guildBot.command(name="showCommands") #Behavior when /help is detected in chat
async def help(ctx): #Ctx is a required parameter that contains information about the message, including the channel and guild and user that called the command

    if ctx.author == guildBot.user:
        return

    response = """/showGrid --> Displays user's personal habit grid \n\n----------------------------------------\n
    /newRemind --> Set habit reminder timing \n\n----------------------------------------\n
    /changeRemind --> Adjust existing reminder timing \n\n----------------------------------------\n
    /showShared --> Show shared habit grid \n\n----------------------------------------\n
    /newHabit --> Set new habit \n\n----------------------------------------\n
    /deleteHabit --> Delete existing habit \n\n----------------------------------------\n
    /showStreak --> Show habit streaks \n\n----------------------------------------\n"""

    await ctx.send(response)


guildBot.run(TOKEN)
#client.run(TOKEN)