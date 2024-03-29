# Canadian Computing Competition: 2018 Stage 1, Junior #1
#
# Here at the Concerned Citizens of Commerce (CCC),
# we have noted that telemarketers like to use seven-digit phone numbers
# where the last four digits have three properties. Looking just at the last four digits, these properties are:
#
#     the first of these four digits is an 8 or 9 ;
#     the last digit is an 8 or 9 ;
#     the second and third digits are the same.
#
# For example, if the last four digits of the telephone number are 8229, 8338, or 9008, these are telemarketer numbers.
#
# Write a program to decide if a telephone number is a telemarketer number or not,
# based on the last four digits. If the number is not a telemarketer number, we should answer the phone,
# and otherwise, we should ignore it.

# Input Specification
# The input will be a 4 lines where each line contains exactly one digit in the range from 0 to 9 .

# Output Specification
# Output either ignore if the number matches the pattern for a telemarketer number; otherwise, output answer.

digit1 = int(input())
digit2 = int(input())
digit3 = int(input())
digit4 = int(input())

if (digit1 == 8 or digit1 == 9) and (digit4 == 8 or digit4 == 9) and (digit2 == digit3):
    print("ignore")
else:
    print("answer")
