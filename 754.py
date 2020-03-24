a = list(map(int, input().split()))
err = 0
for i in a:
  if i < 94 or i > 727:
    print('Error')
    err = 1
    break
if err == 0:
  print(max(a))