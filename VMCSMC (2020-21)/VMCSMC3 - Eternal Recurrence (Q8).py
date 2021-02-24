import sys
num = int(sys.stdin.readline())


def isPrime(x):
    for i in range (2, num):
        if x % i == 0:
            return False
    return True


def fib(n):
    x = 0
    y = 1
    for i in range(2, n+1):
        comb = x + y
        x = y
        y = comb
        if x > n:
            if isPrime(x):
                return x


if num == 2:
    print(3)
elif num == 3 or num == 4:
    print(5)
elif num == 5 or num == 6:
    print(13)
else:
    print(fib(num))
