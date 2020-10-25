# A palindrome is a word which is the same when read forwards as it is when read backwards.
# For example, mom and anna are two palindromes.
#
# A word which has just one letter, such as a, is also a palindrome.
#
# Given a word, what is the longest palindrome that is contained in the word?
# That is, what is the longest palindrome that we can obtain,
# if we are allowed to delete characters from the beginning and/or the end of the string?

# Input Specification
# The input will consist of one line, containing a sequence of at least 1 and at most 40 lowercase letters.
# Output Specification
# Output the total number of letters of the longest palindrome contained in the input word.

word = input()
length = []


def palindrome(x):
    if x == x[::-1]:
        return len(x)
    else:
        return 0


for i in range(len(word)):
    # from 0 to length of the word
    for j in range(i, len(word)):
        # from 0 to the length of the word
        length.append(palindrome(word[i:j+1]))
        # j increases, which increases length of string, then i increases which moves the start 1
print(max(length))
