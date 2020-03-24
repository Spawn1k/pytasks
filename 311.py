import math
a = int(input())
sum_ = 0
for i in range(1, a+1):
    sum_ += math.factorial(i)
print(sum_)