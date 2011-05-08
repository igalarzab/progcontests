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

def solve(numbers):
    errors = 0

    for i in xrange(len(numbers)):
        if numbers[i] != i+1:
            errors += 1

    return errors


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        nnumbers = int(sys.stdin.readline()) # Ignore :P
        numbers = map(int, sys.stdin.readline().split())
        print("Case #%d: %.6f" % (i+1, solve(numbers)))

# vim: ai ts=4 sts=4 et sw=4
