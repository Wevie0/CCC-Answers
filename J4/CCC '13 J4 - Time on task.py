total = int(input())
chores = int(input())
counter = 0
time = sorted([int(input()) for i in range(chores)])
while total > 0:
    total -= time[0]
    del time[0]
    if total < 0:
        break
    else:
        counter += 1
print(counter)
