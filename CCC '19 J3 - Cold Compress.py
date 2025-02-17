def another(string,char):
    if len(string) < 1:
        return 2
    else:
        if char == string[0]:
            return 1, string[1:]
        else:
            return 0, string[1:]
reps = int(input)
strings = []

for i in range(reps):
    temp = input("")
    length = len(temp)
    counter = -1
    for x in temp:
        counter += 1
        current = x
        if temp[counter+1] == x:
            pass
