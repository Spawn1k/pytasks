s = list(map(int, input().split()))
n = s[0]
x = s[1]
y = s[2]
l = 0
time = min(x,y)
r = (n-1)*max(x, y) + 1
m = 0
while (l + 1) < r:
        m = (r + l) // 2
        if m // x + m // y < n-1:
                l = m
        else:
                r = m
print(time+r)