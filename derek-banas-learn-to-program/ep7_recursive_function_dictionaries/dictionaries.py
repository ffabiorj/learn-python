derekDict = {"fName": "Derek", "lName": "Basas", "address": "123 Main St."}
print("My Name:", derekDict["fName"])

derekDict["address"] = "215 North St"
print(derekDict)

derekDict["city"] = "Pittsburg"
print("Is there a city:", "city" in derekDict)

print(derekDict.values())
print(derekDict.keys())

for k, v in derekDict.items():
	print(k, v)

print(derekDict.get("mName", "Not Here"))

del derekDict["fName"]

for i in derekDict:
	print(i)

derekDict.clear()

employees = []
fName, lName = 'Kristofferson', 'Carillo'
employees.append({"fName": fName, "lName": lName})
print(employees)