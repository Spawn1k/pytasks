a = input()
n = 0
if a[len(a) - 1] == '0':
    k = len(a) - 1
    while a[k] == '0':
        n += 1
        k -= 1
    print('1'+'0'*n)
else:
    print(1)