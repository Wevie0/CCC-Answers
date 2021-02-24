weight = int(input())
cars = int(input())
bridge = []
counter = 0
for i in range(cars):
    bridge.append(int(input()))
    counter += 1
    if len(bridge) > 4:
        del bridge[0]
    if sum(bridge) > weight:
        counter -= 1
        break

print(counter)