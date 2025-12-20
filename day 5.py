with open('input.txt', 'r') as file:
    input = file.read().splitlines()

idx = input.index("")
ranges = input[:idx]
ids = input[idx+1:]

sol = 0
all = []
for j in range(len(ranges)):
    fst, sec = ranges[j].split("-")
    fst, sec = int(fst), int(sec)
    all.append((fst, sec))

print()
change = -1
i = 0
while i < len(all):
    change = 0
    fst = all[i][0]
    sec = all[i][1]
    for p in range(len(all)):
        if p == i:
            continue
        if all[p][0] <= fst <= all[p][1] or all[p][0] <= sec <= all[p][1]:
            print(i, p)
            all[i] = (min(fst, all[p][0]), max(sec, all[p][1]))
            all.remove(all[p])
            change += 1
            break
    if change == 0:
        i += 1
    else:
        i = 0

sol = 0
for i in range(len(all)):
    sol += all[i][1] - all[i][0] + 1
print(sol)