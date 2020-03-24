s = input()
s += ' '
err = 0
l = 0
pseudo = 0
c = [0, 1]
d = [0, 1]
if s[0].isdigit():
    print('NO')
    err = 1
if s[0].islower():
    print('NO')
    err = 1
if err == 0:
    for i in range(1, len(s)):
        if s[i-1].isupper() and s[i].islower():
            c.append(s[i-1:i+1])
            l += 1
            d.append(s[i-1:i+1])
            pseudo += 1
        if c[l] == c[l+1]:
            print('NO')
            err = 1
            break
        if s[i-1].isupper() and s[i].isdigit():
            d.append(s[i-1])
            pseudo += 1
        if s[i].isupper() and s[i-1].isdigit() and not s[i+1].islower():
            d.append(s[i])
            pseudo += 1
        if d[pseudo] == d[pseudo+1]:
            print('NO')
            err = 1
            break
        if i != len(s)-1:
            if s[i] == s[i-1] and not s[i+1].islower() and not s[i].isdigit():
                print('NO')
                err = 1
                break
        else:
            if s[i] == s[i-1]:
                print('NO')
                err = 1
                break
        if s[i].islower() and s[i-1].islower():
            print('NO')
            err = 1
            break
        if s[i].islower() and s[i-1].isdigit():
            print('NO')
            err = 1
            break
        if i != len(s) - 1:
            if s[i].isdigit() and not s[i+1].isdigit():
                if int(s[i]) == 1:
                    print('NO')
                    err = 1
                    break
        if s[i].isupper() and s[i-1].isupper():
            l += 1
            c.append(str(i))
            d.append(str(i))
            pseudo += 1
        if s[i].isdigit() and s[i-1].isupper():
            c.append(str(i))
            l+=1
        if s[i].isdigit() and not s[i-1].isdigit():
            if int(s[i]) == 0:
                print('NO')
                err = 1
                break
if err == 0:
    print('YES')