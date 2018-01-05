# Create a class that returns values from the Fibonacci sequence
# each time the next is called
# Sample output:
# Fib: 1
# Fib: 2

class FibGenerator():
	"""docstring for FibGenerator"""
	def __init__(self):
		self.first = 0
		self.second = 1

	def __iter__(self):
		return self

	def __next__(self):
		fibNum = self.first + self.second
		self.first = self.second
		self.second = fibNum
		return fibNum

fib = FibGenerator()

for i in range(1,100):
	print("Fib:", next(fib))