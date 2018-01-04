import random
num_list = []

for i in range(5):
	num_list.append(random.randint(1, 10))

num_list.sort()
num_list.reverse()
num_list.insert(5, 10)
num_list.remove(10)
num_list.pop(2)

for k in num_list:
	print(k, end=", ")