from pymongo import MongoClient
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


def addServer(serverName):
    server_collection.insert_one(
        {
            'serverName' : serverName,
            'users' : [],
            'habits' : []
        }
    )

def addUser(username):
    user_collection.insert_one(
        {
            'username' : username,
            'reminders' : [],
            'habits' : []
        }
    )

def updateServer(serverName, users, habit):
    server_collection.update_one({'serverName' : serverName}, {'$push' : {'habits' : habit}})

def updateUser(username, habit, startDate):
    user_collection.update_one({'username' : username}, {'$push': {'habits' : habit} })

def removeHabit(username, habit):
    return
    

'''def addHabit(habit, server):
    serverId = findServerId(server)
    habit_collection.insert_one(
        {
            'habit' : habit,
            'server' : serverId
        }
    )

def addUserHabitData(user, habit, habitData):
    habitId = findHabitId(habit)
    userId = findUserId(user)
    userHabitData_collection.insert_one(
        {
            'habit' : habitId,
            'username' : userId,
            'userHabitData' : habitData
        }
    )

def findServerId(serverName):
    #Finds server by name from server collection; returns object id as dict
    results = server_collection.find({'serverName' : serverName}, {'_id' : 1})
    #Turns Dict to string and formats to leave only object id
    return str(results.next()).strip('{}').split()[1]

def findHabitId(habitName):
    results = habit_collection.find({'habit' : habitName}, {'_id' : 1})
    return str(results.next()).strip('{}').split()[1]


def findUserId(username):
    results = user_collection.find({'username' : username}, {'_id' : 1})
    return str(results.next()).strip('{}').split()[1]
'''

