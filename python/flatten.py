#!/usr/bin/python

def flatten(l):
    if type(l) is int:
        return [l]
    if len(l) == 0:
        return []
    if len(l) == 1:
        return flatten(l[0])
    return flatten(l[0]) + flatten(l[1:])

#>>> flatten([12, 13])
#[12, 13]
#>>> flatten([12, [13]])
#[12, 13]
#>>> flatten([12, [13, [12, 13]]])
#[12, 13, 12, 13]
#>>> flatten([12, [13, [12, [14, 35], 13]]])
#[12, 13, 12, 14, 35, 13]
#>>> flatten([1, [2, 3], [[4, [5], 6], 7], 8])
#[1, 2, 3, 4, 5, 6, 7, 8]

