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


def solve(N, M):
    found = set([])

    for number in xrange(N, M + 1):
        snumber = str(number)
        for i in xrange(1, len(snumber)):
            snumber = snumber[1:] + snumber[0]
            inumber = int(snumber, 10)
            if number < inumber and N <= inumber <= M:
                found.add((number, inumber))

    return len(found)


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        N, M = map(int, sys.stdin.readline().split())
        print("Case #%d: %d" % (i + 1, solve(N, M)))

# vim: ai ts=4 sts=4 et sw=4
