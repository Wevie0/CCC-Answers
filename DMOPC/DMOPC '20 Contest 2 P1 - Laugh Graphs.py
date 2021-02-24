import sys
n = int(sys.stdin.readline())
commands = list(input())
col = 4005
row = n
arr = [['.' for i in range(row)] for j in range(col)]
position = [2000, 0]  # pos 0 is y
for i in commands:
    if i == 'v':
        position[0] += 1
        arr[position[0]][position[1]] = '\\'
        position[1] += 1
    elif i == '^':
        arr[position[0]][position[1]] = '/'
        position[0] -= 1
        position[1] += 1
    elif i == '>':
        arr[position[0]][position[1]] = '_'
        position[1] += 1

for i in arr:
    if col == 2:
        print("".join(arr[0]))
        break
    elif '_' in i or '\\' in i or '/' in i:
        print("".join(i))