'''
create a class that acts as a list with a limit on adding objects. 
* can push objects 
* delete objects 
* sort objects
'''


class MaxSizeList():
    """
    MaxSizeList creates a list with a limit depending
    on the argument given after creating an instance
    of class.   
    """

    def __init__(self, max_list='af'):
        self.my_list = []
        self.max_list = max_list
        # First we check max list if it's an int
        if isinstance(max_list, int) is True:
        	print('Creating max limit sucess')
       	else:
       		self.max_list = int(input('Enter an integer: '))

    def push(self, item):
        """ Pushes new item in my_list """
        # check if my_list is over the limit
        if len(self.my_list) > self.max_list:
            print('Cannot add any more item')
        else:
            self.my_list.append(item)
            print(self.my_list)
    def get(self):
        return self.my_list

def main():
    """ Create an instance of the class and push items more than the max_limit  """
    x = MaxSizeList()
    x.push(5)
    x.push(5)
    x.push(5)
    x.push(5)
    x.push(5)
    x.push(5)
    x.get()

if __name__ == '__main__':
    main()
