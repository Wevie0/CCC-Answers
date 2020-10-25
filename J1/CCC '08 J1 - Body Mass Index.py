# Canadian Computing Competition: 2008 Stage 1, Junior #1
#
# The Body Mass Index (BMI) is one of the calculations used by doctors to assess an adult's health.
# The doctor measures the patient's height (in metres) and weight (in kilograms),
# then calculates the BMI using the formula:
#
# BMI = weight/(weight*height)
#
# Write a program which takes the patient's weight and height as input, calculates the BMI,
# and displays the corresponding message from the table below.

weight = float(input())
height = float(input())

BMI = weight/(height**2)

if BMI > 25:
    print("Overweight")
elif BMI < 18.5:
    print("Underweight")
else:
    print("Normal weight")
