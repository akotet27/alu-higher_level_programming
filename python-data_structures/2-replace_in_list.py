#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    if idx < 0 or idx > len(my_list):
        return None
    my_list[idx] = new_element
    return my_list
idx = 0
new_element = 7

my_list = [1, 2, 3, 4, 5]
new_list = replace_in_list(my_list, idx, new_element)
print(new_list)
