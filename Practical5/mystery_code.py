# What does this piece of code do?
# Answer:Select ten random numbers between 1 and 100 and print the tenth one

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress<10:
	progress+=1
	print(progress)
	#n = randint(1,100)
#print(n)
