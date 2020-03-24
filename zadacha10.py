a = list(map(int, input().split()))
b, c = a[0], a[1]
while b != c:
    if b > c:
        b -= c
    else:
        c -= b
print(int(a[0]*a[1]/b))