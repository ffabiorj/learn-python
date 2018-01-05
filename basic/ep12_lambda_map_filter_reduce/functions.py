def mult_by_2(n):
	return n * 2

x = mult_by_2
print("5 * 2", x(5))

def do_math(func, num):
	return func(num)

print("8 x 2", do_math(x, 8))
