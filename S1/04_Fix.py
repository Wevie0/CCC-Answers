n = int(input())


for i in range(n):
    collection = []
    output = "Yes"
    for j in range(3):
        collection.append(input())
    if collection[1].find(collection[0]) == 0:
        output = "No"
    if collection[1].find(collection[0]) == abs(len(collection[1]) - len(collection[0])):
        output = "No"
    if collection[1].find(collection[2]) == 0:
        output = "No"
    if collection[1].find(collection[2]) == abs(len(collection[1]) - len(collection[2])):
        output = "No"
    if collection[2].find(collection[0]) == 0:
        output = "No"
    if collection[2].find(collection[0]) == abs(len(collection[2]) - len(collection[0])):
        output = "No"
    if collection[2].find(collection[1]) == 0:
        output = "No"
    if collection[2].find(collection[1]) == abs(len(collection[2]) - len(collection[1])):
        output = "No"
    if collection[0].find(collection[1]) == 0:
        output = "No"
    if collection[0].find(collection[1]) == abs(len(collection[0]) - len(collection[1])):
        output = "No"
    if collection[0].find(collection[2]) == 0:
        output = "No"
    if collection[0].find(collection[2]) == abs(len(collection[0]) - len(collection[2])):
        output = "No"

    print(output)
