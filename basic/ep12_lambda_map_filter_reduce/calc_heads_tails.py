import random
# Create a random list filled with characters h and t (h=heads, t=tails) and output results = Heads: 54
flipList = []

for i in range(1, 1000):
	flipList += random.choice(["H", "T"])

# Output
print("Heads:", flipList.count('H'))
print("Tails:", flipList.count('T'))