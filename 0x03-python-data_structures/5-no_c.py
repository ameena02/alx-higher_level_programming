#!/usr/bin/python3
def no_c(my_string):
    a = my_string
    a = a.translate({ord('c'): None})
    a = a.translate({ord('C'): None})
    return (a)
