

def is_sequence(arr):
    valid = True
    change = arr[0] - arr[1]
    for i in range(len(arr)-1):
        if arr[i] - arr[i+1] != change:
            valid = False
    return arr if valid else None


import sys
length = int(sys.stdin.readline())
intervals = length // 720

length = length % 720

hours = 12
mins = 00
counter = 0
counter += (31 * intervals)
while True:
    mins = "%02d" % mins
    hours = "%02d" % hours
    if int(hours) >= 10:
        x = is_sequence([int(hours[0]), int(hours[1]), int(mins[0]), int(mins[1])])
    else:
        x = is_sequence([int(hours), int(mins[0]), int(mins[1])])
    if x is not None:
        counter += 1
    mins = int(mins)
    hours = int(hours)
    if length > 0:
        length -= 1
        mins += 1
    else:
        break
    
    if mins > 60:
        hours += 1
        if hours > 12:
            hours -= 12
        if hours == 12:
            break
        mins -= 60
print(counter)


# def is_arithmetic(x):
#     diff = x[1] - x[0]
#     for i in range (len(x) - 1):
#         if (x[i + 1] - x[i] != diff):
#             return False
#     return True

# t = int(input())
# count = 0
# starttime = 1200
# if (t >= 720):
#     count = 31 * (t // 720)
# for i in range (0, t % 720):
#     starttime += 1
#     if (is_arithmetic([int(i) for i in str(starttime)])):
#         count+=1
#     if ((starttime % 100) >= 60):
#         starttime += 40
#     if (starttime >= 1300):
#         starttime -= 1200
# print (count)
