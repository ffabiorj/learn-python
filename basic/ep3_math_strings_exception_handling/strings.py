print(type(3))
print(type(3.14))
print(type("3"))
print(type('3'))

samp_string = "This is a very important string"
print(samp_string[0])
print(samp_string[-1])
print(len(samp_string)) 
print(samp_string[8:]) 
print("Green" + "Eggs")
print("Hello " * 5)

for char in samp_string:
    print(char)

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])
