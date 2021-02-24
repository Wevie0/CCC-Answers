from sys import stdin

num = int(stdin.readline())
all_x = []
all_y = []
for i in range(num):
    x, y = map(int, stdin.readline().split())
    all_x.append(x)
    all_y.append(y)

len_x = abs(max(all_x) - min(all_x))
len_y = abs(max(all_y) - min(all_y))

print(len_x * len_y)