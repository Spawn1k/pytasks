import sys
num = input()
l = len(num)
st = '0'
if l == 4:
    s = int(num[:2])
    k = int(num[2:])
    if k > s:
        print(0)
        sys.exit()
    s -= 9
    if k > 9:
        k -= 9
        st = '9' + str(s) + '9' + str(k)
    else:
        print(0)
        sys.exit()
if l == 3:
    s = int(num[:2])
    k = int(num[2:])
    s -= 9
    st = '9' + str(s) + str(k) + '0'
if l == 2:
    s = int(num[0])
    k = int(num[1])
    if k > s:
        print(0)
        sys.exit()
    st = str(s)+'0'+str(k)+'0'
if len(st) <= 4:
    print(st)
else:
    print(0)