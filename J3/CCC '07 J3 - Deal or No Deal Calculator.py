# Canadian Computing Competition: 2007 Stage 1, Junior #3
#
# In the CCC version of the game, there are 10 possible dollar amounts:
# $ 100, $ 500, $ 1 000, $ 5 000, $ 10 000, $ 25 000 , $ 50 000, $ 100 000, $ 500 000, $ 1 000 000
# sealed in imaginary briefcases. These dollar amounts are numbered 1 − 10
# (i.e. 1 → $ 100, 2 → $ 500, 3 → $ 1 000, ..., 10 → $ 1 000 000).
# Before the game starts the contestant will have chosen one of the briefcases as his/hers to possibly keep.
# During the game, some of the ten possible dollar amounts have been eliminated from the game
# because the contestant has selected some of the other briefcases and revealed the amounts inside.
#
# At some point, the contestant will stop opening briefcases,
# and a "Banker" will offer the contestant cash in exchange for what might be contained in his/her chosen briefcase.
# Then the contestant is asked: "Deal or No Deal?".
#
# Write a program that helps a player decide if he/she should choose "deal" or "no deal",
# by calculating the average of the remaining amounts
# (i.e., all unopened briefcases, including his/her "own" briefcase),
# and comparing that value to the "Banker's" offer. If the offer is higher than the average,
# then the player should "deal" otherwise, the player should say "no deal".

# Input Specification
# The user must input a number n ( 1 ≤ n < 10) which indicates how many cases have been opened so far,
# followed by a list of integers between 1 and 10 representing the values in the game that have been eliminated,
# followed by the "Banker's" offer. For example: 3, 2, 5, 10, 300 indicates that
# briefcases containing $ 500, $ 10 000, and $ 1 000 000 have been eliminated and the Banker's offer is $ 300.
# You may assume that no duplicate case numbers are entered for the eliminated values,
# and you may assume that the "Banker's" offer is an integer greater than 10.

# Output Specification
# The program will print out one of two statements: deal or no deal.

values = {
    "1": 100, "2": 500, "3": 1000, "4": 5000, "5": 10000, "6": 25000, "7": 50000, "8": 100000, "9": 500000,
    "10": 1000000}
total = 1691600
numOpened = int(input())
opened = []
left = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
leftSum = 0
for i in range(numOpened):
    opened.append(input())
offer = int(input())
for i in range(len(opened)):
    total -= values[opened[i]]
    for j in range(len(left)):
        if opened[i] == left[j]:
            del left[j]
            break
if total/len(left) < offer:
    print("deal")
else:
    print("no deal")

# cases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
# newc = cases.copy()
#
# num = int(input())
# for i in range(num):
#     index = int(input()) - 1
#     item = cases[index]
#     newc.remove(item)
# avg = sum(newc)/len(newc)
#
# offer = int(input())
# if offer>avg:
#     print('deal')
# else:
#     print('no deal')
