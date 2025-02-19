def another(string):
    charnum = []
    counter = 1
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            counter += 1
        else:
            charnum.append(f"{counter} {string[i-1]}")
            counter = 1
    charnum.append(f"{counter} {string[-1]} ")
    return " ".join(charnum)



reps = int(input())
lines = []
charnum = []
for i in range(reps):
    temp = input("")
    lines.append(temp)

for line in lines:
    print(another(line))
