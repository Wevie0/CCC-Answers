# Canadian Computing Competition: 2012 Stage 1, Junior #1
#
# Many communities now have "radar" signs that tell drivers what their speed is, in the hope that they will slow down.
#
# You will output a message for a "radar" sign.
# The message will display information to a driver based on his/her speed according to the following table:

# km/h over the limit 	Fine
# 1 to 20 	            $100
# 21 to 30           	$270
# 31 or above       	$500

# Input Specification
# The user will be prompted to enter two integers.
# First, the user will be prompted to enter the speed limit.
# Second, the user will be prompted to enter the recorded speed of the car.

# Output Specification
# If the driver is not speeding, the output should be: Congratulations, you are within the speed limit!
# If the driver is speeding, the output should be: You are speeding and your fine is $F,
# where F is the amount of the fine as described in the table above.

speedLimit = int(input())
speedOfCar = int(input())
difference = speedOfCar - speedLimit
fine = 0

if difference <= 0:
    print("Congratulations, you are within the speed limit!")
elif difference < 21:
    fine = 100
elif difference < 31:
    fine = 270
else:
    fine = 500

if fine != 0:
    print("You are speeding and your fine is $%d." % fine)
