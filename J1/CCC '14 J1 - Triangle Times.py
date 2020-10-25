'''
Canadian Computing Competition: 2014 Stage 1, Junior #1

You have trouble remembering which type of triangle is which. You write a program to help. Your program reads in three angles (in degrees).

    If all three angles are 60, output Equilateral.
    If the three angles add up to 180 and exactly two of the angles are the same, output Isosceles.
    If the three angles add up to 180 and no two angles are the same, output Scalene.
    If the three angles do not add up to 180, output Error.

Input Specification

The input consists of three integers, each on a separate line. Each integer will be greater than 0 and less than 180.
Output Specification

Exactly one of Equilateral, Isosceles, Scalene or Error will be printed on one line.
'''

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

if angle1 == 60 and angle2 == 60 and angle3 == 60:
    print("Equilateral")
elif angle1 + angle2 + angle3 == 180 and (angle1 == angle2 or angle2 == angle3 or angle1 == angle3):
    print("Isosceles")
elif angle1 + angle2 + angle3 != 180:
    print("Error")
else:
    print("Scalene")