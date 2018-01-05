# lambda arg1, arg2 : expression use the args

# store inside variable
sum = lambda n1, n2:  n1 + n2

print("Sum: ", sum(4, 5))

can_vote = lambda age: True if age >= 19 else False
print(can_vote(19))

# store inside lists

powerList = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for func in powerList:
    print(func(4))

# store inside dictionaries
attack = {"quick": (lambda: print("quick attack")),
          "power": (lambda: print("power attack")),
          "miss": (lambda: print("quick attack"))}

attack['quick']()

import random

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()