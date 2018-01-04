# 1, 1, 2, 3, 5, 8, 13
# Fn = Fn-1 + Fn - 2
# Where F0 = 0 and F1 = 1

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		result = fib(n - 1) + fib(n - 2)
		return result

print(fib(5))