#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    tmp_dict = a_dictionary.copy()
    for x in tmp_dictionary.keys():
        tmp_dictionary[x] *= 2
    return (tmp_dictionary)
