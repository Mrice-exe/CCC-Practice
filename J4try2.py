def count(line):
    scount = 0 
    temp = 0
    for i in range(len(line)):
        if line[i] == "S":
            temp += 1
        if line[i] == "P" or i+1 >= len(line):
            if temp > scount:
                scount = temp
            temp = 0
            
    return scount
def bruteforce(line):
    temp = []
    temp.append(line)
    temp = temp[0]
    highscore = 0 
    highscoretemp = 0
    for i in range(len(line)):
        if line[i] == "P":
            temp[i] = "S"
            highscoretemp = count(temp)
            if highscoretemp > highscore:
                highscore = highscoretemp
            highscoretemp = 0
            temp[i] = "P"
            
    
    return highscore
            
reps = int(input())
line = []

for i in range(reps):
    pors = input("")
    line.append(pors)

if "P" not in line:
    print(len(line)-1)
else:
    print(bruteforce(line))