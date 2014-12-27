#!/usr/bin/python

def get_char_list(chars):
    if type(chars) is str:
        return chars
    elif type(chars) is list:
        return ''.join(chars)
    else:
        return ''

def permutations(input):
    """Generate all the permutations of the characters of the given input"""
    def permute(chars):
        if len(chars) == 0:
            return ''
        if len(chars) == 1:
            return chars[0]
        biglist = []
        for index in range(len(chars)):
            popped = chars[index]
            copy = chars[:index] + chars[index + 1:]
            sublists = permute(copy)
            for sublist in sublists:
                biglist += [sublist[:i] + popped + sublist[i:] for i in range(len(sublist) + 1)]
        return set(biglist)

    return permute(input)


print permutations('eabcd')
