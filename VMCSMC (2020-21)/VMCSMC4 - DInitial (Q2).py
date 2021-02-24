from sys import stdin
t = int(stdin.readline())
g = [[] for i in range(t)]
visited = [[False for j in range(t)]for k in range(t)]
for i in range(t):
    g[i] = list(input())
position = [0, 0]
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == 'S':
            position = [i, j]
output = 0
def search(y, x):
    global output
    visited[y][x] = True
    if g[y][x] == 'E':
        output = 1

    if y > 0 and g[y-1][x] != '#' and visited[y-1][x] == False:
        search(y-1, x)
    if y < t - 1 and g[y+1][x] != '#' and visited[y+1][x] == False:
        search(y+1, x)
    if x < t - 1 and g[y][x+1] != '#' and visited[y][x+1] == False:
        search(y, x+1)
    if x > 0 and g[y][x-1] != '#' and visited[y][x-1] == False:
        search(y, x-1)

search(position[0], position[1])
print(output)