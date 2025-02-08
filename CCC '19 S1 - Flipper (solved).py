flips = input("")
num = [1,2,3,4]
for x in flips:
  if x == "H":
    
    numtemp = [num[2],num[3],num[0],num[1]]
    num = numtemp
  if x == "V":
    numtemp = [num[1],num[0],num[3],num[2]]
    num = numtemp
  else:
    continue

print("""{0} {1}
{2} {3}""".format(num[0],num[1],num[2],num[3]))
