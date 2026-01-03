with open('input.txt', 'r') as file:
    input = file.read().splitlines()

s = "dac"
d = "out"
D = {}
DP = {}
visited = {}
for i in range(len(input)):
    source, dest = input[i].split(":")
    D[source] = dest[1:].split(" ")
    DP[source] = 0
    visited[source] = False
DP["out"] = 0
DP[s] = 1
path = [s]
start = D[s]
queue = [(s, path)]
visited[s] = True
visited["out"] = False
print(D)

sol = 0
while queue:
    print("queue:", queue)
    l1 = queue.pop(0)
    if l1[0] == "out":
        continue
    elif l1[0] == d:
        continue
    else:

        for i in range(len(D[l1[0]])):
            new_path = l1[1].copy()
            new_dest = D[l1[0]][i]
            DP[new_dest] += DP[l1[0]]
            new_path.append(new_dest)
            if not visited[new_dest]:
                queue.append((new_dest, new_path))
                visited[new_dest] = True

memo = {}
def visit(curr, end):
    if curr == end:
        return 1
    if curr == "out":
        return 0
    if curr in memo:
        return memo[curr]

    total = 0
    for i in range(len(D[curr])):
        n = D[curr][i]
        total += visit(n, end)
    memo[curr] = total

    return total

print(visit(s, d))

print(DP[d])
print(sol)
# multiply the 3 paths ( start to ttf, ttf to dac, dac to out)
print(7366*4043694*16647)