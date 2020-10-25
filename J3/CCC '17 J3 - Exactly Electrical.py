x, y = map(int, input().split())
x2, y2 = map(int, input().split())
charge = int(input())

distance = abs(x-x2) + abs(y-y2)

print("Y" if distance <= charge and (charge - distance) % 2 == 0 else "N")



