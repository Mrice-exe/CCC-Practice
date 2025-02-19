def new(line):
    num = 0
    string = ""
    skip = 0
    for i in range(len(line)):
        if i < skip:
            continue
        if line[i] in upper:
            string = (f"{string}{line[i]}")
        elif line[i] in lower:
            pass
        elif line[i] == "-":
            pass
        else:
            f = 1
            counter = 0
            current = (f"{line[i]}")
            while f == 1:
                counter += 1
                if i+counter < len(line):
                    if line[i+counter] not in lower and line[i+counter] not in upper and line[i+counter] != "-":
                        current = int(f"{current}{line[i+counter]}")
                    else:
                        f = 0 
                else:
                    f = 0
            skip = i+counter
            num += int(current)
    string = (f"{string}{num}")
    return string

string = "nihao"
lower = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
upper = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

reps = int(input())

for i in range(reps):
    line = input("")
    print(new(line))