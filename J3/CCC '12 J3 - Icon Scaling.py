# Canadian Computing Competition: 2012 Stage 1, Junior #3
#
# You have been asked to take a small icon that appears on the screen of a smart telephone and scale it up
# so it looks bigger on a regular computer screen.
#
# The icon will be encoded as characters (x and *) in a 3×3 grid as follows:
#
#   *x*
#    xx
#   * *
#
# Write a program that accepts a positive integer scaling factor and outputs the scaled icon. A scaling factor of k
# means that each character is replaced by a k×k grid consisting only of that character.

# Input Specification
# The input will be a positive integer k such that k < 25.

# Output Specification
# The output will be 3k lines, which represent each individual line scaled by a factor of k and repeated k times.
# A line is scaled by a factor of k by replacing each character in the line with k copies of the character.

scale = int(input())

for i in range(scale):
    print("*" * scale + "x" * scale + "*" * scale)
for i in range(scale):
    print(" " * scale + "x" * scale + "x" * scale)
for i in range(scale):
    print("*" * scale + " " * scale + "*" * scale)
