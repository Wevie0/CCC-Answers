# Canadian Computing Competition: 2002 Stage 1, Junior #1
#
#  _     _  _       _   _  _   _   _
# | | |  _| _| |_| |_  |_   | |_| |_|
# |_| | |_  _|   |  _| |_|  | |_|  _|
#
# Most digital devices show numbers using a seven segment display. The seven segments are arranged as shown:
#
#  * * *
# *     *
# *     *
# *     *
#  * * *
# *     *
# *     *
# *     *
#  * * *
#
# For this problem each segment is represented by three asterisks in a line as shown above.
#
# Any digit from 0 - 9 can be shown by illuminating the appropriate segments.
# For example the digit 1 may be displayed using the two segments on the right side:
#
#       *
#       *
#       *
#
#       *
#       *
#       *
#
# The digit 4 needs four segments to display it properly:

#
# *     *
# *     *
# *     *
#  * * *
#       *
#       *
#       *
#
# Write a program that will accept a single digit input from the user,
# and then display that digit using a seven segment display.
# You may assume that each segment is composed of three asterisks.
#
# DMOJ-specific note: None of your lines should contain any trailing whitespace.
# The last line must end with a newline.

digit = int(input())


# def horizontal():
#     print(" * * * "))
# 
# 
# def verticalboth():
#     print("*     *")
# 
# 
# def verticalright():
#     print("      *")
# 
# 
# def verticalleft():
#     print("*      "))
# 
# 
# def blank():
#     print("      "))
# 
# 
# if digit == 0 or digit == 1 or digit == 3 or digit == 4 or digit == 7 or digit == 8 or digit == 9:
#     if digit == 0 or digit == 3 or digit == 7 or digit == 8 or digit == 9:
#         horizontal()
#     for i in range(3):
#         if digit == 0 or digit == 4 or digit == 8 or digit == 9:
#             verticalboth()
#         else:
#             verticalright()
#     if digit == 0 or digit == 1 or digit == 7:
#         blank()
#     else:
#         horizontal()
#     for i in range(3):
#         if digit == 0 or digit == 8:
#             verticalboth()
#         else:
#             verticalright()
#     if digit == 0 or digit == 3 or digit == 8 or digit == 9:
#         horizontal()
# 
# else:
#     horizontal()
#     if digit == 2:
#         for i in range(3):
#             verticalright()
#     else:
#         for i in range(3):
#             verticalleft()
#     horizontal()
#     if digit == 2:
#         for i in range(3):
#             verticalleft()
#     elif digit == 5:
#         for i in range(3):
#             verticalright()
#     else:
#         for i in range(3):
#             verticalboth()
#     horizontal()

if digit == 0:
    print(" * * * ")
    print("*     *")
    print("*     *")
    print("*     *")
    print("       ")
    print("*     *")
    print("*     *")
    print("*     *")
    print(" * * * ")
    print(" ")
elif digit == 1:
    print("       ")
    print("      *")
    print("      *")
    print("      *")
    print("       ")
    print("      *")
    print("      *")
    print("      *")
    print("       ")
elif digit == 2 :
    print(" * * * ")
    print("      *")
    print("      *")
    print("      *")
    print(" * * * ")
    print("*      ")
    print("*      ")
    print("*      ")
    print(" * * * ")
elif digit == 3 :
    print(" * * * ")
    print("      *")
    print("      *")
    print("      *")
    print(" * * * ")
    print("      *")
    print("      *")
    print("      *")
    print(" * * * ")
elif digit == 4 :
    print("       ")
    print("*     *")
    print("*     *")
    print("*     *")
    print(" * * * ")
    print("      *")
    print("      *")
    print("      *")
    print("       ")
elif digit == 5 :
    print("* * * ")
    print("*      ")
    print("*      ")
    print("*      ")
    print(" * * * ")
    print("      *")
    print("      *")
    print("      *")
    print(" * * * ")
elif digit == 6 :
    print(" * * * ")
    print("*      ")
    print("*      ")
    print("*      ")
    print(" * * * ")
    print("*     *")
    print("*     *")
    print("*     *")
    print(" * * * ")
elif digit == 7 :
    print(" * * * ")
    print("      *")
    print("      *")
    print("      *")
    print("       ")
    print("      *")
    print("      *")
    print("      *")
    print("       ")
elif digit == 8 :
    print(" * * * ")
    print("*     *")
    print("*     *")
    print("*     *")
    print(" * * * ")
    print("*     *")
    print("*     *")
    print("*     *")
    print(" * * * ")
elif digit == 9 :
    print(" * * * ")
    print("*     *")
    print("*     *")
    print("*     *")
    print(" * * * ")
    print("      *")
    print("      *")
    print("      *")
    print(" * * * ")
