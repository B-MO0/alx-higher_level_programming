#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = []
    rev = reversed(my_list)
    for i in rev:
        print(f"{i:d}")
