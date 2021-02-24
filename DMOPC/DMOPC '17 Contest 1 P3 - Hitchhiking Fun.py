from sys import stdin
from queue import PriorityQueue
from math import inf

dest, roads = map(int, stdin.readline().split())
g = []
for i in range(max(dest, roads + 2)):
    g.append([])
dest -= 1
for i in range(roads):
    road = [int(j) for j in stdin.readline().split()]
    g[road[0] - 1].append((road[1] - 1, road[2]))
    g[road[1] - 1].append((road[0] - 1, road[2]))

dist = [inf for i in range(len(g))]
q = PriorityQueue()
q.put((0, 0, 0))
current = []
dist[0] = 0
paths = []


while not q.empty():
    current = q.get()
    node = current[1]
    possible = g[node]
    if current[1] == dest:
        paths.append([current[0], current[2]])
    for p in possible:
        weight = p[1]
        nextN = p[0]
        if dist[node] + weight < dist[nextN]:
            dist[nextN] = dist[node] + weight
            q.put((dist[nextN], nextN, current[2] + 1))

if dist[dest] != inf:
    z = min(paths[0])
    output = []
    for i in range(len(paths)):
        if paths[i][0] == z:
            output.append(paths[i][1])
    print(dist[dest], min(output))
else:
    print(-1)