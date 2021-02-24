line = input()
line = line.lower()
letters = 'abcdefghijklmnopqrstuvwxyz '

for i in line:
    if i not in letters:
        if i == '\'':
            line = line.replace(i, "")
        else:
            line = line.replace(i, " ")
arr = line.split()
print(line, arr)
tot = 0
for i in arr:
    tot += len(i)
tot //= len(arr)
print(tot)

vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,
    'y': 0,
}
cons = {
    'b': 0,
    'c': 0,
    'd': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'z': 0,

}
places = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

for i in line:
    if i in vowels:
        vowels[i] += 1
    elif i in cons:
        cons[i] += 1

for i in sorted(vowels, key=vowels.get, reverse=True):
    cv = 0
    if vowels[i] > 0:
        cv = places[i]
        print(i)
    break
for i in sorted(cons, key=cons.get, reverse=True):
    cc = 0
    if cons[i] > 0:
        cc = places[i]
        print(i)
    break

out = cc * cv * tot
print(out)
