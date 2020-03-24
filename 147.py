import math
n = int(input())
k1 = ((1 + math.sqrt(5))/2) ** n
k2 = ((1 - math.sqrt(5))/2) ** n
print(int((k1-k2)/math.sqrt(5)))