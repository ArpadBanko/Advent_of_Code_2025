from shapely import Polygon
with open('example.txt', 'r') as file:
    input = file.read().splitlines()

pairs = []

for i in range(len(input)):
    x, y = input[i].split(",")
    pairs.append((int(x), int(y)))

#print(pairs)

area = 0
polygon = Polygon(pairs)
for i in range(len(pairs)):
    for j in range(i+1, len(pairs)):
        first = pairs[i]
        sec = pairs[j]
        edges = [first, (first[0], sec[1]), sec, (sec[0], first[1])]
        current_poly = Polygon(edges)
        if polygon.covers(current_poly):
            curr = (abs(first[0]-sec[0])+1) * (abs(first[1]-sec[1])+1)
            if curr > area:
                area = curr


print(polygon.area)
print(area)


