#!/usr/bin/python3 
# ^ used to run python in different environments
# four spaces are traditional in python
def main():
	a = 1 # defines a variable "a" and creates an
		  # integer type variable an puts the value "1"
	print('This is the syntax.py file')

def func(): # a simple function that prints 0 - 10
	for i in range(10):
		print(i)

if __name__ == '__main__':
	main() # allows us to run the script 
		   # in any order we want
	func()
