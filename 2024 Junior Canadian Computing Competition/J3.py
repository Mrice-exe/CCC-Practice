def quicksort(scorelist):
    if len(scorelist) <= 1:
        return scorelist
    else:
        pivot = scorelist[0]
        left = [x for x in scorelist[1:] if x < pivot]
        right = [x for x in scorelist[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

peoplenum = int(input())
scorelist = []

for x in range(peoplenum):
    score = int(input())
    scorelist.append(score)


sortedlist = quicksort(scorelist)

first = sortedlist[len(sortedlist)-1]


firstlist = [x for x in sortedlist if x == first]
firstammount = len(firstlist)

secondfinder = firstammount + 1

second = sortedlist[len(sortedlist)-secondfinder]


secondlist = [x for x in sortedlist if x == second]

secondammount = len(secondlist)
thirdfinder = secondammount + firstammount + 1
third = sortedlist[len(sortedlist)-thirdfinder]
thirdlist = [x for x in sortedlist if x == third]
thirdammount = len(thirdlist)

print(third,thirdammount)