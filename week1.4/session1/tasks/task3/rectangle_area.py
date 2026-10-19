
# function implementation

def rectangle_area( ):  # define suitable input data
    x = int(input("Enter your first value: ")) 
    y = int(input("Enter your second value: "))
    return x*y

def num_range():
    ask_int = int(input("Enter an integer: "))
    int_list = []
    for i in range(ask_int+1):
        int_list.append(i)
    return (ask_int, int_list)
# testing the function


print(f"Area is {rectangle_area( )}.")   # provide suitable data matching your inputs
num_range_tuple = num_range()
print(f"Here is a list of numbers from 0 to {num_range_tuple[0]}: {num_range_tuple[1]}")