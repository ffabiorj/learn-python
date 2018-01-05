import random
# Find the multiples of 9 from a random 100 value list with 
# values between 1-1000

# Create 100 value list with values between 1-1000
aList = list(random.randint(1, 1001) for i in range(100))
find = list(filter((lambda x: x % 9 == 0), aList))

print(find)