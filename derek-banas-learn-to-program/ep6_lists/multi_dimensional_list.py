import random
import math

list_table = [[0] * 4 for i in range(10)]

for i in range(4):
	for j in range(4):
		list_table[i][j] = f"{i} : {j}"

for i in range(4):
	for j in range(4):
		print(list_table[i][j], end=" || ")
	print()