with open('input.txt', 'r') as file:
    ipt = file.read().splitlines()

input = []

for i in range(len(ipt)):
    input.append(list(ipt[i]))
DP = [[0 for x in range(len(input[0]))] for y in range(len(input))]
sol = 0
for x in range(len(input)):
    for y in range(len(input[0])):
        if input[x][y] == "S":
            input[x+1][y] = "|"
            DP[x+1][y] = 1
        elif input[x][y] == "|" and x != len(input)-1:
            lower = input[x+1][y]
            if lower == ".":
                input[x+1][y] = "|"
                DP[x+1][y] = DP[x][y] + DP[x+1][y]
            elif lower == "^":
                sol += 1
                input[x+1][y+1] = "|"
                input[x+1][y-1] = "|"
                DP[x+1][y+1] = DP[x][y] + DP[x+1][y+1]
                DP[x+1][y-1] = DP[x][y] + DP[x+1][y-1]
            elif lower == "|":
                DP[x + 1][y] = DP[x][y] + DP[x+1][y]

print(sol)
print(sum(DP[-1]))