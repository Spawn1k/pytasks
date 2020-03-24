import math
fin = open('INPUT.TXT')
a = list(map(int, fin.readline().split()))
b = list(map(int, fin.readline().split()))
d = math.sqrt((a[1]-b[1])**2 + (a[0]-b[0])**2)
if d < max(a[2], b[2]):
    if d + min(a[2], b[2]) >= max(a[2], b[2]):
        print('YES')
    else:
        print('NO')
elif d <= a[2]+b[2]:
    print('YES')
else:
    print('NO')