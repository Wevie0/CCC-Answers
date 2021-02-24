# i = nk -1

string = input()
n = string.count("goose")
output = ""
if n != 0:
    for i in range(len(string)):
        for k in range(200):
            if i == n * k - 1:
                output += string[i]
    print(output)
else:
    print("The goose is on the loose.")
