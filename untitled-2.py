a=str(input())
b=str(input())
t=a
s=1
i=0
while a!=b:
    z=a[-1::]
    a=a[:-1]
    a=z+a
    if t==a:
        s=0
        break
    i+=1
if s==0:
    print(-1)
else:
    print(i)