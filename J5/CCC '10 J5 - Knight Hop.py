board = [[10 for i in range(8)] for j in range(8)]

pos = [0, 0]
pos[0], pos[1] = map(int, input().split())
pos[0] -= 1
pos[1] = 8 - pos[1]

dest = [0, 0]
dest[0], dest[1] = map(int, input().split())
dest[0] -= 1
dest[1] = 8 - dest[1]

def move(y, x, moves):
    if moves < board[y][x]:
        board[y][x] = moves
        if x < 6 and y > 0 and board[y-1][x+2] != 0:  # right 2 up 1
            move(y-1, x+2, moves+1)
        if x < 6 and y < 7 and board[y+1][x+2] != 0:  # right 2 down 1
            move(y+1, x+2, moves+1)
        if x > 1 and y > 0 and board[y-1][x-2] != 0:  # left 2 up 1
            move(y-1, x-2, moves+1)
        if x > 1 and y < 7 and board[y+1][x-2] != 0:  # left 2 down 1
            move(y+1, x-2, moves+1)
        if y > 1 and x > 0 and board[y-2][x-1] != 0:  # up 2 left 1
            move(y-2, x-1, moves+1)
        if y > 1 and x < 7 and board[y-2][x+1] != 0:  # up 2 right 1
            move(y-2, x+1, moves+1)
        if y < 6 and x > 0 and board[y+2][x-1] != 0:  # down 2 left 1
            move(y+2, x-1, moves+1)
        if y < 6 and x < 7 and board[y+2][x+1] != 0:  # down 2 right 1
            move(y+2, x+1, moves+1)


move(pos[1], pos[0], 0)
print(board[dest[1]][dest[0]])
