from sys import stdin
from queue import PriorityQueue
from math import inf
houses, roads, dest, queries = map(int, stdin.readline().split())
g = [[] for i in range(houses)]
for i in range(roads):
    road = [int(j) for j in stdin.readline().split()]
    g[road[0] - 1].append((road[1] - 1, road[2]))
    g[road[1] - 1].append((road[0] - 1, road[2]))

dest -= 1
dist = [inf for i in range(houses)]
q = PriorityQueue()
q.put((0, dest))
dist[dest] = 0

while not q.empty():
    current = q.get()
    node = current[1]
    possible = g[node]
    for p in possible:
        weight = p[1]
        nextN = p[0]
        if dist[node] + weight < dist[nextN]:
            dist[nextN] = dist[node] + weight
            q.put((dist[nextN], nextN))

for i in range(queries):
    query = int(stdin.readline()) - 1
    print(dist[query] if dist[query] != inf else -1)
