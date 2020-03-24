def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
sum1 = 0
sum2 = 0
p1 = 0
p2 = 0
a = list(input().split())
b = list(input().split())
ch1 = convert_base(int(a[0]), int(a[1]))
ch2 = convert_base(int(b[0]), int(b[1]))
for i in range(len(ch1)):
    if ch1[i].isdigit():
        p1 += int(ch1[i])
    else:
        p1 += int(convert_base(ch1[i], 10, int(a[1])))
for i in range(len(ch2)):
    if ch2[i].isdigit():
        p2 += int(ch2[i])
    else:
        p2 += int(convert_base(ch2[i], 10, int(b[1])))
if p1 == p2:
    print(p1)
else:
    print(0)