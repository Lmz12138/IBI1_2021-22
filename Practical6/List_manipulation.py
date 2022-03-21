import matplotlib.pyplot as plt
marks = [45, 36, 86, 57, 53, 92, 65, 45]
marks_sorted = sorted(marks) #sort this list
print(marks_sorted)
plt.boxplot(marks_sorted, vert=False, meanline=True)
plt.show() # draw the boxplot
import numpy as np
average = np.mean(marks_sorted) #get the average
print(average)
print(average > 60) #compare the result
if average > 60:
    print("it is bigger than 60")
else:
    print("it is smaller than 60") #output the result


