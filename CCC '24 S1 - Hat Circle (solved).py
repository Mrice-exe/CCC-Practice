N = int(input(""))
hatarr = []
acrossnum = 0
for x in range(N):
  hatarrtemp = input("")
  hatarr.append(hatarrtemp)

half = N//2
for x in range(half):
  num = x
  if hatarr[num] == hatarr[half+num]:
    acrossnum+=1
  else:
    continue
print(acrossnum*2)
