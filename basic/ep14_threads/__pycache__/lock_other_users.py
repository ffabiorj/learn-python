import threading
import time
import random


class BankAccount(threading.Thread):
    """docstring for BankAccount"""

    accountBalance = 100

    def __init__(self, name, amount):
        threading.Thread.__init__(self)

        self.name = name
        self.amount = amount

    def run(self):
        threadLock.acquire()

        BankAccount.getMoney(self)
        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print(f"{customer.name} tries to withdraw ${customer.amount} {time.strftime('%H:%M:%S')}")

        if BankAccount.accountBalance - customer.amount > 0:
            BankAccount.accountBalance -= customer.amount
            print(f"{customer.name} balance left: ${BankAccount.accountBalance}: ")
        else:
            print(f"Not enough money to withdraw ${customer.amount} : Balance ${BankAccount.accountBalance}")

        time.sleep(3)

threadLock = threading.Lock()

doug = BankAccount("Doug", 1)
merry = BankAccount("Merry", 100)
sally = BankAccount("Sally", 50)
pewds = BankAccount("Pewds", 200)

doug.start()
merry.start()
sally.start()
pewds.start()

doug.join()
merry.join()
sally.join()
pewds.join()

print("Execution ends")
