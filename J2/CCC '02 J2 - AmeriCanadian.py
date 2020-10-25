# Canadian Computing Competition: 2002 Stage 1, Junior #2
#
# Americans spell differently from Canadians.
# Americans write neighbor and color while Canadians write neighbour and colour.
# Write a program to help Americans translate to Canadian.
#
# Your program should interact with the user in the following way.
# The user should type a word (not to exceed 64 letters) and if the word appears to use American spelling,
# the program should echo the Canadian spelling for the same word. If the word does not appear to use American spelling,
# it should be output without change. When the user types quit! the program should terminate.
#
# The rules for detecting American spelling are quite naive:
# If the word has more than four letters and has a suffix consisting of a consonant followed by or,
# you may assume it is an American spelling, and that the equivalent Canadian spelling replaces the or by our.
# Note : you should treat the letter y as a vowel.

while True:
    word = input()
    if word == "quit!":
        break
    if len(word) >= 4:
        american = word[len(word)-2:]
        index = word.index(american)
        index -= 1
        if word[index] == "a" or word[index] == "e" or word[index] == "i" or word[index] == "o" or word[index] == "u" or word[index] == "y":
            print(word)
        else:
            word = word.replace("or", "our")
            print(word)
    else:
        print(word)
