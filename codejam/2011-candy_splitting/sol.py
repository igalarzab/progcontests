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


def solve(movements):
    if reduce(lambda x, y: x ^ y, movements):
        return "NO"

    movements.sort()
    return str(sum(movements[1:]))


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        ncandies = int(sys.stdin.readline())  # Ignore :P
        candies = map(int, sys.stdin.readline().split())
        print("Case #%d: %s" % (i + 1, solve(candies)))

# vim: ai ts=4 sts=4 et sw=4
