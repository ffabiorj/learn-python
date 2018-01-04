def add_num(x, y):
    return x + y


glb_name = "Sally"


def change_name():
    global glb_name
    glb_name = "Sammy"

def get_sum(x, y):
	sum = x + y

print(get_sum(5,6))

change_name()


print(glb_name)
