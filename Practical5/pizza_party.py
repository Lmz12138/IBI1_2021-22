def Slice(a):
    return (a**2 + a + 2)/2
for i in range(1,64):
    print(Slice(i))
n = 64
print(f"when n equals 64, the result is:{Slice(n)}")