length = int(input())
words = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]
periods = [7, 10, 14, 19, 24, 30]   # [8, 11, 15, 20, 25] in normal counting


def addPeriod(string):
    pointer = 0
    diff = length - len(string)
    while diff > 0:
        pointer = (string.find('.', pointer))
        if pointer == -1:
            string += '.'
        else:
            string = string[:pointer] + '.' + string[pointer:]
        diff = length - len(string)
        pointer += 2
    return string


for i in periods:
    if i <= length:
        maximum = periods.index(min(i, length))

line = ('.'.join(words[0:maximum+1]))
print(addPeriod(line))
line2 = ('.'.join(words[maximum+1:]))
print(addPeriod(line2))



# 20 doesn't work
# fix multiple lines
