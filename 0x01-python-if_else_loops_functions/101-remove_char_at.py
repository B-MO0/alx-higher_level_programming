#!/usr/bin/python3
def remove_char_at(i, j):
    if 0 <= j < len(i):
        return i[:j] + i[j+1:]
    return i
