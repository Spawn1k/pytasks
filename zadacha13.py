k = int(input())
result = []
for i in range(k):
    a = list(map(int, input().split()))
    n = a[0]
    m = a[1]
    d = int(19*m + (n+239) * (n+366)/2)
    a.clear()
    result.append(d)
print(*result, sep = '\n')