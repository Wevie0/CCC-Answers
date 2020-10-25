# Canadian Computing Competition: 2015 Stage 1, Junior #2
#
# We often include emoticons in our text messages to indicate how we are feeling.
# The three consecutive characters :-) indicate a happy face
# and the three consecutive characters :-( indicate a sad face.
# Write a program to determine the overall mood of a message.

# Input Specification
# There will be one line of input that contains between 1 and 255 characters.
# Output Specification
#
# The output is determined by the following rules:
#
#     If the input line does not contain any happy or sad emoticons, output none.
#     Otherwise, if the input line contains an equal number of happy and sad emoticons, output unsure.
#     Otherwise, if the input line contains more happy than sad emoticons, output happy.
#     Otherwise, if the input line contains more sad than happy emoticons, output sad.

# string = input()
#
#
# def find_all(str, sub):
#     start = 0
#     while True:
#         start = str.find(sub, start)
#         if start == -1:
#             return
#         yield start
#         start += len(sub)
#
#
# happy = (list(find_all(string, ":-)")))
# sad = (list(find_all(string, ":-(")))
#
# if len(happy) > len(sad):
#     print("happy")
# elif len(sad) > len(happy):
#     print("sad")
# elif len(sad) == len(happy) and sad != [] and happy != []:
#     print("unsure")
# else:
#    print("none")

happy = 0
sad = 0
string = input()
listString = list(string)
for i in range(len(listString) - 2):
    if listString[i] == ":" and listString[i+1] == "-":
        if listString[i+2] == ")":
            happy += 1
        elif listString[i+2] == "(":
            sad += 1
if happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif (not(sad == 0 and happy == 0)) and happy == sad:
    print("unsure")
else:
    print("none")
