class Dog:
	num_of_dogs = 0

	def __init__(self, name="Unknown"):
		self.name = name

		Dog.num_of_dogs += 1

	@staticmethod
	def getNumOfDogs():
		print(f"There are currently {Dog.num_of_dogs} dogs.")


def main():
	spot = Dog("Spot")
	doug = Dog("Doug")
	spot.getNumOfDogs()
	doug.getNumOfDogs()

if __name__ == '__main__':
	main()