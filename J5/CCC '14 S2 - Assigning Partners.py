num = int(input())
a = input().split()
b = input().split()
output = "good"
for i in range(num):
    pair1 = [a[i], b[i]]
    first = pair1[0]
    index = b.index(first)
    pair2 = [a[index], b[index]]
    pair2.reverse()
    if pair1[0] == pair1[1] or pair2[0] == pair2[1]:
        output = "bad"
    elif pair2 != pair1:
        output = "bad"
print(output)