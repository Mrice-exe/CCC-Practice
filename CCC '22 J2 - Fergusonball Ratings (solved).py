playernum = int(input(""))
def checkgold(point,foul):
  if point*5 - foul*3 > 40:
    return True
  else: 
    return False

goldnumber = 0
for x in range(playernum):
  ppoint = int(input(""))
  pfoul = int(input(""))
  playergold = checkgold(ppoint,pfoul)
  if playergold == True:
    goldnumber += 1
  else: 
    continue
if goldnumber == playernum:
  print("{}+".format(goldnumber))
else:
  print(goldnumber)
