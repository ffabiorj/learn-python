import random
# Create a guessing game between 1 and 10
secret = random.randint(1, 10)

while True:
	answer = int(input("Guess the number: "))
	if answer == secret:
		print("You are right!")
		break