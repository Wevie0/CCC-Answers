# Canadian Computing Competition: 2009 Stage 1, Junior #3
#
# A mobile cell service provider in Ottawa broadcasts an automated time standard
# to its mobile users that reflects the local time at the user's actual location in Canada.
# This ensures that text messages have a valid local time attached to them.
#
# For example, when it is 1420 in Ottawa on Tuesday February 24, 2009 (specified using military, 24 hour format),
# the times across the country are shown in the table below:

# Pacific Time
# Victoria, BC
# Tuesday
# 2/24/2009
# 1120 PST

# Mountain Time
# Edmonton, AB
# Tuesday
# 2/24/2009
# 1220 MST
#
# Central Time
# Winnipeg, MB
# Tuesday
# 2/24/2009
# 1320 CST
#
# Eastern Time
# Toronto, ON
# Tuesday
# 2/24/2009
# 1420 EST
#
# Atlantic Time
# Halifax, NS
# Tuesday
# 2/24/2009
# 1520 AST
#
# Newfoundland Time
# St. John's, NL
# Tuesday
# 2/24/2009
# 1550 Newfoundland ST
#
# Write a program that accepts the time in Ottawa in 24 hour format
# and outputs the local time in each of the cities listed above including Ottawa.
# You should assume that the input time will be valid
# (i.e., an integer between 0 and 2359 with the last two digits being between 00 and 59).
#
# You should note that 2359 is one minute to midnight,
# midnight is 0, and 13 minutes after midnight is 13.
# You do not need to print leading zeros, and input will not contain any extra leading zeros.

time = int(input())

timeZones = [time - 300, time - 200, time - 100, time + 100, time + 130]

for i in range(len(timeZones)):
    if timeZones[i] > 2400:
        timeZones[i] -= 2400
    if timeZones[i] < 0:
        timeZones[i] += 2400  # 2400 - timeZones[i] works as well
    if timeZones[i] % 100 > 60:
        timeZones[i] += 40

print("%d in Ottawa" % time)
print("%d in Victoria" % timeZones[0])
print("%d in Edmonton" % timeZones[1])
print("%d in Winnipeg" % timeZones[2])
print("%d in Toronto" % time)
print("%d in Halifax" % timeZones[3])
print("%d in St. John's" % timeZones[4])



