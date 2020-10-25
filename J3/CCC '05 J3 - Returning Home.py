# Canadian Computing Competition: 2005 Stage 1, Junior #3
#
# Jane's family has just moved to a new city and today is her first day of school.
# She has a list of instructions for walking from her home to the school.
# Each instruction describes a turn she must make. For example, the list

# R
# QUEEN
# R
# FOURTH
# R
# SCHOOL
#
# means that she must turn right onto Queen Street, then turn right onto Fourth Street,
# then finally turn right into the school.
# Your task is to write a computer program which will create instructions for walking in the opposite direction:
# from her school to her home.
#
# The input and output for your program will be formatted like the samples below.
# You may assume that Jane's list contains at least two but at most five instructions,
# and you may assume that each line contains at most 10 characters, all of them capital letters.
# The last instruction will always be a turn into the "SCHOOL".

direction = []
place = []
x = 0
direction.append(input())
place.append(input())

while place[x] != "SCHOOL":
    direction.append(input())
    place.append(input())
    x += 1

for j in range(len(direction)):
    if direction[j] == "R":
        del direction[j]
        direction.insert(j, "LEFT")
    elif direction[j] == "L":
        del direction[j]
        direction.insert(j, "RIGHT")
del place[-1]
place.reverse()
direction.reverse()
for k in range(len(direction)-1):
    print("Turn %s onto %s street." % (direction[k], place[k]))
print("Turn %s into your HOME." % direction[-1])
