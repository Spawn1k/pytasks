n = int(input())
number = 0
men = -1
result = 0
for i in range(n):
    a = list(map(int, input().split()))
    number += 1
    if a[0] > men and a[1] == 1:
        result = number
        men = a[0]
    a = []
if result == 0:
    print(-1)
else:
    print(result)