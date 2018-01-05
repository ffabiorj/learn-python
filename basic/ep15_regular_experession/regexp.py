import re

string = "The ape was at the apex"

# re.search
if re.search("ape", string):
	print("There is an ape in the string")


# re.findall
allApes = re.findall("ape.", string)
print("Matches:", " | ".join(allApes))


# iterator
for i in re.finditer("ape.", string):
	locTuple = i.span()
	print(locTuple)
	print(string[locTuple[0]:locTuple[1]])



animalStr = "Cat rat mat pat"

#  match characters
allAnimals = re.findall("[crmfp]at", animalStr)
print(allAnimals)

# match 
someAnimals = re.findall("[^Cr]at", animalStr)
print(someAnimals)
