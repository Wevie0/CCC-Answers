# Magic Squares are square arrays of numbers that have the interesting property that the numbers in each column,
# and in each row, all add up to the same total.
#
# Given a 4 × 4 square of numbers, determine if it is magic square.

# Input Specification
# The input consists of four lines, each line having 4 space-separated integers.

# Output Specification
# Output either magic if the input is a magic square, or not magic if the input is not a magic square.
sum = [0, 0, 0, 0, 0, 0, 0, 0]

line1 = input()
line2 = input()
line3 = input()
line4 = input()

line1 = line1.split()
line2 = line2.split()
line3 = line3.split()
line4 = line4.split()
k = 1
for i in range(4):
    sum[0] += int(line1[i])
    sum[1] += int(line2[i])
    sum[2] += int(line3[i])
    sum[3] += int(line4[i])
sum[4] += (int(line1[0]) + int(line2[0]) + int(line3[0]) + int(line4[0]))
sum[5] += (int(line1[1]) + int(line2[1]) + int(line3[1]) + int(line4[1]))
sum[6] += (int(line1[2]) + int(line2[2]) + int(line3[2]) + int(line4[2]))
sum[7] += (int(line1[3]) + int(line2[3]) + int(line3[3]) + int(line4[3]))

if sum[0] == sum[1] == sum[2] == sum[3] == sum[4] == sum[5] == sum[6] == sum[7]:
    print("magic")
else:
    print("not magic")


