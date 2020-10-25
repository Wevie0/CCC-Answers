# Canadian Computing Competition: 2010 Stage 1, Junior #2
#
# Nikky and Byron are playing a silly game in gym class.
#
# Nikky is told by his teacher to walk forward a steps (1 ≤ a ≤ 100) and then walk backward b steps (1 ≤ b ≤ 100),
# after which he repeats a forward, b backward, etc.
# Likewise, Byron is told to walk forward c c steps (1 ≤ c ≤ 100) and then walk backward d steps (1 ≤ d ≤ 100),
# after which he repeats c forward, d backward, etc. You may assume that a ≥ b and c ≥ d.
#
# Byron and Nikky have the same length of step, and they are required to take their steps simultaneously
# (that is, Nikky and Byron will both step forward on their first steps at the same time,
# and this will continue for each step).
#
# Nikky and Byron start walking from one end of a soccer field.
# After s steps (1 ≤ s ≤ 10000), the gym teacher will blow the whistle.
# Your task is to figure out who has moved the farthest away from the starting position when the whistle is blown.

# Input Specification
# The input will be the 5 integers a, b, c, d, and s, each on a separate line.
# Output Specification
#
# The output of your program will be one of three possibilities:
# Nikky if Nikky is farther ahead after s steps are taken;
# Byron if Byron is farther ahead after s steps are taken;
# Tied if Byron and Nikky are at the same distance from their starting position after s steps are taken.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())


def calc(a1, b1):
    times = int(s / (a1 + b1))
    steps = times * (a1 - b1)
    remainder = s - (times * (a1 + b1))

    if a1 <= remainder:
        steps += a1
        remainder = remainder - a1
        steps -= remainder
    else:
        steps += remainder
    return steps


nikky = calc(a, b)
byron = calc(c, d)

if nikky > byron:
    print("Nikky")
elif nikky == byron:
    print("Tied")
else:
    print("Byron")
