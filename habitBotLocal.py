#habitBotLocal.py

import os
import discord
import datetime
#from mongo import *
#from habitBotFiles import reminder
from reminder import reminder
from discord.ext import commands #Implements detection and functionality for / commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


"""
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

db = client.habitTracker
server_collection = db.server_collection
user_collection = db.user_collection
"""

guildBot = commands.Bot(command_prefix="/", intents = discord.Intents.all()) #Flags anything beginning with a / as a command
#all permissions
#gives discord bot all permissions

"""
for guild in guildBot.guilds:
    if not server_collection.find_one({'serverName' : str(guild.name)}):
        addServer(serverName=str(guild.name))
"""
        

#print(db.find({'serverName' : {in : ['Adam']}})

'''results = db.find({'serverName' : 'Jacob' },{'_id' : 1})
print(str(results.next()).strip('{}').split()[1])'''

@guildBot.event
async def on_ready():
    print(f'{guildBot.user} has connected to Discord!')

    for guild in guildBot.guilds:
        if guild.name == GUILD:
            break



    existing_category = discord.utils.get(guild.categories, name = "Habits")
    if not existing_category:
        print(f'Creating a new category: {"Habits"}')
        category = await guild.create_category("Habits")
        print(f'Creating a new channel: {"Controller"}')
        await guild.create_text_channel("Controller", category=category)
        #overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),}
        #await guild.create_text_channel("Memory", category=category, overwrites=overwrites)
        f = open("habits.txt",  "w")
        f.close()

   



@guildBot.command(name="showCommands") #Behavior when /help is detected in chat
async def showCommands(ctx): #Ctx is a required parameter that contains information about the message, including the channel and guild and user that called the command

    if ctx.author == guildBot.user:
        return

    response = """/showGrid --> Displays user's personal habit grid \n\n----------------------------------------\n
    /newReminder --> Set habit reminder timing \n\n----------------------------------------\n
    /changeReminder --> Adjust existing reminder timing \n\n----------------------------------------\n
    /showShared --> Show shared habit grid \n\n----------------------------------------\n
    /newHabit --> Set new habit \n\n----------------------------------------\n
    /deleteHabit --> Delete existing habit \n\n----------------------------------------\n
    /showStreak --> Show habit streaks \n\n----------------------------------------\n"""
    await ctx.send(response)

@guildBot.command(name="newHabit")
async def newHabit(ctx, habit_name):
    guild = ctx.guild
    member = ctx.author
    existing_habit = discord.utils.get(guild.channels, name = habit_name)

    if not existing_habit:
        print(f'Creating a new channel for the habit: {habit_name}')
        f = open("habits.txt", "a")
        f.write(habit_name + "\n")
        f.close()

        f = open(habit_name + ".txt", "a")
        f.write(member.display_name + ":")
        f.close()


        for category in guild.categories:
            if category.name == "Habits":
                break

        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True),
        }

        """
        if not server_collection.find_one({'habits' : habit_name}):
            updateServer(GUILD,'',habit_name)
        if not user_collection.find_one({'username' : str(member)}):
            addUser(str(ctx.author))
        if not user_collection.find_one({'habits' : { '$in' : [habit_name]}}):
            updateUser(username=str(ctx.author),habit=habit_name, startDate='')"""
        await guild.create_text_channel(habit_name, category = category, overwrites=overwrites)
        
        
    else:

        f = open(habit_name + ".txt", "a")
        f.write("\n")
        f.write(member.display_name + ":")
        f.close()

        for category in guild.categories:
            if category.name == "Habits":
                break

        for channel in category.channels:
            if channel.name == habit_name:
                perms = channel.overwrites_for(member)
                perms.send_messages = True
                perms.read_messages = True
                await channel.set_permissions(member, overwrite = perms)
                break
        
"""
@guildBot.command(name = "join")
async def join(ctx):
    guild = ctx.guild
    member = ctx.author
    
    if not user_collection.find_one({'username' : str(member)}):
        addUser(str(ctx.author))
    if not user_collection.find_one({'habits' : { '$in' : [str(ctx.channel)]}}):
        updateUser(username=str(ctx.author),habit=str(ctx.channel), startDate='')
"""


@guildBot.command(name = "removeHabit")
async def removeHabit(ctx, habit_name):
    guild = ctx.guild
    member = ctx.author

    


    existing_habit = discord.utils.get(guild.channels, name = habit_name)
    if existing_habit:

        for category in guild.categories:
           if category.name == "Habits":
               break
        

        for channel in category.channels:
            if channel.name == habit_name:
                perms = channel.overwrites_for(member)
                perms.send_messages = False
                perms.read_messages = False
                await channel.set_permissions(member, overwrite = perms)

                f = open(habit_name + ".txt", "r")
                lines = f.readlines()
                f.close()
                f = open(habit_name + ".txt", "w")
                for line in lines:
                    if not member.display_name in line.strip("\n"):
                        f.write(line)
                f.close


                f = open(habit_name + ".txt", "r")
                all = f.read()
                f.close()
                deleteChannel = True
                for members in guild.members:
                    if members.display_name in all:
                        deleteChannel = False
                        break

                if(deleteChannel):
                    await channel.delete()
                    with open("habits.txt", "r") as f:
                        lines = f.readlines()
                        f.close()
                    with open("habits.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != habit_name:
                                f.write(line)
                        f.close()
               
    

@guildBot.command(name = "newReminder")
async def newReminder(ctx, name, when, repeat):

    alert = reminder(name, when, repeat)
    await ctx.channel.send(alert)


@guildBot.command(name = "changeReminder")
async def changeReminder(ctx, field, value):

    if(field == "name"):

        print("a")

    elif(field == "time"):

        print("b")

    elif(field == "days"):

        print("c")



guildBot.run(TOKEN)