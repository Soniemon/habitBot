from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import rcParams


print("How many Days back would you like to track?")#needs to match the number of rows in data being read. in this specific case, it's 12
days = int(input())

str1 = ['100100011011',
        '111101110111']#getstring from data base, unadjusted
data=[]#declare empty array to hold adjusted, integer array
data2=[]

#ADJUST 2D ARRAY
for index in range(len(str1[0])): #read columns
     rowData = []
     for val in str1:
          rowData.append(int(val[index]))
     data.append(rowData)

for rows in range (days, 0, -1):
    data2.append(data[-rows])

#print(data2)#just checking
#============================================================

axisArray = []
for i in range(days):
     axisArray.append(i+1)
#print(axisArray)# just checking'


#-----------Formatting prior to graph creation----------------

cbar = False #Delete heatmap bar

#Figure Sizing
sns.set_theme(rc={'figure.figsize':(8.27, 11.7)})

##Formatting boxes
linewidths =2
linecolor = "white"
#-----------------------------------------------------------
    

    
#Create heatmapfrom data set
habitTracker = sns.heatmap(data=data2,
            cbar=cbar,
            linewidths=linewidths,
            linecolor=linecolor,
            cmap='Greens',
            square = True,)#<= makes boxes perfectly square


#Axis Formatting
habitTracker.set_title("Personal Habits")
habitTracker.set_xlabel("Habit")
habitTracker.xaxis.set_label_position("top")
habitTracker.xaxis.set_ticks_position("top")
habitTracker.set_yticklabels(habitTracker.get_yticklabels(), rotation=0,)
habitTracker.set_yticklabels(axisArray)
habitTracker.set_ylabel("Days")








#Save Tracker as png
fig = habitTracker.get_figure()
fig.savefig("myTracker.png")



plt.show()