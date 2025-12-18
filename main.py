with open('input.txt', 'r') as file:
    input = file.read().splitlines()
def select(curr: list, k: int, s: str, start: int):
    if k == 0:
        first = max(curr[start:])
        index = curr[start:].index(first)
    else:
        first = max(curr[start:-k])
        index = curr[start:-k].index(first)
    s += str(first)
    if len(s) == 12:
        return s
    else:
        return select(curr, k-1, s, start+index+1)

sol = 0
for i in range(len(input)):
    curr1 = list(input[i])
    curr = list(map(int, curr1))
    my_str = select(curr, 11, "", 0)
    sol += int(my_str)
print(sol)
