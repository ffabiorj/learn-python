import random
import math

rand_list = ["string", 1.234, 25]
one_to_ten = list(range(10))
rand_list = rand_list + one_to_ten

print(rand_list)
print(rand_list[0])
print("List length:", len(rand_list))

first3 = rand_list[0:3]

for i in first3:
	print(f"{first3.index(i)}, {i}")

print(first3[0] * 3)
print("string" in first3)
print("Index of string:", first3.index("string"))
print("How many strings:", first3.count("string"))

first3[0] = "New String"
print(first3[0])

first3.append("New new string")