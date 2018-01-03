import math

def circle_area():
	radius = float(320)

	area = math.pi * (math.pow(radius, 2))
	print(f"The area of the circle is: {area:.2f}")
def rectangle_area():
	length = float(15)
	width = float(30)

	area = length * width
	print("The area of the rectangle is:", area)

def get_area(shape):
	shape = shape.lower()
	if shape == "rectangle":
		rectangle_area()
	elif shape == "circle":
		circle_area()
	else:
		print("Please enter rectangle or circle.")

def main():
    shape_type = "circle"
    get_area(shape_type)


if __name__ == '__main__':
    main()
