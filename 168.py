s = [str(x) for x in range(1, 10001)]
string = ''.join(s)
n = input()
print(string.find(n)+1)