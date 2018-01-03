import random

# 1. An outer loop decrease in size each time
# 2. The goal is to have the largest number at the end of the list
#    when the router loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning of
#    the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at the
#    end of the list decrement the outer loop by 1

num_list = []

for i in range(6):
    num_list.append(random.randint(1, 10))

i = len(num_list) - 1

while i > 1:
    j = 0
    while j < i:
        print(f"\nis {num_list[j]} > {num_list[j+1]}")
        if num_list[j] > num_list[j + 1]:
            print("Switch")
            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = temp
        else:
            print("Don't switch")
        j += 1

        for k in num_list:
            print(k, end=", ")
        print()

    print("End of round")
    i -= 1

for k in num_list:
    print(k, end=", ")
