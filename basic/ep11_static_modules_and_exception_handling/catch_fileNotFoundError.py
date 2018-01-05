try:
	myFile = open("mydata2.txt", encoding="utf-8")
except FileNotFoundError as e:
	print("File not found")
else:
	print(myFile.read())
	myFile.close()
finally:
	print("Finished working with file")