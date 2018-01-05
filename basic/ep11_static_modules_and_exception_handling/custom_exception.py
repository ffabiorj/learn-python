class DogNameError(Exception):
	def __init__(self, *args, **kwargs):
		Exception.__init__(self, *args, **kwargs)

try:
	dogName = "P1231kaka"
	if any(char.isdigit() for char in dogName):
		raise DogNameError
except DogNameError:
	print("Your dog name can't contain a number")
