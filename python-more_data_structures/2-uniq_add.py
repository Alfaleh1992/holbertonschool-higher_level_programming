#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for n in my_list:
        if n not in unique:
            unique.append(n)
    return sum(unique)
