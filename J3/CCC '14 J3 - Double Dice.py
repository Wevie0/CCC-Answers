# Canadian Computing Competition: 2014 Stage 1, Junior #3
#
# Antonia and David are playing a game. Each player starts with 100 points.
#
# The game uses standard six-sided dice and is played in rounds. During one round, each player rolls one die.
# The player with the lower roll loses the number of points shown on the higher die.
# If both players roll the same number, no points are lost by either player.
#
# Write a program to determine the final scores.

# Input Specification
# The first line of input contains the integer n (1 ≤ n ≤ 15), which is the number of rounds that will be played.
# On each of the next n lines, will be two integers: the roll of Antonia for that round, followed by a space,
# followed by the roll of David for that round. Each roll will be an integer between 1 and 6 (inclusive).

# Output Specification
# The output will consist of two lines.
# On the first line, output the number of points that Antonia has after all rounds have been played.
# On the second line, output the number of points that David has after all rounds have been played.

antonia = 100
david = 100

rounds = int(input())
for i in range(rounds):
    roll = input().split()
    roll = list(map(int, roll))
    if roll[0] > roll[1]:
        david -= roll[0]
    elif roll[1] > roll[0]:
        antonia -= roll[1]
print(antonia)
print(david)
