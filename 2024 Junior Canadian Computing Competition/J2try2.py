Dsize = int(input())
monsizes = []
for x in range(8):
    monsize = (input(""))
    if monsize == (""):
        break
    else:
        monsizeint = int(monsize)
        monsizes.append(monsizeint)
def find(Dsize,monsizes):
    for x in (monsizes):
        if x >= Dsize:
            return Dsize
            break
        else:
            Dsize += x
    return Dsize
        
ans = find(Dsize,monsizes)
print(ans)