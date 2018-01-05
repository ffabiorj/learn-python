onTo10 = range(1, 11)


def dbl_num(num):
    return num * 2

print(list(map(dbl_num, onTo10)))
print(list(map((lambda x: x * 3), onTo10)))

aList = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(aList)