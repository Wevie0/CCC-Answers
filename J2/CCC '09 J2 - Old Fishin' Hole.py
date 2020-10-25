# Canadian Computing Competition: 2009 Stage 1, Junior #2
#
# Fishing habitat and fish species are a resource that must be carefully managed.
# Accordingly, fishing limits have been established for a particular river based on the population of each species.
# Specifically, points are associated with the fish caught
# and the total points you catch must be less than or equal to the points allowed for that river.
#
# As an example, suppose each brown trout counts as 2 points,
# each northern pike counts as 5 points and each yellow pickerel counts as 2 points,
# and the total points allowed must be less than or equal to 12 .
# One acceptable catch could consist of 3 brown trout and 1 northern pike, but other combinations would also be allowed.
#
# Your job is to write a program to input the points allocated for a river,
# and find how many different ways an angler who catches at least one fish can stay within his/her limit.

# Input Description
# You will be given 4 integers, one per line,
# representing trout points, pike points, pickerel points, and total points allowed in that order.
#
# You can assume that each integer will be greater than 0 and less than or equal to 100.

# Output Description
# For each different combination of fish caught,
# output the combination of brown trout, northern pike, and yellow pickerel in that order.
# The combinations may be listed in any order.
# The last line of output should display the total number of unique ways to catch fish within the established limit.

troutPoints = int(input())
pikePoints = int(input())
pickerelPoints = int(input())
totalPoints = int(input())

ways = 0

for k in range(int(totalPoints/pickerelPoints + 1)):
    for j in range(int(totalPoints/pikePoints + 1)):
        for i in range(int(totalPoints/troutPoints + 1)):
            if (i > 0 or j > 0 or k > 0) and (i * troutPoints + j * pikePoints + k * pickerelPoints) <= totalPoints:
                ways += 1
                print("%d Brown Trout, %d Northern Pike, %d Yellow Pickerel" % (i, j, k))
print("Number of ways to catch fish: %d" % ways)
