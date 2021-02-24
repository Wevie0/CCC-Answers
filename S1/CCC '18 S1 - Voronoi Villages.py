from sys import stdin
from math import inf
v = []

villages = int(stdin.readline())
dist = [inf for i in range(villages)]
for i in range(villages):
    v.append(int(stdin.readline()))
v.sort()
for i in range(1, len(v)-1):
    dist[i] = (abs(v[i] - v[i-1]))/2 + (abs(v[i] - v[i+1]))/2
print("%.1f" % min(dist))