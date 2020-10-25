# Canadian Computing Competition: 2011 Stage 1, Junior #2
#
# Margaret has looked at the wind floating over the prairies for a long time.
# After these observations,
# she has created a formula that will describe the altitude of a weather balloon launched from her house.
# In particular, her equation predicts the altitude A at hour t after launching her balloon is:
#
# A = -6t^4 + ht^3 + 2t^2 + t
#
# where h is an integer value representing the humidity as a value between 0 and 100 inclusive.
#
# Margaret is curious at what the earliest hour is (if any) that her weather balloon will hit the ground after launch,
# so long as it is no more than the maximum time, M , that Margaret is willing to wait.
# You can assume that the weather balloon touches ground when A ≤ 0.
#
# In order to do this, your program should use the formula to calculate the altitude when t = 1, t = 2, and so on,
# until the balloon touches the ground or t = M is reached.

# Input Specification
# The input is two non-negative integers: h, the humidity factor,
# followed by M , the maximum number of hours Margaret will wait for the weather balloon to return to ground.
# You can assume 0 ≤ h ≤ 100 and 0 < M < 240 0 < M < 240.

# Output Specifications
# The output will be one of the following possibilities:
#
#     The balloon does not touch ground in the given time.
#     The balloon first touches ground at hour: T
#
# where T is a positive integer value representing the earliest hour
# when the balloon has altitude less than or equal to zero.

humidity = int(input())
wait = int(input())

for t in range(wait):
    altitude = (-6*((t+1)**4)) + humidity*((t+1)**3) + (2*((t+1)**2)) + (t+1)
    if altitude <= 0:
        print("The balloon first touches ground at hour:")
        print(t+1)
        break
    elif t+1 == wait and altitude > 0:
        print("The balloon does not touch ground in the given time.")
