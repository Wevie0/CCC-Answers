from sys import stdin

def factors(n):
    div = 2
    out = []
    while div ** 2 <= n:
        if n % div == 1:
            div += 1
        else:
            n //= div
            out.append(div)
    if n > 1:
        out.append(n)
    return out

n = int(stdin.readline())
list = set(factors(n))
prod = 1
for i in list:
    prod *= i
print(prod)