# Canadian Computing Competition: 2020 Stage 1, Junior #2
#
# People who study epidemiology use models to analyze the spread of disease. In this problem, we use a simple model.
#
# When a person has a disease, they infect exactly R other people but only on the very next day.
# No person is infected more than once. We want to determine when a total of more than P people have had the disease.
#
# Input Specification
# There are three lines of input. Each line contains one positive integer. The first line contains the value of P .
# The second line contains N , the number of people who have the disease on Day 0 .
# The third line contains the value of R . Assume that P ≤ 10^7 and N ≤ P  and R ≤ 10.

# Output Specification
# Output the number of the first day on which the total number of people who have had the disease is greater than P.

# p = int(input())
# n = int(input())
# r = int(input())
# subtotal = 0
# total = n
# counter = 0
# c = r
# one = False
#
# while total <= p:
#     if n == 0 == r:
#         break
#     elif n == 1 == r:
#         print(p)
#         one = True
#         break
#     subtotal = n * c
#     c *= r
#     total += subtotal
#     counter += 1
# if not one:
#     print(counter)

# p = int(input())
# n = int(input())
# r = int(input())
# tot = n
# ans = 0
# while tot <= p:
#     n *= r
#     tot += n
#     print(n)
#     ans += 1
# print(ans)

# magicNum = int(input())
# init = int(input())
# tot = init
# rate = int(input())
#
# if rate == init == 1:
#     print(magicNum)
# else:
#     i = 1
#     while tot <= magicNum:
#         tot += init*(rate)**i
#         i += 1
#     print(i - 1)

