#!/usr/bin/python


def array_product(a):
    output = [1] * len(a)
    left = right = 1
    indices = [(x, len(a) - 1 - x) for x in range(len(a))]
    for (l, r) in indices:
        output[l] *= left
        output[r] *= right
        left *= a[l]
        right *= a[r]
    return output


arrays = [[], [1, 2], [2, 3, 5], [2, 3, 5, 7], [11, 11, 11], [1, 2, 3, 4, 0], [12], [-12, 9, -4, -12, -34]]

for array in arrays:
    print array, array_product(array)
