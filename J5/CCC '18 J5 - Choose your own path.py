import queue
import pprint
pages = int(input())
g = [[] for i in range(pages + 1)]
for i in range(pages):
    line = list(map(int, input().split()))
    if line[0] != 0:
        del line[0]
        for j in range(len(line)):
            g[i].append(line[j] - 1)
    else:
        g[i].append(pages)
        g[pages].append(i)


visited = [False for i in range(len(g))]
q = queue.Queue()
q.put((0, 0))
output = ['N', 0]
flag = False
while not q.empty():
    current = q.get()
    visited[current[0]] = True
    for nxt in g[current[0]]:
        if not visited[nxt]:
            q.put((nxt, current[1] + 1))
    if current[0] == pages and not flag:
        output[1] = current[1]
        flag = True


if all(visited):
    output[0] = 'Y'
print(output[0])
print(output[1])
