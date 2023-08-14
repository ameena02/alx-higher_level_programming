#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if (idx < 0 or idx > size - 1):
        return (None)
    for j, e in enumerate(my_list):
        if (j == idx):
            return (e)
