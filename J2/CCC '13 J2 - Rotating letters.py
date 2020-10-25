# Canadian Computing Competition: 2013 Stage 1, Junior #2
#
# An artist wants to construct a sign whose letters will rotate freely in the breeze.
# In order to do this, she must only use letters that are not changed by rotation of 180 degrees:
# I, O, S, H, Z, X, and N.
#
# Write a program that reads a word and determines whether the word can be used on the sign.

# Input Specification
# The input will consist of one word, all in uppercase letters, with no spaces.
# The maximum length of the word will be 30 letters, and the word will have at least one letter in it.
# Output Specification
#
# Output YES if the input word can be used on the sign; otherwise, output NO.

rotatable = True
word = list(input())
for i in range(len(word)):
    if word[i] != "I" and word[i] != "O" and word[i] != "S" and word[i] != "H" and word[i] != "Z" and word[i] != "X"\
            and word[i] != "N":
        rotatable = False

if rotatable:
    print("YES")
else:
    print("NO")