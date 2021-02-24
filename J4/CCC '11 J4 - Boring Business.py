import sys
grid = [[0 for i in range(401)] for j in range(200)]
danger = False

x = int((len(grid[0]) - 1) * 0.5)
position = [4, x-1]  # y, x
grid[0][x] = 1
grid[1][x] = 1
grid[2][x] = 1
grid[2][x+1] = 1
grid[2][x+2] = 1
grid[2][x+3] = 1
grid[3][x+3] = 1
grid[4][x+3] = 1
grid[4][x+4] = 1
grid[4][x+5] = 1
grid[3][x+5] = 1
grid[2][x+5] = 1
grid[2][x+6] = 1
grid[2][x+7] = 1
grid[3][x+7] = 1
grid[4][x+7] = 1
grid[5][x+7] = 1
grid[6][x+7] = 1
grid[6][x+6] = 1
grid[6][x+5] = 1
grid[6][x+4] = 1
grid[6][x+3] = 1
grid[6][x+2] = 1
grid[6][x+1] = 1
grid[6][x+0] = 1
grid[6][x-1] = 1
grid[5][x-1] = 1
grid[4][x-1] = 1

while True:
    command = sys.stdin.readline().split()
    if command[0] == 'q':
        break
    elif command[0] == 'l':
        for i in range(int(command[1])):
            position[1] -= 1
            if grid[position[0]][position[1]] == 1:
                danger = True
            grid[position[0]][position[1]] = 1

    elif command[0] == 'r':
        for i in range(int(command[1])):
            position[1] += 1
            if grid[position[0]][position[1]] == 1:
                danger = True
            grid[position[0]][position[1]] = 1

    elif command[0] == 'u':
        for i in range(int(command[1])):
            position[0] -= 1
            if grid[position[0]][position[1]] == 1:
                danger = True
            grid[position[0]][position[1]] = 1

    elif command[0] == 'd':
        for i in range(int(command[1])):
            position[0] += 1
            if grid[position[0]][position[1]] == 1:
                danger = True
            grid[position[0]][position[1]] = 1
    if not danger:
        print("%s %s safe" % (position[1] - x, position[0] * -1 - 1))
    else:
        print("%s %s DANGER" % (position[1]-x, position[0] * -1 - 1))
        break
