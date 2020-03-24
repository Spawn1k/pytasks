s = input()
st = '>>-->'
st2 = '<--<<'
sch1 = sch2 = 0
i = 0
j = 0
k = -1
while i != -1:
    i = s.find(st, j)
    if (k != i) and (i != -1):
        k = i
        sch1 += 1
    j += 1
j = 0
i = 0
k = -1
while i != -1:
    i = s.find(st2, j)
    if (k != i) and (i != -1):
        k = i
        sch2 += 1
    j += 1
print(sch1+sch2)