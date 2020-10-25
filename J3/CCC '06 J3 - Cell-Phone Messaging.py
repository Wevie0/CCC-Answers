# Canadian Computing Competition: 2006 Stage 1, Junior #3
#
# Joe Coder has just received a cell phone for his birthday. At first he was not so excited about it,
# since he does not like to talk that much, nor listen for that matter,
# and he hates being interrupted by phone calls while coding or playing his favourite computer game.
# But, Joe learned that he can talk to his friends and also send e-mails. That made the phone cool.
#
# In order to fit the 26 letters of the alphabet onto the keys of a cell phone,
# several letters are assigned to each key, as shown on the diagram.
# To write a text message, we have to choose a letter from a set assigned to a key.
# The first letter on a key is chosen by pressing the key once, the second letter by pressing the key twice,
# third letter by pressing the key three times, and so on.
#
# For example, to write a we press the key 2 once and we are done;
# to write dada we press 3232—four key presses; and to write bob we press 2266622.
#
# An obvious issue is how to write two consecutive letters on the same key, for example in abba or cell.
# The problem is solved by introducing a time-out feature:
# a letter currently displayed is chosen when another key is pressed, but also after a pause, i.e., a time out.
# Hence for example, to write abba we press 2-pause-22-pause-22-pause-2;
# to write cell we press 22233555-pause-555; or to write www we press 9-pause-9-pause-9.
#
# This kind of typing takes some time,
# and Joe is working on a program to calculate how much time is needed to type certain words.
# His assumption is that he spends one second per press,
# and whenever he makes a pause he loses an additional two seconds.
# You are to help him to calculate the minimal time needed to type a message, under the above assumptions.

# Input
# Each line of input contains a word consisting only of lowercase letters. Words have at most 20 characters.
# Input will be given from the keyboard, and the program should stop reading input when the word halt has been entered.

# Output
# For each input word (excluding the word halt), print (on the screen)
# the minimal number of seconds needed to type in the word, with one number of output per line.

timeDict = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1, 'h': 2, 'i': 3, 'j': 1, 'k': 2, 'l': 3, 'm': 1,
            'n': 2, 'o': 3, 'p': 1, 'q': 2, 'r': 3, 's': 4, 't': 1, 'u': 2, 'v': 3, 'w': 1, 'x': 2, 'y': 3, 'z': 4}
keypad = {
    "a": 2, "b": 2, "c": 2, "d": 3, "e": 3, "f": 3, "g": 4, "h": 4, "i": 4,
    "j": 5, "k": 5, "l": 5, "m": 6, "n": 6, "o": 6, "p": 7, "q": 7, "r": 7,
    "s": 7, "t": 8, "u": 8, "v": 8, "w": 9, "x": 9, "y": 9, "z": 9}
temp = []

word = ""
while word != ["h", "a", "l", "t"]:
    word = list(input())
    time = 0
    temp = 0
    if word == ["h", "a", "l", "t"]:
        break
    for i in word:
        time += timeDict[i]
        if keypad[i] == temp:
            time += 2
        temp = keypad[i]
    print(time)

# secs = []
# while 1:
#     text = input()
#     if text == 'halt':
#         break
#     s = 0
#     n = ''
#     for i in text:
#         if i in 'a d g j m p t w'.split(' '):
#             s += 1
#         elif i in 'b e h k n q u x'.split(' '):
#             s += 2
#         elif i in 'c f i l o r v y'.split(' '):
#             s += 3
#         else:
#             s += 4
#         if i in 'a b c'.split(' ') and n in 'a b c'.split(' '):
#             s += 2
#         elif i in 'd e f'.split(' ') and n in 'd e f'.split(' '):
#             s += 2
#         elif i in 'g h i'.split(' ') and n in 'g h i'.split(' '):
#             s += 2
#         elif i in 'j k l'.split(' ') and n in 'j k l'.split(' '):
#             s += 2
#         elif i in 'm n o'.split(' ') and n in 'm n o'.split(' '):
#             s += 2
#         elif i in 'p q r s'.split(' ') and n in 'p q r s'.split(' '):
#             s += 2
#         elif i in 't u v'.split(' ') and n in 't u v'.split(' '):
#             s += 2
#         elif i in 'w x y z'.split(' ') and n in 'w x y z'.split(' '):
#             s += 2
#         n = i
#     secs.append(s)
# for i in secs:
#     print(i)
