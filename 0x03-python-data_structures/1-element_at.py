#!/usr/bin/python3
def element_at(my_list, idx):
    c = len(my_list)
    if idx < 0 or idx >= c:
        return None
    else:
        return my_list[idx]
