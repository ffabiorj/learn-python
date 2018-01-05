# __itr__
sampStr = iter("Sample")

print("Char: ", next(sampStr))
print("Char: ", next(sampStr))

# custom iterator
class Alphabet:
	def __init__(self):
		self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.index = -1

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.letters) - 1:
			raise StopIteration
		self.index += 1 
		return self.letters[self.index]

alpha = Alphabet()

for letter in alpha:
	print(letter)

# key iterator
kris = {"fName": "Kristoffer", "lName": "Carillo"}

for key in kris:
	print(key, kris[key])
