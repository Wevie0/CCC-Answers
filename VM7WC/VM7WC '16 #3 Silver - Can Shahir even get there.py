import queue
import sys
info = sys.stdin.readline().split()
g = [[] for i in range(int(info[0]))]
print(g)
for i in range(int(info[1])):
    x, y = map(int, sys.stdin.readline().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)
    print(g)
start = int(info[2])
dest = int(info[3])

q = queue.Queue()
q.put(start-1)

visited = [False for i in range(len(g))]
found = False

while not q.empty():
    if start == dest:
        found = True
        break
    c = q.get()
    visited[c] = True
    for nxt in g[c]:
        if not visited[nxt]:
            q.put(nxt)
    if c == dest-1:
        found = True
        break
print("GO SHAHIR!" if found else "NO SHAHIR!")
