import math
import random
# Warrior & Battle Class


class Warrior:
    """docstring for Warrior"""

    def __init__(self, name="Warrior", health=0, atkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.atkMax = atkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.atkMax * (random.random() + .5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt


class Battle:

    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB

        print(f"{warriorA.name} attacks {warriorB.name} and deals {warriorAAttkAmt} damage.")
        print(f"{warriorB.name} is down to {warriorB.health} health")

        if warriorB.health <= 0:
            print(f"{warriorB.name} has died and {warriorA.name} is victorious.")
            return "Game Over"
        else:
            return "Fight Again"


def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    leonidas = Warrior("Leonidas", 50, 20, 10)
    battle = Battle()
    battle.startFight(maximus, leonidas)

if __name__ == '__main__':
	main()