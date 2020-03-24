m = int(input())
err = 0
ch1 = ch2 = ch3 = k = 0
c = ''
for i in range(m):
    s = input()
    while s[k] == '0':
        ch1 += 1
        if k+1 != len(s):
            k += 1
        else:
            err = -1
            break        
    while s[k] == '1':
        ch2 += 1
        if k+1 != len(s):
            k += 1
        else:
            err = -1
            break        
    while s[k] == '2':
        ch3 += 1
        if k+1 != len(s):
            k += 1
        else:
            err = -1
            break
    if ch1 == ch2 == ch3 and err == -1:
        c += 'YES'
    else:
        c += 'NO'
    c += '\n'
    ch1 = ch2 = ch3 = err = k = 0
if m != 0:
    print(c[:-1])