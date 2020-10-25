# Canadian Computing Competition: 2010 Stage 1, Junior #3
#
# In the early days of computing, instructions had to be "punched" onto rectangular cards, one instruction per card.
# This card deck was then fed into a card reader so the program could be read and executed.
# Students put elastic bands around their card deck, and, often,
# carried their cards in a box for fear that they would become rearranged, and thus, their program would be incorrect.
# Poor Bill though... he left his cards right near a window and the wind blew his neat deck of cards all over the place,
# and thus his program is out of order!
# Bill decides to pick up the cards in some random order and then execute the program
# Write a program to read and execute the commands in Bill's "new" program.

# Input Specification
# The programming language that Bill is using has only two variables (A and B)
# and seven different types of instructions.
# Initially, the variables A and B contain the value 0.
# There is one instruction per line. An instruction is an integer in the range 1 … 7,
# possibly followed by a variable name, which in turn is possibly followed by either a number or a variable.
# In all instructions below, the variable X or Y may refer to either A or B
#
# The specific instructions are:
#
# 1 X n means set the variable X to the integer value n;
# 2 X means output the value of variable X to the screen;
# 3 X Y means calculate X+Y and store the value in variable X;
# 4 X Y means calculate X×Y and store the value in variable X;
# 5 X Y means calculate X−Y and store the value in variable X;
# 6 X Y means calculate the quotient of X/Y and store the value in variable X as an integer, discarding the remainder.
# 7 means stop execution of this program.
#
# You may assume that all division instructions do not cause a division by zero,
# and that all other operations (including instruction 1) do not cause the computed/stored value
# to be larger than 10000 or smaller than −10000

# Output Specification
# Your program should output the value of the indicated variables, one integer per line,
# until the "stop" instruction has been read in, at which time your program should stop execution.

A = 0
B = 0
while True:
    instruction = (input()).split()
    if instruction[0] == "7":
        break
    if instruction[0] == "1":
        if instruction[1] == "A":
            A = int(instruction[2])
        else:
            B = int(instruction[2])
    elif instruction[0] == "2":
        if instruction[1] == "A":
            print(A)
        else:
            print(B)
    else:
        if instruction[1] == "A":
            if instruction[2] == "A":
                if instruction[0] == "3":
                    A = A + A
                elif instruction[0] == "4":
                    A = A * A
                elif instruction[0] == "5":
                    A = A - A
                elif instruction[0] == "6":
                    A = int(A/A)
            else:
                if instruction[0] == "3":
                    A = A + B
                elif instruction[0] == "4":
                    A = A * B
                elif instruction[0] == "5":
                    A = A - B
                elif instruction[0] == "6":
                    A = int(A/B)
        else:
            if instruction[2] == "B":
                if instruction[0] == "3":
                    B = B + B
                elif instruction[0] == "4":
                    B = B * B
                elif instruction[0] == "5":
                    B = B - B
                elif instruction[0] == "6":
                    B = int(B/B)
            else:
                if instruction[0] == "3":
                    B = A + B
                elif instruction[0] == "4":
                    B = A * B
                elif instruction[0] == "5":
                    B = B - A
                elif instruction[0] == "6":
                    B = int(B/A)
