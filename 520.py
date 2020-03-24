a = int(input())
# 134 is OK 
# 10 is OK
# last
c = a
k = c // 144
a = a % 144
if a > 133:
    k += 1
    a = 0
s = a // 12
a = a % 12
if a > 9:
    s += 1
    a = 0
p = a
print(k, s, p)