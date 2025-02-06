Dsize = int(input())
monsizes = []
for x in range(7):
    monsize = int(input())
    monsizes.append(monsize)
def find(Dsize,monsizes):
    for x in (monsizes):
        if x >= Dsize:
            return Dsize
        else:
            Dsize += x
    return Dsize
        
ans = find(Dsize,monsizes)
print(ans)