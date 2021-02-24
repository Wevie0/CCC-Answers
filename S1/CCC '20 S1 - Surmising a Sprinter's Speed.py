num = int(input())
data = []
speeds = []
for i in range(num):
    data.append([int(x) for x in input().split()])
data.sort()
for i in range(len(data)-1):
    speeds.append(abs(data[i+1][1]-data[i][1])/(data[i+1][0]-data[i][0]))

print(max(speeds))