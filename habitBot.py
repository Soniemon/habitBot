#habitBot.py

import os
import discord
import datetime
from reminder import reminder
from discord.ext import commands #Implements detection and functionality for / commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

guildBot = commands.Bot(command_prefix="/", intents = discord.Intents.all()) #Flags anything beginning with a / as a command

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

        for category in guild.categories:
            if category.name == "Habits":
                break

        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True),
        }


        await guild.create_text_channel(habit_name, category = category, overwrites=overwrites)
        
    else:

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
                break
               
    

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