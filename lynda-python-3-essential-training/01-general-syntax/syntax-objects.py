#!/usr/bin/python3 
# ^ used to run python in different environments
# four spaces are traditional in python

class Egg():
	# Constructor is a method, inside the class
	def __init_(self, kind = "fried"):
		self.kind = kind
	def whatKind(self):
		return self.kind

def main():
	# a = 1 # defines a variable "a" and creates an
	# 	  # integer type variable an puts the value "1"
	# print('This is the syntax.py file')

	fried = Egg()
	scrambled = Egg('scrambled')
	print(fried.whatKind())

def func(): # a simple function that prints 0 - 10
	for i in range(10):
		print(i)

if __name__ == '__main__':
	main() # allows us to run the script 
		   # in any order we want
	#func()
