"""
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.
"""
def add_binary(a,b):
    add = a + b
    ans = '{0:b}'.format(add)
    return str(ans) 

print(add_binary(1,1))