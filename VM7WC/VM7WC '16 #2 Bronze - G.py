l1 = 'GGGGG'
l5 = 'GGGGG'

multiple = int(input())

for i in range(multiple):
    print(l1 * multiple)
for i in range(multiple):
    print('G' * multiple + '.' * 4 * multiple)
for i in range(multiple):
    print('G' * multiple + '.' * 2 * multiple + 'G' * 2 * multiple)
for i in range(multiple):
    print('G' * multiple + '.' * 3 * multiple + 'G' * 1 * multiple)
for i in range(multiple):
    print(l5 * multiple)