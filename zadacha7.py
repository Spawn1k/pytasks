a = input()
b = int(a)
pr = 1
while b > 4:
    b -= 3
    pr *= 3
if b == 4:
    pr *= 4
elif b == 3:
    pr *= 3
elif b == 2:
    pr *= 2
print(pr)