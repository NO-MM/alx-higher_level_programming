#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = my_string.translate({ord("C"): None, ord("c"): None})
        return new_string
