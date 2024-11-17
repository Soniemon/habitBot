from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import rcParams


def groupGridShow(names, data):

     #print("How many Days back would you like to track?")#needs to match the number of rows in data being read. in this specific case, it's 12
     days = 7#int(input())

     test = ['100100011011',
          '111101110111']#getstring from data base, unadjusted
     translatedArray=[]#declare empty array to hold adjusted, integer array
     truncatedArray=[]

     #ADJUST 2D ARRAY
     for index in range(len(data[0])): #read columns
          rowData = []
          for val in data:
               rowData.append(int(val[index]))
          translatedArray.append(rowData)

     for rows in range (days, 0, -1):
          truncatedArray.append(translatedArray[-rows])

     ##print(data2) #just checking
     #============================================================

     axisArray = []
     for i in range(days):
          axisArray.append(i+1)
     #print(axisArray)# just checking'


     #-----------Formatting prior to graph creation----------------

     cbar = False #Delete heatmap bar

     #Figure Sizing
     sns.set_theme(rc={'figure.figsize':(6, 8)})

     ##Formatting boxes
     linewidths =2
     linecolor = "white"
     #-----------------------------------------------------------
     

     
     #Create heatmapfrom data set
     habitTracker = sns.heatmap(data=truncatedArray,
               cbar=cbar,
               linewidths=linewidths,
               linecolor=linecolor,
               cmap='Greens',
               square = True,)#<= makes boxes perfectly square


     #Axis Formatting
     habitTracker.set_title("Community Habits")
     habitTracker.set_xlabel("Names")
     habitTracker.set_xticklabels(names)
     habitTracker.xaxis.set_label_position("top")
     habitTracker.xaxis.set_ticks_position("top")
     habitTracker.set_yticklabels(habitTracker.get_yticklabels(), rotation=0,)
     habitTracker.set_yticklabels(axisArray)
     habitTracker.set_ylabel("Days")








     #Save Tracker as png
     fig = habitTracker.get_figure()
     fig.savefig("myTracker.png")



     plt.show()