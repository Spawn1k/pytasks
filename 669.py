import sys
a = int(input())
b = a
s = ''
st = ''
err = 0
while a > 1:
    for i in reversed(range(2,10)):
        if a % i == 0:
            s += str(i)
            a /= i
            err = 0
            break
    if err == -1:
        print(-1, -1)
        sys.exit()
    err = -1
s = s[::-1] + ' '
l = len(s)
while b > 1:
    for i in range(2,10):
        if b % i == 0:
            st += str(i)
            b /= i
            err = 0
            break
    err = -1
st = st[::-1]
s += st
print(s)