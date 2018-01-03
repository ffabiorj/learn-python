# Have the user enter their investment amount and expected interest
# Each year their investment will increase their investment + their investment  * interest
# Print out the earnings after a 10 year period

# Ask for the money invested + the interest rate
money = input("Investment: ")
interest = input("Interest: ")
# convert the value to float
money = float(money)
# convert value to a float and round the percentage rate by 2 digits 
interest = float(interest) * .01
# cycle through 10 years using a for loop and range 0 to 9
for i in range(10):
	money = money + (money * interest)
# Output results 
print(f"Investment after 10 years: {money:.2f}")