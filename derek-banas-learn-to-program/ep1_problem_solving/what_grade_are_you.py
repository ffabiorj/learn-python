# Ask user to input age
age = eval(input('What is your age: '))
# If age is 5 Go to Kindergarten
if age < 5:
	print('Go to kindergarten')
# Ages 6 through 17 goes to grade 1 through 12
elif age <= 17:
	print('Go to grade 1 or 12')
# If age is greater then 17 say go to college
else:
	print('Go to college')
