#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    size = len(my_list)
    if (idx >= 0 or idx < size):
        for j, e in enumerate(my_list):
            if (j == idx):
                my_list[j] = element
    return (my_list)
