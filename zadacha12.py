n = int(input())
a = list(map(int, input().split()))
m = int(input())
mas = list()
s = 0
for i in range(m):
    pair = list(map(int, input().split()))
    for j in range(pair[0]-1, pair[1]):
        s += a[j]
    mas.append(s)
    s = 0
    pair.clear()
print(*mas)