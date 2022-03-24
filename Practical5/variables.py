a = 19245301
b = 4218520
c = 271 #set the variable
d = b-c
e = a-b #use equal sign for assignment
print(d)
print(e)
if d > e: #set the condition
    print("d is bigger than e, the rate of 2021 is smaller than 2020")
else:
    print("d is smaller than e, the rate of 2021 is bigger than 2020")
#d is smaller than e
#the rate of 2021 is bigger than 2020
x = 1 #set the variable
y = 0
bool(x) # make logical decision
bool(y)
print(bool(x))
print(bool(y))
w = x and y # make bool decision
print(bool(w))
#the true table
def AND(x1,y1):
    w1,w2,theta = 0.5,0.5,0.7 #Weighted assignment
    temp = x1*w1 + y1*w2 #set the true table formula
    if temp <= theta: #logical decision
        return 0
    elif temp > theta:
        return 1
#we need numpy package to test the true table
import numpy as np
x1 = np.array([0,1,0,1])
y1 = np.array([0,0,1,1])#Arranged into matrices
for m in range(len(x1)):
    Name = "AND("+str(x1[m])+","+str(y1[m])+"):"
    Tmp = AND(x1[m],y1[m])
    W = Name
    print(W, str(Tmp))



