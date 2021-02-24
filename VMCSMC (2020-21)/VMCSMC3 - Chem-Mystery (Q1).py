import queue
mem = {}
lines = int(input())
g = [[] for i in range(30)]
for j in range(lines):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

test = []
for i in g:
    if i != []:
        test.append(i)

starts = []

for i in test:
    for j in i:
        if j not in starts:
            starts.append(j)

dests = starts
max = 0
for start in starts:
    for dest in dests:
        q = queue.Queue()
        q.put((start, 0))
        visited = [False for i in range(len(g))]
        while not q.empty():
            c = q.get()
            visited[c[0]] = True
            if c[0] == dest:
                if c[1] > max:
                    max = c[1]
                break
            for nxt in g[c[0]]:
                if not visited[nxt]:
                    q.put((nxt, c[1]+1))
print(str(max) + '-otone')