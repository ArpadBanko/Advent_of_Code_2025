with open('input.txt', 'r') as file:
    input = file.read().splitlines()

op = input[-1]
input.pop()

operations = [x for x in op]
for i in range(len(input)):
    input[i] += "        "
for i in range(10):
    operations.append(" ")

sol = 1
mul = operations[0]
total = 0
for i in range(len(input[0])):
    if operations[i] != " ":
        mul = operations[i]
    s = ""
    for j in range(len(input)):
        if input[j][i] != " ":
            s += input[j][i]
    if s != "":
        if mul == "*":
            sol *= int(s)
        elif mul == "+":
            sol += int(s)
    else:
        if sol != 1:
            total += sol
            if mul == "+":
                total -= 1
        sol = 1


print(total)

