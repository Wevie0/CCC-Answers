lines = int(input())
messages = [input().split(' ') for i in range(lines)]
tracker = []
sent = []
for i in range(len(messages)):
    if messages[i][0] == 'R':
        tracker.append([messages[i][1], 0])
    for j in range(len(tracker)):
        if messages[i][0] == 'S':
            if messages[i][1] == tracker[j][0]:
                sent.append(tracker[j])
                del tracker[j]
                tracker.insert(j, ['0', -50])
        if messages[i][0] == 'W':
            tracker[j][1] += int(messages[i][1]) - 1
        else:
            tracker[j][1] += 1


sent.sort()
for i in range(len(sent) - 1, -1, -1):
    if sent[i][0] == sent[i-1][0]:
        sent[i][1] += sent[i -1][1]
        del sent[i-1]
tracker = [row for row in tracker if '0' not in row[0]]
for i in range(len(sent)):
    for j in range(len(tracker)):
        if sent[i][0] == tracker[j][0]:
            sent[i][1] = -1
            del tracker[j]
            break
for i in range(len(tracker)):
    tracker[i][1] = -1
    sent.append(tracker[i])

sent.sort()

for row in sent:
    for cell in row:
        print(cell, end=' ')
    print()
