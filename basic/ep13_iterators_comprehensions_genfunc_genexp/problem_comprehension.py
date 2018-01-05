# Generate a list of 50 random values between 1-1000
# Return numbers that are multiple of 9
# print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])
import random

print([x for x in [random.randint(1,1001) for i in range(50)] if x % 9 == 0])