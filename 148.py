a = list(map(int, input().split()))
while a[0] != 0 and a[1] != 0:
    if a[0] > a[1]:
        a[0] %= a[1]
    else:
        a[1] %=  a[0]
print(a[0]+a[1])