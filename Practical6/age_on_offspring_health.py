import numpy as np
paternal_age = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75] #list the data
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
print(paternal_age)
print(chd)
dic = {'30': 1.03, '35': 1.07, '40': 1.11, '45': 1.17, '50': 1.23, '55': 1.32,
       '60': 1.42, '65': 1.55, '70': 1.72, '75': 1.94}# make a dictionary
print(dic)
import matplotlib.pyplot as plt# import matlab package
x = paternal_age #set the axes
y = chd
plt.scatter(x, y, color='blue') #set the figure
plt.show()
print(dic['45'])#Check for correctness
print(dic['55'])
