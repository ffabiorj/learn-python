num1, num2 = 4, 0

try:
	quotient = num1 / num2
	print(f"{num1} / {num2} = {quotient}")
except ZeroDivisionError:
	print("You can't divide by zero")
else:
	print("You didn't raise an exception")
finally:
	print("I execute no matter what")