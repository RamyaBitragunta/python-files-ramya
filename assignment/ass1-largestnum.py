# PYTHON PROGRAM TO FIND THE LARGEST NUMBER IN THE LIST

# using max function
my_list = [99, 88, 44, 72]
max_result = max(my_list)
print(max_result)

# sort and last element
sort_result = sorted(my_list)
print(sort_result[len(sort_result)-1])
#sort- ascending order

# comparing with each element
def find_large_element(numbers):
    large_element = numbers[0]
    for i in numbers:
        if i > large_element:
            large_element = numbers
    return large_element


result = find_large_element(my_list)
print("Large number is", result)

def find_large_element(my_list):
    large_element = my_list[0]
    for i in my_list:
        if i > large_element:
            large_element = my_list
    return large_element


result = find_large_element(my_list)
print("Large number is", result)
