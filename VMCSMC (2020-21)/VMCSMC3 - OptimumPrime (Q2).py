import sys

number = int(sys.stdin.readline())

i = 1
prime = True
def isPalindrome(x):
    reversed = x[::-1]
    for i in range(len(x)):
        if x[i] != reversed[i]:
            return False
    return True

def isPrime(y):
    for i in range(2, y):
        if y % i == 0:
            return False
    return True

while True:
    possible = number + i
    if isPalindrome(str(possible)):
        if isPrime(possible):
            print(possible)
            break
    i += 1