b = int(input())
a = list(map(int, input().split()))
i = 0
answ = 0
if (b > 1) and (a[0] != a[1]):
    sch = 2
else:
    sch = 1
answ = sch
for i in range(2, b):
    if (a[i-2] > a[i-1] < a[i]) or (a[i-2] < a[i-1] > a[i]):
        sch += 1
    elif sch != 1:
        sch = 2
    answ = max(answ, sch)
print(answ)