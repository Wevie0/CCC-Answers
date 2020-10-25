# Canadian Computing Competition: 2005 Stage 1, Junior #1
#
# Moe Bull has a cell phone and after a month of use
# is trying to decide which price plan is the best for his usage pattern.
# He has two options, each plan has different costs for daytime minutes, evening minutes and weekend minutes.

# Plan Costs
#       daytime 	                                evening 	            weekend
# A 	100 free minutes then 25 cents per minute 	15 cents per minute 	20 cents per minute
# B 	250 free minutes then 45 cents per minute 	35 cents per minute 	25 cents per minute
#
# Write a program that will input the number of each type of minutes and output the cheapest plan for this usage pattern
# using the format shown below. The input will be in the order of daytime minutes, evening minutes and weekend minutes.
# In the case that the two plans are the same price, output both plans.

daytime = int(input())
evening = int(input())
weekend = int(input())

costA = max(0,((daytime - 100) * 0.25)) + (evening * 0.15) + (weekend * 0.20)
costB = max(0,((daytime - 250) * 0.45)) + (evening * 0.35) + (weekend * 0.25)

costA = round(costA, 2)
costB = round(costB, 2)

print("Plan A costs %.2f" % costA)
print("Plan B costs %.2f" % costB)

if costA == costB:
    print("Plan A and B are the same price.")
elif costA > costB:
    print("Plan B is cheapest.")
else:
    print("Plan A is cheapest.")


