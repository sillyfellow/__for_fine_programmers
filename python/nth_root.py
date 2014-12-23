#!/usr/bin/python

from math import fabs


def nth_root(m, n, epsilon=1e-4):
    low, high = 1.0, m * 1.0
    while True:
        root = (low + high) / 2.0
        delta = (root ** n) - m
        if fabs(delta) < epsilon:
            return root

        if delta < 0:
            low = root
        else:
            high = root


def Usage(name):
    print "Usage: %s <m> <n>" % name


import sys
if __name__ == "__main__":
    if len(sys.argv) != 3:
        Usage(sys.argv[0])
        exit(1)
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    print "%d-th root of %d is => %f" % (n, m, nth_root(m, n))
