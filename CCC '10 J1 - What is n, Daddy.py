# Canadian Computing Competition: 2010 Stage 1, Junior #1
#
# Natalie is learning to count on her fingers. When her Daddy tells her a number n ( 1 ≤ n ≤ 10 ),
# she asks "What is n, Daddy?",
# by which she means "How many fingers should I hold up on each hand so that the total is n?"
#
# To make matters simple, her Daddy gives her the correct finger representation according to the following rules:
#
#     the number may be represented on one or two hands;
#     if the number is represented on two hands, the larger number is given first.
#
# For example, if Natalie asks "What is 4 , Daddy?", her Dad may reply:
#
#
# 5 is 5
# 5 is 4 and 1
# 5 is 3 and 2
# 3
#

# Your job is to make sure that Natalie's Daddy gives the correct number of answers.

n = int(input())

counter = 0
hand = [n, 0]
while True:
    if hand[0] <= 5 or hand[1] <= 5:
        counter += 1
    hand[0] -= 1
    hand[1] += 1
    if hand[0] < hand[1]:
        break
print(counter)





