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


def solve(start, end):
    real_start = int(math.ceil(math.sqrt(start)))
    real_end = int(math.ceil(math.sqrt(end)))
    matches = 0

    for num in xrange(real_start, real_end + 1):
        str_num = str(num)
        if str_num == str_num[::-1]:
            twice = num * num
            stwice = str(twice)
            if twice <= end and stwice == stwice[::-1]:
                matches += 1

    return matches


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        nstart, nend = map(int, sys.stdin.readline().split())
        for _ in xrange(10000):
            print("Case #{0}: {1}".format(i + 1, solve(nstart, nend)))

# vim: ai ts=4 sts=4 et sw=4
