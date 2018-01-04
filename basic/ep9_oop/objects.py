# Real World Objects: Attributes & Capabilities
# Dog Attributes (Fields/Variables): Height, Weight, Favorite Food
# Dog Capabilities(Methods): Run, Walk, Eat
# Define attributes and capabalites


class Dog(object):
    """docstring for Dog"""

    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print(f"{self.name} the dog runs")

    def eat(self):
        print(f"{self.name} the dog eats")

    def bark(self):
        print(f"{self.name} the dog barks")


def main():
    spot = Dog("Spot", 66, 26)
    spot.bark()

    bowser = Dog("Bowser")
    bowser.run()

if __name__ == '__main__':
    main()
