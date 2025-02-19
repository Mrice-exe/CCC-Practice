def check(grid):
    starting = 0 
    count = 0 
    lowest = 99999999
    for x in range(row):
        for i in range(len(grid)):
            count += grid[i][x]
        if count < lowest:
            lowest = count
            count = 0 
    return lowest
        
row = int(input())
column = int(input())
maxi = int(input())

grid = []
temp = []
for i in range(row*column):
    
    if i != 0 and i%row == 0:
        grid.append(temp)
        temp = []
        temp.append(i%maxi+1)
    else:
        temp.append(i%maxi+1)
grid.append(temp)
    
print(check(grid))