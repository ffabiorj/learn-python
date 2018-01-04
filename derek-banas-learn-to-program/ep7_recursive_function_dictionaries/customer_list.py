# Create an array of customers in dictionaries

# Enter Customer: y/n
# Enter Customer Name: 

customers = []
while True:
    answer = input("Enter Customer Name Y/N: ")
    answer = answer.lower()

    if answer == "y":
        fName = input("fName: ")
        lName = input("lName: ")

        customers.append({"fName": fName, "lName": lName})
        print("Successfully added customer.")

    elif answer == "n":
        if len(customers) > 0:
        	print(customers)
        	
        print("Closing program...")
        break
    else: 
        print("Please answer with Y/N")