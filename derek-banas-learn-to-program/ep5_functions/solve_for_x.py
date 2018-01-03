# solve for x
# x + 4 = 9

# x will always be the 1st value received and you only will deal with addtion


def solve_x(equation):
    # Receive the string and split the string into variablse
    x, add, num1, equal, num2 = equation.split()
    # convert the strings into ints
    num1, num2 = int(num1), int(num2)
    # convert the result into a string and join it to the string
    return "x = " + str(num2 - num1)


print(solve_x("x + 4 = 9"))
