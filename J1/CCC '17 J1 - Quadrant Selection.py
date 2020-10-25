# A common problem in mathematics is to determine which quadrant a given point lies in.
# There are four quadrants, numbered from 1 to 4
#
# For example, the point A , which is at coordinates (12, 5),
# lies in quadrant 1 since both its x and y values are positive,
#
# Your job is to take a point and determine the quadrant it is in.
# You can assume that neither of the two coordinates will be 0 .

# Input Specification
# The first line of input contains the integer x  ( − 1 000 ≤ x ≤ 1 000 ; x ≠ 0 ).
# The second line of input contains the integer y ( − 1 000 ≤ y ≤ 1 000 ; y ≠ 0 ).
#
# Output Specification
# Output the quadrant number ( 1 , 2 , 3 or 4 ) for the point (x,y).

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 < y:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")




