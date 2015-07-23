#!/usr/bin/python


def atoi(s):
    return reduce(lambda x, y: x * 10 + y, [ord(d) - ord('0') for d in s], 0)


def itoa(n):
    digits = []
    while n > 0:
        digits = [n % 10] + digits
        n /= 10

    return ''.join([chr(d + ord('0')) for d in digits])


def itoa_r(n):
  return chr(n + ord('0')) if n < 10 else itoa(n / 10) + itoa(n % 10)


def Usage(name):
    print "Usage: %s <n>" % name


import sys
if __name__ == "__main__":
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
        exit(1)
    s = sys.argv[1]
    n = atoi(s)
    if n != int(s):
        print "Error!"

    s2 = itoa(n)
    if s != s2:
        print "Error2"

    s2 = itoa_r(n)
    if s != s2:
        print "Error2"

    print "%s => %d => %s" % (s, n, s2)
