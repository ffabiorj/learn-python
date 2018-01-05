try:
    aList = [1, 2, 3]
    print()
except (IndexError, NameError):
	print("Index does not exists")
except:
	print("An unknown error occurred.")
