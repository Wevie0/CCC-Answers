phrase1 = list(input())
phrase2 = list(input())

phrase1 = sorted(filter(str.strip, phrase1))
phrase2 = sorted(filter(str.strip, phrase2))

if phrase1 == phrase2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
