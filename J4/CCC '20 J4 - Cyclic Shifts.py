text = input()
string = input()
length = len(string)
found = False
for i in range(length):
    string = "".join(string)
    if string in text:
        found = True
        break
    string = list(string)
    string.append(string[0])
    del string[0]
print("yes" if found else "no")
