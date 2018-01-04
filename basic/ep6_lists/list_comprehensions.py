import random
import math

even_list = [i*2 for i in range(10)]
print(even_list, end=", ")

num_list = [1,2,3,4,5]
value_list = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)] for m in num_list]

for i in value_list:
	print(i)

mult_list = [[0] * 10 for i in range(10)]

for i in mult_list:
	print(i)