a = 19245301
b = 4218520
c = 271
d = b-c
e = a-b
print(d)
print(e)
if d > e:
    print("d is bigger than e")
else:
    print("d is smaller than e")
#d is smaller than e
#the rate of 2021 is bigger than 2020
x = 1
y = 0
bool(x)
bool(y)
print(bool(x))
print(bool(y))
w = x and y
print(bool(w))
#the true table
def AND(x1,y1):
    w1,w2,theta = 0.5,0.5,0.7
    temp = x1*w1 + y1*w2
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1
#we need numpy package to test the true table
import numpy as np
x1 = np.array([0,1,0,1])
y1 = np.array([0,0,1,1])
for m in range(len(x1)):
    Name = "AND("+str(x1[m])+","+str(y1[m])+"):"
    Tmp = AND(x1[m],y1[m])
    W = Name
    print(W,str(Tmp))



