# Canadian Computing Competition: 2014 Stage 1, Junior #2
#
# A vote is held after singer A and singer B compete in the final round of a singing competition.
# Your job is to count the votes and determine the outcome.

# Input Specification
# The input will be two lines. The first line will contain V ( 1 ≤ V ≤ 15 ), the total number of votes.
# The second line of input will be a sequence of V characters, each of which will be A or B,
# representing the votes for a particular singer.

# Output Specification
# The output will be one of three possibilities:
#
#     A, if there are more A votes than B votes;
#     B, if there are more B votes than A votes;
#     Tie, if there are an equal number of A votes and B votes.


votes = int(input())
allVotes = input()
aVote = allVotes.count("A")
bVote = allVotes.count("B")
# for i in range(votes):
#     if allVotes[i] == "A":
#         aVote += 1
#     else:
#         bVote += 1
if aVote > bVote:
    print("A")
elif bVote > aVote:
    print("B")
else:
    print("Tie")

