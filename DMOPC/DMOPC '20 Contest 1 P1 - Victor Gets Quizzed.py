num = int(input())
for i in range(num):
    sub = input()
    math = False
    cs = False
    for j in sub:
        if j == 'M':
            math = True
        if j == 'C':
            cs = True
    if math and cs:
        print("NEGATIVE MARKS")
    elif math or cs:
        print("FAIL")
    else:
        print("PASS")