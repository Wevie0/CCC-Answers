# Canadian Computing Competition: 2004 Stage 1, Junior #3
#
# A simile is a combination of an adjective and noun that produces a phrase such as "Easy as pie" or "Cold as ice".
#
# Write a program to input n adjectives ( 1 ≤ n ≤ 5 )and m nouns ( 1 ≤ m ≤ 5 ), and print out all possible similes.
# The first two lines of input will provide the values of n and m, in that order followed,
# one per line, by n adjectives and m nouns.
#
# Your program may output the similes in any order.

n = int(input())
m = int(input())
adjectives = []
nouns = []

for i in range(n):
    adjective = input()
    adjectives.append(adjective)
for j in range(m):
    noun = input()
    nouns.append(noun)

for i in range(len(adjectives)):
    for j in range(len(nouns)):
        print("%s as %s" % (adjectives[i], nouns[j]))
