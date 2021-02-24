import sys

num = int(sys.stdin.readline())
rt = 0
gt = 0
bt = 0
for i in range(num):
    r, g, b = map(int, sys.stdin.readline().split())
    rt += r
    gt += g
    bt += b

rt = rt % 255
gt = gt % 255
bt = bt % 255

print(rt, gt, bt)