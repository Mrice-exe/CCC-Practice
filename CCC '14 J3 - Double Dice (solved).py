times = int(input(""))
Antonia = 100
David = 100
for x in range(times):
  number = input("")
  if number[0] > number[2]:
    David -= int(number[0])
  elif number[0] < number[2]:
    Antonia -= int(number[2])
  else:
    continue

print(Antonia)
print(David)
