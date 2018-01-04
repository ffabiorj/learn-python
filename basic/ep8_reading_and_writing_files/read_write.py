import os

with open("mydata.txt", mode="w", encoding="utf-8") as file:
	file.write('Some random text\nMore random text\nAnd some more')

with open("mydata.txt", encoding="utf-8") as file:
	print(file.read())

os.rename("mydata.txt", "mydata2.txt")
os.remove("mydata2.txt")
#os.mkdir("mydir")
os.chdir("mydir")
print("Current directory:", os.getcwd())

os.chdir("..")
os.remove("mydir")