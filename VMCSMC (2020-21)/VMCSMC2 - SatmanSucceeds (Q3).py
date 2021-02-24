def isprime(a):
    print(a)
    if a == 0 or a == 1:
        return "No"
    for i in range(2,a):
        if counter % i == 0:
            return "No"
    return "Yes"

lower, upper = map(int, input().split())
counter = 0
for i in range(lower, upper+1):
    prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prime = False
            break
    if prime and i > 1:
        counter += 1

print(isprime(counter))

