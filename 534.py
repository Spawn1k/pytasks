
kl = int(input())
k = list(map(int, input().split()))
naj = int(input())
mas = list(map(int, input().split()))
for i in range(naj):
    k[mas[i]-1] -= 1
for i in range(kl):
    if k[i] < 0:
        print('yes')
    else:
        print('no')   