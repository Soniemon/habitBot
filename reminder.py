import datetime

class reminder:
    def __init__(self, reminderName, time, days):
        self.reminderName = reminderName
        self.time = time
        self.days = days   

    def getName(self):
        return self.reminderName
    
    def getTime(self):
        return self.time
    
    def getDays(self):
        return self.days
    
    def alert(self, dayOfWeek){
        #Monday = 0, Sunday = 6

        today = datetime.datetime.today()
        return self.days[dayOfWeek] == 1

    }
    

