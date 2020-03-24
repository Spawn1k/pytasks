import sys
s = input()
if len(s) != 5:
    print('ERROR')
    sys.exit()
if s[2] != '-':
    print('ERROR')
    sys.exit()
if not s[0].isupper() or not s[3].isupper():
    print('ERROR')
    sys.exit()
if ord(s[0]) < 65 or ord(s[0]) > 72:
    print('ERROR')
    sys.exit()
if ord(s[3]) < 65 or ord(s[3]) > 72:
    print('ERROR')
    sys.exit()
if not s[1].isdigit() or not s[4].isdigit():
    print('ERROR')
    sys.exit()
if int(s[1]) > 8 or int(s[4]) > 8:
    print('ERROR')
    sys.exit()
if int(s[1]) < 1 or int(s[4]) < 1:
    print('ERROR')
    sys.exit()
if abs(int(s[1]) - int(s[4])) != 2 and abs(int(s[1]) - int(s[4])) != 1:
    print('NO')
    sys.exit()
if abs(int(s[1]) - int(s[4])) == 2:
    if chr(ord(s[0]) - 1) != s[3] and chr(ord(s[0]) + 1) != s[3]:
        print('NO')
        sys.exit()
    else: 
        print('YES')
if abs(int(s[1]) - int(s[4])) == 1:
       if chr(ord(s[0]) - 2) != s[3] and chr(ord(s[0]) + 2) != s[3]:
           print('NO')
           sys.exit()
       else: 
           print('YES')