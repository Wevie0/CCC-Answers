# CCC '00 J1 - Calendar
# Canadian Computing Competition: 2000 Stage 1, Junior #1
#
# Write a program to print out a calendar for a particular month
# given the day on which the first of the month occurs together with the number of days in the month.
#
# Your program should take as input an integer representing the day of the week on which the month begins
# (1 for Sunday, 2 for Monday, … , 7 for Saturday),
# and an integer which is the number of days in the month (between 28 and 31 inclusive).
# Your program should print the appropriate calendar for the month. You can assume that all input data will be valid.
#
# DMOJ-specific note: None of the output lines should contain trailing whitespace.
# The last line must end with a newline.


info = input()
info = info.split()
start = int(info[0])
days = int(info[1])
week1 = []
week2 = []
week3 = []
week4 = []
week5 = []
week6 = []
counter = 1;

while counter <= 7-(start-1):
    week1.append(counter)
    counter += 1
while counter <= 7 + 7-(start-1):
    week2.append(counter)
    counter += 1

while counter <= 14 + 7-(start-1):
    week3.append(counter)
    counter += 1

while counter <= 21 + 7-(start-1):
    week4.append(counter)
    counter += 1

while counter <= 28 + 7-(start-1):
    if counter > days:
        break
    else:
        week5.append(counter)
        counter += 1

while counter <= 35 + 7-(start-1):
    if counter > days:
        break
    else:
        week6.append(counter)
        counter += 1

print("Sun Mon Tue Wed Thr Fri Sat")
print("   " * (start-1) + (" " * (start - 2)), end="")
for i in range(len(week1)):
    if i == 0 and start == 1:
        print("  " + str(week1[0]), end="")
    else:
        print("   " + str(week1[i]), end="")
print("")
for i in range(len(week2)):
    if i == 0:
        print("  " + str(week2[0]), end="")
    elif i > 0 and week2[i] < 10:
        print("   " + str(week2[i]), end="")
    else:
        print("  " + str(week2[i]), end="")
print("")
for i in range(len(week3)):
    if i == 0 and week3[i] > 9:
        print(" " + str(week3[0]), end="")
    elif i == 0 and week3[i] < 10:
        print("  " + str(week3[0]), end="")
    else:
        print("  " + str(week3[i]), end="")
print("")
for i in range(len(week4)):
    if i == 0:
        print(" " + str(week4[0]), end="")
    else:
        print("  " + str(week4[i]), end="")
print("")
for i in range(len(week5)):
    if i == 0:
        print(" " + str(week5[0]), end="")
    else:
        print("  " + str(week5[i]), end="")
print("")
if week6:
    for i in range(len(week6)):
        if i == 0:
            print(" " + str(week6[0]), end="")
        else:
            print("  " + str(week6[i]), end="")
print("\n")


