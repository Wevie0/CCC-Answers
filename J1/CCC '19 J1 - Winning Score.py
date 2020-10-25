# You record all of the scoring activity at a basketball game.
# Points are scored by a 3 -point shot, a 2 -point field goal, or a 1 -point free throw.
#
# You know the number of each of these types of scoring for the two teams: the Apples and the Bananas.
# Your job is to determine which team won, or if the game ended in a tie.

# Input Specification
# The first three lines of input describe the scoring of the Apples,
# and the next three lines of input describe the scoring of the Bananas.
# For each team, the first line contains the number of successful 3 -point shots,
# the second line contains the number of successful 2 -point field goals,
# and the third line contains the number of successful 1 -point free throws.
# Each number will be an integer between 0 and 100 , inclusive.

# Output Specification
# The output will be a single character.
# If the Apples scored more points than the Bananas, output A.
# If the Bananas scored more points than the Apples, output B. Otherwise, output T, to indicate a tie.

appleThree = int(input())
appleTwo = int(input())
appleOne = int(input())

bananaThree = int(input())
bananaTwo = int(input())
bananaOne = int(input())

appleTotal = appleThree * 3 + appleTwo * 2 + appleOne
bananaTotal = bananaThree * 3 + bananaTwo * 2 + bananaOne

if appleTotal > bananaTotal:
    print("A")
elif bananaTotal > appleTotal:
    print("B")
else:
    print("T")
