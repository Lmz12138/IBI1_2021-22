def Slice(a):
    return (a**2 + a + 2)/2 #define a function of this formula
for i in range(1,64):
    print(Slice(i)) # make a list of i increasing
n = 64
print(f"when n equals 64, the result is:{Slice(n)}")
# The method used by mystery_code.py
b = 0 # set a condition
while b < 64: #make a loop
   b += 1
   s = (b**2 + b +2)/2
   print(s)
print("the slice is incease with increasing number of straight cuts"
      f"and when n equals 64,the total number is {s}")
