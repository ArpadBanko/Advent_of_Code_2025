from functools import cmp_to_key

with open('input.txt', 'r') as file:
    input = file.read().splitlines()



coord = []
for i in range(len(input)):
    x, y, z = input[i].split(",")
    coord.append((int(x), int(y), int(z)))

def comparator(a,b):
    return a[2] - b[2]


def kruskals_mst(V, edges):
    edges = sorted(edges, key=cmp_to_key(comparator))
    dsu = DSU(V)
    cost = 0
    count = 0
    last_x = 0
    last_y = 0
    for x, y, w in edges:
        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
            cost += w
            count += 1
            last_x = x
            last_y = y

    return last_x, last_y

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1


edges = []
for i in range(len(coord)):
    for j in range(i+1, len(coord)):
        dist = ((coord[i][0] - coord[j][0])**2 + (coord[i][1] - coord[j][1])**2 + (coord[i][2] - coord[j][2])**2)
        edges.append([i, j, dist])
idx1, idx2 = kruskals_mst(len(edges)-1, edges)
print(coord[idx1][0] * coord[idx2][0])
