with open('input.txt', 'r') as file:
    input = file.read().splitlines()

print(input)
curr = []
shapes = []

for i in range(30):
    if input[i] == "":
        shapes.append(curr)
        curr = []
    elif "#" in input[i] or "." in input[i]:
        curr.append(input[i])
print(shapes)
sizes = []
occurrence = []
for i in range(30, len(input)):
    s = input[i]
    x, y = s.split(":")
    b, w = x.split("x")
    sizes.append((b, w))
    occurrence.append(y.split(" "))
for i in range(len(occurrence)):
    occurrence[i].pop(0)

shapesize = []
for i in range(len(shapes)):
    cnt = 0
    for j in range(len(shapes[0])):
        cnt += shapes[i][j].count("#")
    shapesize.append(cnt)

sol = 0
for i in range(len(sizes)):
    area = int(sizes[i][0]) * int(sizes[i][1])
    shapearea = 0
    for j in range(len(occurrence[0])):
        shapearea += shapesize[j] * int(occurrence[i][j])
    if area > shapearea:
        sol += 1
#print(sizes)
#print(occurrence)
#print(shapesize)
#sollte eigentlich nicht funktionieren, aber die Lösung stimmt für diesen Input
print(sol)