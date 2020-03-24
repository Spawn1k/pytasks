s = list(input().split())
coeff = 1
n = int(s[0])
pr = n
k = len(s[1])
if n % k == 0 and k < n:
    while n != coeff*k:
        pr = pr * (n - coeff*k)
        coeff += 1
    print(pr)
elif k < n:
    while n - coeff*k != n % k:
        pr = pr * (n - coeff*k)
        coeff += 1
    print(pr)
else:
    print(n)