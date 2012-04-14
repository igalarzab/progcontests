#!/usr/bin/env python
#
#  Problems of Programming Contests
#  ================================
#
#  Jose Ignacio Galarza (igalarzab)
#  <igalarzab@gmail.com>
#  http://sysvar.net
#

import sys


def solve(surprising, minimum, marks):
    awesome_googlers = 0

    for mark in marks:
        base, rest = (mark // 3, mark % 3)

        if rest == 0:
            if base >= minimum:
                awesome_googlers += 1
            elif base > 0 and (base + 1) >= minimum and surprising:
                surprising -= 1
                awesome_googlers += 1
        elif rest == 1:
            if (base + 1) >= minimum:
                awesome_googlers += 1
        elif rest == 2:
            if (base + 1) >= minimum:
                awesome_googlers += 1
            elif (base + 2) >= minimum and surprising:
                surprising -= 1
                awesome_googlers += 1

    return awesome_googlers


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        line = sys.stdin.readline().split()[1:]
        print("Case #%d: %d" % (i + 1,
            solve(int(line[0]), int(line[1]), map(int, line[2:]))))

# vim: ai ts=4 sts=4 et sw=4
