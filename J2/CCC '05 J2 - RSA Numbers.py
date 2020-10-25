# Canadian Computing Competition: 2005 Stage 1, Junior #2
#
# When a credit card number is sent through the Internet it must be protected so that other people cannot see it.
# Many web browsers use a protection based on "RSA Numbers."
#
# A number is an RSA number if it has exactly four divisors. In
# other words, there are exactly four numbers that divide into it evenly.
# For example, 10 is an RSA number because it has exactly four divisors (1, 2, 5, 10).
# 12 is not an RSA number because it has too many divisors(1, 2, 3, 4, 6, 12).
# 11 is not an RSA number either. There is only one RSA number in the range 10 … 12.
#
# Write a program that inputs a range of numbers and then counts how many numbers from that range are RSA numbers.
# You may assume that the numbers in the range are less than 1000.


rangeStart = int(input())
rangeEnd = int(input())
counter = 0
rsa = 0
for i in range(rangeStart, rangeEnd+1):
    for j in range(1, rangeEnd+1):
        if i % j == 0:
            counter += 1
    if counter == 4:
        rsa += 1
        counter = 0
    else:
        counter = 0

print("The number of RSA numbers between %d and %d is %d" % (rangeStart, rangeEnd, rsa))
