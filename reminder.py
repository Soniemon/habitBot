'''import datetime
from ast import literal_eval

class reminder:
    def __init__(self, reminderName, time, days):
        self.reminderName = reminderName
        self.time = time
        self.days = literal_eval(days)   

    def getName(self):
        return self.reminderName
    
    def getTime(self):
        return self.time
    
    def getDays(self):
        return self.days
    
    def setName(self, newName):
        self.reminderName = newName


    def setTime(self, newTime):
        self.time = newTime
  

    def setDays(self, newDays):
        self.days = literal_eval(newDays)

    
    def alert(self, dayOfWeek):
        #Monday = 0, Sunday = 6

        today = datetime.datetime.today()
        return self.days[dayOfWeek] == 1
    
    def __str__(self):
        key = ("Monday ", "Tuesday ", "Wednesday ", "Thursday ", "Friday ", "Saturday ", "Sunday ")
        output = "Reminder for: {0}, set to go off at {1}, repeating every ".format(self.reminderName, self.time)

        for ind, val in enumerate(self.days):
            if(val == 1):
                output += key[ind]
            
        return output
'''
    