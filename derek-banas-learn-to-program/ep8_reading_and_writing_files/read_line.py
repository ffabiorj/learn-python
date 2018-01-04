import os

with open("mydata.txt", mode="w", encoding="utf-8") as file:
	file.write('Some random text\nMore random text\nAnd some more')


with open("mydata.txt", encoding="utf-8") as myFile:
	lineNum = 1
	while True:
		line = myFile.readline()
		
		if not line:
			break
		print("Line: ", lineNum, " : ", line, end="")
	
	print()