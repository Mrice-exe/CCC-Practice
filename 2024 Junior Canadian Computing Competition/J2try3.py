Dsize = int(input())
for x in range(8):
    monsize = (input(""))
    if monsize == (""):
        break
    else:
        monsizeint = int(monsize)
        if monsizeint >= Dsize:
            DsizeDef = Dsize
        else:
            Dsize += monsizeint
        

print(DsizeDef)