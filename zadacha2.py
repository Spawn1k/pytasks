a=input()
s=''
b=list(map(int, a.split()))
for i in range (-100,101):
    if b[0]*i**3+b[1]*i**2+b[2]*i+b[3] == 0:
        s += str(i)+' '
print(s)
