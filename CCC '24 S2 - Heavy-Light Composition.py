
letters = {
    
    
}
ans = []
rep = (input())
rep = int(rep[0])
for i in range(rep):
    string = input("")
    Heavy = False
    alr = False
    letters.clear()
    counter = -1
    for x in string:
        counter += 1
        if x not in letters:
            letters.update({x:1})
            Heavy = False
        else:
            letters[x] += 1
            if string[0] == x and counter == 1:
                print("yes")
                Heavy = True
            if Heavy == True and alr == False:
                ans.append("F")
                alr = True
                break
            elif Heavy == False:
                Heavy = True
                continue

    if alr == False:
        L = 2
        for i in string:
            if letters[i] == 1 and L == 1:
                ans.append("F")
                alr = True
                break
            elif letters[i] == 1:
                L = 1
            elif letters[i] > 1:
                L = 0
        if alr == False:            
            ans.append("T")
    
for y in ans:
    print(y)
