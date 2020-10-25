# a = 0
# b, c, d, e = map(int, input().split())
# c += b
# d += c
# e += d
# print(a, b, c, d, e)
# a += b
# c -= b
# d -= b
# e -= b
# b = 0
# print(a, b, c, d, e)
# a += c
# b += c
# d -= c
# e -= c
# c = 0
# print(a, b, c, d, e)
# a += d
# b += d
# c += d
# e -= d
# d = 0
# print(a, b, c, d, e)
# a += e
# b += e
# c += e
# d += e
# e = 0
# print(a, b, c, d, e)


distances = map(int, input().split())
positions = [0]
for i in distances: positions.append(positions[-1] + i)

for i in range(5):
    for j in range(5):
        print(f"{abs(positions[i] - positions[j])} ", end="")
    print()
