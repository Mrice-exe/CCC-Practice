number = 91

for x in range(1,3+1):
    add = int(input())
    if x % 2 == 1:
        number += add
    if x % 2 == 0:
        number += add*3
print(f"The 1-3-sum is {number}")
