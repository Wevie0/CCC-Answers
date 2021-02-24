from sys import stdin
tot_mark = 0
initial = int(stdin.readline())
students = initial
for i in range(initial):
    tot_mark += int(stdin.readline())
transfers = int(stdin.readline())
for i in range(transfers):
    tot_mark += int(stdin.readline())
    students += 1
    print("%.3f" % (tot_mark/students))