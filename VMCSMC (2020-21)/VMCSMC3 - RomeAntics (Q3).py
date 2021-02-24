converter = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
}
roman = {
    300: 'CCC',
    200: 'CC',
    100: 'C',
    90: 'XC',
    80: 'LXXX',
    70: 'LXX',
    60: 'LX',
    50: 'L',
    40: 'XL',
    30: 'XXX',
    20: 'XX',
    10: 'X',
    9: 'IX',
    8: 'VIII',
    7: 'VII',
    6: 'VI',
    5: 'V',
    4: 'IV',
    3: 'III',
    2: 'II',
    1: 'I'
}
operation = input()
num1 = input()
num2 = input()

tot1 = 0
tot2 = 0

for i in range(len(num1) - 1):
    sym = num1[i]
    x = converter[sym]
    if converter[num1[i + 1]] > x:
        tot1 -= x
    else:
        tot1 += x
tot1 += converter[num1[-1]]

for i in range(len(num2) - 1):
    sym = num2[i]
    x = converter[sym]
    if converter[num2[i + 1]] > x:
        tot2 -= x
    else:
        tot2 += x
tot2 += converter[num2[-1]]

if operation == '*':
    tot1 *= tot2
elif operation == '+':
    tot1 += tot2
else:
    tot1 -= tot2

tot1 = str(tot1)
tot1 = tot1.zfill(3)
output = ""
for index, symbol in enumerate(tot1):
    if symbol != '0':
        if index == 0:
            output += roman[int(symbol + '00')]
        if index == 1:
            output += roman[int(symbol + '0')]
        if index == 2:
            output += roman[int(symbol)]

print(output)
