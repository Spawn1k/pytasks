import sys
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False
fin = open('INPUT.TXT')
a = fin.readline()
zn = -1
if a == '' or a == '\n':
    print('ERROR')
    sys.exit()
osh = a.find(' ')
if osh != -1:
    print('ERROR')
    sys.exit()
ravn = a.find('=')
if zn == -1:
    zn = a.find('-')
    if zn == 0:
        zn = a.find('-', 1)
    if (a[zn-1] == '+') or (a[zn-1] == '*') or (a[zn-1] == '/') or (a[zn-1] == '='):
        zn = -1
    else:
        state = 2
if zn == -1:
    zn = a.find('+')
    state = 1
if zn == -1:
    zn = a.find('*')
    state = 3
if zn == -1:
    zn = a.find('/')
    state = 4
if zn == -1:
    print('ERROR')
    sys.exit()
if (zn + 1 == ravn) or (zn == 0) or (ravn < zn):
    print('ERROR')
    sys.exit()
ch1 = a[0:zn]
ch2 = a[zn+1:ravn]
ch3 = a[ravn+1:]
if is_digit(ch1) and ch1[0] != '+':
    ch1 = int(ch1)
else:
    print('ERROR')
    sys.exit()
if is_digit(ch2) and ch2[0] != '+':
    ch2 = int(ch2)
else:
    print('ERROR')
    sys.exit()
if is_digit(ch3) and ch3[0] != '+':
    ch3 = int(ch3)
else:
    print('ERROR')
    sys.exit()
if state == 1:
    if ch1 + ch2 == ch3:
        print('YES')
    else:
        print('NO')
if state == 2:
    if ch1 - ch2 == ch3:
        print('YES')
    else:
        print('NO')
if state == 3:
    if ch1 * ch2 == ch3:
        print('YES')
    else:
        print('NO')
if state == 4 and ch2 != 0:
    if ch1 / ch2 == ch3:
        print('YES')
    else:
        print('NO')
elif state == 4 and ch2 == 0:
    print('NO')