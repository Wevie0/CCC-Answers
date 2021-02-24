# motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
# import sys
#
# mini = int(sys.stdin.readline())
# maxi = int(sys.stdin.readline())
# new = int(sys.stdin.readline())
# for i in range(new):
#     motels.append(int(sys.stdin.readline()))
#
# motels.sort()
# ways = [0 for i in range(len(motels))]
#
# for i in range(len(motels)):
#     if mini <= motels[i] <= maxi:
#         ways[i] = 1
#
# for i in range(len(motels) - 1):
#     if ways[i] > 0:
#         for j in range(i + 1, len(motels)):
#             if mini <= motels[j] - motels[i] <= maxi:
#                 ways[j] = ways[j] + ways[i]
# print(ways[-1])

motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
from sys import stdin

counter = 0


def recur(d):
    global counter
    if d == 7000:
        counter += 1
        return
    for newD in motels:
        if mini <= newD - d <= maxi:
            recur(newD)


mini = int(stdin.readline())
maxi = int(stdin.readline())
num = int(stdin.readline())
for i in range(num):
    motels.append(int(stdin.readline()))
motels.sort()
recur(0)
print(counter)
