from queue import *
roads = []
g = [[] for i in range(26)]

trans = {

}
t = 0
while 1:
    line = list(input())
    if line[0] == '*':
        break
    roads.append(line)
    if line[0] not in trans:
        trans[line[0]] = t
        t += 1
    if line[1] not in trans:
        trans[line[1]] = t
        t += 1
    g[trans[line[0]]].append(trans[line[1]])
    g[trans[line[1]]].append(trans[line[0]])

g = [x for x in g if x != []]
ori = [x[:] for x in g]
num = len(roads)
connected = []
for i in roads:
    g = [x[:] for x in ori]
    x = trans[i[0]]
    y = trans[i[1]]
    q = Queue()
    q.put(trans['A'])
    g[x].remove(y)
    g[y].remove(x)
    visited = [False for i in range(len(g))]
    while not q.empty():
        cur = q.get()
        visited[cur] = True
        if cur == trans['B']:
            num -= 1
            connected.append(i)
            break
        for nxt in g[cur]:
            if not visited[nxt]:
                q.put(nxt)
output = [x for x in roads if x not in connected]
for i in output:
    print('%s%s' % (i[0], i[1]))
print("There are %d disconnecting roads." % num)