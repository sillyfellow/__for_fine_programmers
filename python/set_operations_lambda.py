#!/usr/bin/python

def union(a, b):
    return a + filter(lambda x: x not in a, b)

def intersection(a, b):
    return filter(lambda x: x in a, b)

def sym_diff(a, b):
    return filter(lambda x: x not in b, a) + filter(lambda x: x not in a, b)

if __name__ == '__main__':
    a = [x for x in range(1, 100) if x % 3 == 0]
    b = [x for x in range(1, 100) if x % 5 == 0]
    # some simple tests, not all possible ones, of course.
    ua = union(a, b)
    ia = intersection(a, b)
    sda = sym_diff(a, b)
    ub = union(b, a)
    ib = intersection(b, a)
    sdb = sym_diff(b, a)
    assert set(ua) == set(ub)
    assert set(ia) == set(ib)
    assert set(sda) == set(sdb)
    assert set(sdb + ia) == set(sda + ib)
    assert set(sdb + ib) == set(ua)



