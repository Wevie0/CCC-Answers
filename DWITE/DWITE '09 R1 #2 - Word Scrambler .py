def recur(has, left):
    if len(left) == 0:
        print(has)
        return
    for i in range(len(left)):
        recur(has+left[i], left[:i] + left[i+1:])

for i in range(5):
    word = list(input())
    recur('', word)