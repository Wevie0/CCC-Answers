def move(y, x, treasure):
    if y == 0 and x == 7:
        output.append(treasure)
        return
    if g[y][x] != '.':
        treasure += int(g[y][x])
    if y != 0:
        if g[y - 1][x] != '#':
            move(y - 1, x, treasure)
    if x != 7:
        if g[y][x + 1] != '#':
            move(y, x + 1, treasure)

for i in range(5):
    if i > 0:
        seperator = input()
    g = [[None for i in range(8)] for j in range(8)]
    pos = [7, 0]
    output = []
    for i in range(8):
        g[i] = list(input())
    move(pos[0], pos[1], 0)
    print(max(output))
