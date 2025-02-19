
donuts = int(input())

reps = int(input())

for i in range(reps):
    string = input("")
    if string == "+":
        num = int(input(""))
        donuts += num
    elif string == "-":
        num = int(input(""))
        donuts -= num

print(donuts)