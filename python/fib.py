#!/usr/bin/python


def fib_recursive(n):
    """Find the n-th fibonacci number, recursively"""
    if n < 1:
        return 0
    if n <= 2:
        return (n - 1)
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    """Find the n-th fibonacci number, iteratively"""
    if n < 1:
        return 0
    a, b = 0, 1
    while n > 2:
        a = a + b
        b = a + b
        n -= 2
    return a if (n == 1) else b


def fib_memoized(n):
    """Find the n-th fibonacci number, recursively, but using memoization."""
    if n < 1:
        return 0

    fibs = [0, 1] + (n - 2) * [-1]

    def fib_inner(n):
        if fibs[n] == -1:
            fibs[n] = fib_inner(n - 1) + fib_inner(n - 2)
        return fibs[n]

    # note the n - 1, because the indexing starts at zero.
    return fib_inner(n - 1)


def Usage(name):
    print "Usage: %s <n>" % name


import time


def print_times(foo, n, message):
    start = time.time() * 1000
    print "Fib(%d) = %d : %s in %d milliseconcds" % (n, foo(n), message, int(1000 * time.time() - start))


import sys
if __name__ == "__main__":
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
        exit(1)
    n = int(sys.argv[1])
    print_times(fib_recursive, n, "Recursive")
    print_times(fib_iterative, n, "Iterative")
    print_times(fib_memoized,  n, "memoized ")
