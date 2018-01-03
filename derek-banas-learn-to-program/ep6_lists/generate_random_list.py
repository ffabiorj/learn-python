import random

# generate random numbers from 1 -9 inside a list "5 values" 
random_list = []

for i in range(6):
	random_list.append(random.randint(1, 10))

print(random_list)