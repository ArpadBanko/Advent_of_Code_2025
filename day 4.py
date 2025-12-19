with open('input.txt', 'r') as file:
    ipt = file.read().splitlines()

input = []
for i in range(len(ipt)):
    input.append(list(ipt[i]))

def check(l1: list, x: int, y:int):
    count = 0
    if l1[x][y] == ".":
        return False
    else:
        if x != 0:
            if l1[x-1][y] == "@":
                count += 1
            if y != 0:
                if l1[x-1][y-1] == "@":
                    count += 1
        if y != 0:
            if l1[x][y-1] == "@":
                count += 1
            if x != len(l1)-1:
                if l1[x+1][y-1] == "@":
                    count += 1
        if x != len(l1)-1:
            if l1[x+1][y] == "@":
                count += 1
        if y != len(l1[0])-1:
            if l1[x][y+1] == "@":
                count += 1
            if x != 0:
                if l1[x-1][y+1] == "@":
                    count += 1
            if x != len(l1)-1:
                if l1[x+1][y+1] == "@":
                    count += 1
        return count < 4

total = 0
changes = -1
while changes != 0:
    changes = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if check(input, i, j):
                changes += 1
                input[i][j] = '.'
    total += changes
print(total)
