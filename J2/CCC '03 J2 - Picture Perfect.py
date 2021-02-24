# Canadian Computing Competition: 2003 Stage 1, Junior #2
#
# Roy has a stack of student yearbook photos.
# He wants to lay the pictures on a flat surface edge-to-edge to form a filled rectangle with minimum perimeter.
# All photos must be fully visible. Each picture is a square with dimensions 1 unit by 1 unit.
#
# For example, he would place 12 photos in the following configuration, where each photo is indicated with an X.
#
# XXXX
# XXXX
# XXXX
#
# Of course, he could orient them in the other direction, such as
#
# XXX
# XXX
# XXX
# XXX
#
# which would have the same perimeter, 14 units.
#
# Your program should repeatedly read a positive integer C,
# the number of pictures to be laid out. For each input,
# it should print the smallest possible perimeter for a filled rectangle that is formed by
# laying all the pictures edge-to-edge. Also print the dimensions of this rectangle.
#
# You may assume that there are less than 65 000 photos.
# An input value of C = 0 indicates that the program should terminate.

# def factors(n):
#     out = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             out.append(i)
#     return out
#
# while True:
#     inp = int(input())
#     if inp == 0:
#         break
#     factor = factors(inp)
#     mini = []
#     out = [9999, 0, 0]
#     for i in range(len(factor) // 2 + 1):
#         l = factor[i]
#         w = inp//factor[i]
#         mini.append([l, w])
#     for i in mini:
#         peri = 2 * i[0] + 2 * i[1]
#         if peri < out[0]:
#             out[0] = peri
#             out[1] = i[0]
#             out[2] = i[1]
#     print("Minimum perimeter is %d with dimensions %d x %d" % (out[0], out[1], out[2]))

import math

area = int(input())

while (area != 0):
    k = round(math.sqrt(area))
    while (area % k) != 0:
        k = k - 1
    print("Minimum perimeter is " + str((k + (round(area / k))) * 2) + " with dimensions " + str(k) + " x " + str(
        round(area / k)))
    area = int(input())

while area == 0:
    break
