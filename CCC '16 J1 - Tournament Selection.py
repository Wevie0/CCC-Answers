# Each player in a tournament plays six games.
# There are no ties. The tournament director places the players in groups based on the results of games as follows:
#
#     if a player wins 5 or 6 games, they are placed in Group 1;
#     if a player wins 3 or 4 games, they are placed in Group 2;
#     if a player wins 1 or 2 games, they are placed in Group 3;
#     if a player does not win any games, they are eliminated from the tournament.
#
# Write a program to determine which group a player is placed in.

# Input Specification
# The input consists of six lines, each with one of two possible letters: W or L.

# Output Specification
# The output will be either 1, 2, 3 (to indicate which Group the player should be placed in)
# or -1 (to indicate the player has been eliminated).

score = 0
for i in range(6):
    result = input()
    if result == "W":
        score += 1

if score > 4:
    print("1")
elif score > 2:
    print("2")
elif score > 0:
    print("3")
else:
    print("-1")







