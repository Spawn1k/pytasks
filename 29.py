n = int(input())
y = list(map(int, input().split()))
energy = 0
for i in range(2, len(y)):
    energy += min(abs(3*(y[i] - y[i-2])), abs(y[i] - y[i-1]) + abs(y[i-1] - y[i-2]))
print(energy)