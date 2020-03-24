import math
a = int(input())
b = math.factorial(a)
g = str(b)
g = g[::-1]
for i in range(len(g)):
    if g[i] != '0':
        print(g[i])
        break