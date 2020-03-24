a = list(map(int, input().split()))
ves = 0
for i in range(1, a[0]):
    ves += i*a[1]
if ves == a[3]:
    print(a[0])
else:
    num = abs(a[3] - ves)
    num = int(num / a[2])
    print(num)