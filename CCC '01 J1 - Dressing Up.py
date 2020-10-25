
# Canadian Computing Competition: 2001 Stage 1, Junior #1
#
# It is important to keep our computers safe and clean. Some people feel that computers should be well-dressed, also.
# For this question, you will write a program to print out a bow tie on the computer screen.
#
# Your program should take as input the height H of the bow tie,
# where H is an odd positive integer greater than or equal to 5.
# A bow tie with H rows (and 2H columns)
# should then be printed using the pattern shown below in the sample output.
# Input Specification
#
# One line containing integer H. You may assume that all input data will be valid.

# *        *
# ***    ***
# **********
# ***    ***
# *        *

height = int(input())
numspaces = 2 * height - 2
num = 1

for i in range(int(height/2)):
    print("*" * num + " " * numspaces + "*" * num)
    num += 2
    numspaces -= 4
print("*" * 2 * height)
for i in range(int(height/2)):
    num -= 2
    numspaces += 4
    print("*" * num + " " * numspaces + "*" * num)
