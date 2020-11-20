k = int(input())
word = list(input())

for i in range(len(word)):
    word[i] = ord(word[i])
    word[i] = word[i] - 3 * (i+1) - k
    if word[i] < 65:
        word[i] += 26
    word[i] = chr(word[i])
print(''.join(word))
