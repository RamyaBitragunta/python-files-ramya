# TO FIND THE SMALLEST NUMBER IN A LIST

# by using min function
my_list = [34, 58, 79, 23, 54]
mini_list = min(my_list)
print(mini_list)

# by using sort and first element
sor_list = sorted(my_list)
print(sor_list[0])


# by comparing with each element

def find_small_element(my_list):
    first_element = my_list[0]
    for number in my_list:
        if number<first_element:
            first_element = number
    return first_element


result = find_small_element(my_list)
print("Small element is ->", result)
