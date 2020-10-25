# Canadian Computing Competition: 2003 Stage 1, Junior #1
#
# A trident is a fork with three tines (prongs). A simple picture of a trident can be made from asterisks and spaces:
#
# *  *  *
# *  *  *
# *  *  *
# *******
#    *
#    *
#    *
#    *
#
# In this example, each tine is a vertical column of 3 asterisks.
# Each tine is separated by 2 spaces.
# The handle is a vertical column of 4 asterisks below the middle tine.
#
# Tridents of various shapes can be drawn by varying three parameters: t, the height of the tines,
# s, the spacing between tines, and h, the length of the handle.
# For the example above we have t = 3 , s = 2, and h = 4.
#
# You are to write an interactive program to print a trident.
# Your program should accept as input the parameters t, s, and h, and print the appropriate trident.
# You can assume that t, s, h are each at least 0 and not larger than 10.

tine = int(input())
space = int(input())
handle = int(input())

for i in range(tine):
    print("*" + (" "*space) + "*" + (" "*space) + "*")
print("*" * (2 * space + 3))
for i in range(handle):
    print(" " * (space + 1) + "*")

