#import matplotlib.pyplot as ply

# file = open("percentages.csv", "w")
# file.write("56, 12, 34, 25, 4, 5, 7")
# file.close()

# file = open("percentages.csv", "r")
# dataIn = file.read()
# file.close()

# percentages = dataIn.split(",")

# file = open("colours.txt", "w")
# file.write("Blue, Red, Green, Purple, Pink, Orange, Yellow")
# file.close()

# file = open("colours.txt", "r")
# colourRead = file.read()
# file.close

# colours = colourRead.split(",")

# y = [0, 10, 20, 30, 40, 50, 60]
# ply.bar(colours, y)
# ply.title("Favourite Colour popularity")
# ply.xlabel('Colours')
# ply.ylabel('Percentage')
# ply.show()



loetz do it


import matplotlib.pyplot as ply
import numpy as np

file = open("percentages.csv", "w")
file.write("56, 12, 34, 25, 4, 5, 7")
file.close()

file = open("percentages.csv", "r")
dataIn = file.read()
file.close()

percentages = dataIn.split(",")

y = np.array([56, 12, 34, 25, 4, 5, 7])
mylabels = ["56%", "12%", "34%", "25%", "4%", "5%", "7%"]

ply.pie(y, labels = mylabels)
mycolors = ["Blue", "Red", "Green", "Purple", "Pink", "Orange", "Yellow"]
ply.title("The Most Prefered Colours in the World")
ply.pie(y, labels = mylabels, colors = mycolors)
ply.show() 






# Investigation & Planning 

 

# What question are you asking? 

# What are the most popular colours in the world. 


# Design 

 

# Create a flowchart of your process – what did you do first, then next etc 

# Describe how you gathered your data. <<<<<
#                                          ^
# google searched for most popular colours ^


# Describe what you had to do to pre-process your data – were there outliers, did you have to impute any data due to missing values, were there any erroneous code. 
# the data didnt need to be processed because everything there was already processes


# What graphs/charts did you use to display your data and why did you choose them. 

 

# Implementation 

# Describe what you did – a bit more detail than your flowchart. 

 

# Was there any iteration? - Did you change your mind about your idea or a step in the process. 

# Explain why you made some decisions. 

 

# Evaluation 

# Does you code answer your question. 

# What analytics did you do in order to answer your question. 

# Is there anything you would do differently the next time? 

 

 

 

# References 

# Websites visited: 

# Googl ඞ

Among us ඞ Among us ඞ 

Je ඞsse! Jesse! Nahhh