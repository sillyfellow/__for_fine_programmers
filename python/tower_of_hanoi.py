#!/usr/bin/python

class NamedList(list):
    def __init__(self, *args):
        list.__init__(self, args)
        self.name = "??"

    def setName(self, name):
        self.name = name

    def Name(self):
        return self.name

    def __str__(self):
        return "%s: %s" % (self.name, repr(self))


def tower_of_hanoi(start, dest, temp, n):
    if n == 0:
        return
    tower_of_hanoi(start, temp, dest, n - 1)
    moving_disk = start.pop()
    print "Moving %d from %s to %s" % (moving_disk, start.Name(), dest.Name())
    dest.append(moving_disk)
    tower_of_hanoi(temp, dest, start, n - 1)


start = NamedList()
start.setName('start')

dest = NamedList()
dest.setName('dest')

temp = NamedList()
temp.setName('temp')

start += range(6, 0, -1)
print start
print dest
print temp
tower_of_hanoi(start, dest, temp, len(start))
print start
print dest
print temp
