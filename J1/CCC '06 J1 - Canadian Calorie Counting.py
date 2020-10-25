# Canadian Computing Competition: 2006 Stage 1, Junior #1
#
# At Chip's Fast Food emporium there is a very simple menu. Each food item is selected by entering a digit choice.
# Here are the three burger choices:
# 1 – Cheeseburger (461 Calories)
# 2 – Fish Burger (431 Calories)
# 3 – Veggie Burger (420 Calories)
# 4 – no burger
# Here are the three drink choices:
# 1 – Soft Drink (130 Calories)
# 2 – Orange Juice (160 Calories)
# 3 – Milk (118 Calories)
# 4 – no drink
# Here are the three side order choices:
# 1 – Fries (100 Calories)
# 2 – Baked Potato (57 Calories)
# 3 – Chef Salad (70 Calories)
# 4 – no side order
# Here are the three dessert choices:
# 1 – Apple Pie (167 Calories)
# 2 – Sundae (266 Calories)
# 3 – Fruit Cup (75 Calories)
# 4 – no dessert
#
# Write a program that will compute the total Calories of a meal.

# Input Specification
# The program should input a number for each type of item then calculate and display the Calorie total.
# The first line will be the customer's choice of burger,
# the second will be the choice of side, then drink, then dessert.
# You may assume that each input will be a number from 1 to 4.
# That is, each customer has to pick exactly one number from each of the four options out of each category.

# Output Specification
# The program prints out the total Calories of the selected meal, and stops executing after this output.

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

calories = [461, 431, 420, 0, 130, 160, 118, 0, 100, 57, 70, 0, 167, 266, 75, 0]
totalCal = calories[burger-1] + calories[side+7] + calories[drink+3] + calories[dessert+11]
print("Your total Calorie count is %d." % totalCal)
