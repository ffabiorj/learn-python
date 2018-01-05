def isprime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

def gen_primes(max_number):
	for num1 in range(2, max_number):
		if isprime(num1):
			yield num1

prime = gen_primes(50)
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))