from sys import stdin
from math import ceil

cases = int(stdin.readline())


def prime(n):
    for i in range(2, ceil(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(cases):
    pri = int(stdin.readline())
    pri *= 2
    for j in range(2, pri):
        if j + pri - j == pri:
            if prime(j) and prime(pri - j):
                print(j, pri - j)
                break
