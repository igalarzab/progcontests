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
import math


def solve(N):
    if N == 1 or N == 2:
        return N
    elif N < 1:
        return 0

    maximun = pow(2, int(math.log(N - 1, 2))) - 1

    x = format(maximun, 'b')
    y = format(N - maximun, 'b')

    return x.count('1') + y.count('1')


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        try:
            N = int(sys.stdin.readline())
        except ValueError:
            N = 0

        print("Case #%d: %d" % (i + 1, solve(N)))

# vim: ai ts=4 sts=4 et sw=4
