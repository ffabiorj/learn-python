import threading
import time
import random

class CustThread(threading.Thread):
	"""docstring for CustThread"""
	def __init__(self, name):
		threading.Thread.__init__(self)

		self.name = name

	def run(self):
		getTime(self.name)

		print("Thread", self.name, "Execution ends")

def getTime(name):
	print(f"Thread {name} sleeps at {time.strftime('%H:%M:%S')} {time.gmtime()}")
	
	randSleepTime = random.randint(1,5)
	time.sleep(randSleepTime)	


thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()

print(f"Thread 1 Alive: {thread1.is_alive()}")
print(f"Thread 2 Alive: {thread2.is_alive()}")

print(f"Thread 1 name: {thread1.getName()}")
print(f"Thread 2 name: {thread2.getName()}")

thread1.join()
thread2.join()
print("End")