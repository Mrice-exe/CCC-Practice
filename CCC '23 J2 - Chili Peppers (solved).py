spicyness = 0
chilinum = int(input())
for x in range(chilinum):
  chilitype = input("")
  if chilitype == "Poblano":
    spicyness += 1500
  elif chilitype == "Mirasol":
    spicyness += 6000
  elif chilitype == "Serrano":
    spicyness += 15500
  elif chilitype == "Cayenne":
    spicyness += 40000
  elif chilitype == "Thai":
    spicyness += 75000
  elif chilitype == "Habanero":
    spicyness += 125000
print(spicyness)
