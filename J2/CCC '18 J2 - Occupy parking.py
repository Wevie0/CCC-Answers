# Canadian Computing Competition: 2018 Stage 1, Junior #2
#
# You supervise a small parking lot which has N parking spaces.
#
# Yesterday, you recorded which parking spaces were occupied by cars and which were empty.
#
# Today, you recorded the same information.
#
# How many of the parking spaces were occupied both yesterday and today?

# Input Specification
# The first line of input contains the integer N ( 1 ≤ N ≤ 100 ).
# The second and third lines of input contain N characters each.
# The second line of input records the information about yesterday's parking spaces,
# and the third line of input records the information about today's parking spaces.
# Each of these 2N characters will either be C to indicate an occupied space
# or . to indicate it was an empty parking space.

# Output Specification
# Output the number of parking spaces which were occupied yesterday and today.

numSpaces = int(input())
yesterday = input()
today = input()
counter = 0

for i in range(numSpaces):
    if yesterday[i] == "C" and today[i] == "C":
        counter += 1
print(counter)
