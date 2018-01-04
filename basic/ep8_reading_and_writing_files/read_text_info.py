import os

with open("mydata.txt", mode="w", encoding="utf-8") as file:
	file.write('Some random text\nMore random text\nAnd some more')


with open("mydata.txt", encoding="utf-8") as myFile:
	lineNum = 1
	while True:
		line = myFile.readline()
		
		if not line:
			break

		print("line", lineNum)
		
		wordList = line.split()
		print("Number of words:", len(wordList))

		charCount = 0
		for word in wordList:
			for char in word:
				charCount += 1

		avgNumChar = charCount/len(wordList)
		print(f"Avg Word Length : {avgNumChar:.2}")
		print()
		lineNum +=1
	print()