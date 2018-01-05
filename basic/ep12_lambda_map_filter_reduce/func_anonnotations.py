def random_func(name: str, age: int, weight: float) -> str:
	print("Name:", name)
	print("Age:", age)
	print("Weight:", weight)
	return f"{name} is {age} years old and weighs {weight}"

print(random_func("Derek", 41, 165.5))
print(random_func(89, "Derek", "Turtle"))
print(random_func.__annotations__)