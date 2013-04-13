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
    matches = 0

    for num in xrange(start, end + 1):
        str_num = str(num)
        # Check if it's a palindrome
        if str_num == str_num[::-1]:
            sqrnum = math.sqrt(num)

            # Check if it's a square
            if sqrnum % 1 == 0:
                str_sqrnum = str(int(sqrnum))

                # Check if the square is a palindrome
                if str_sqrnum == str_sqrnum[::-1]:
                    matches += 1

    return matches


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        nstart, nend = map(int, sys.stdin.readline().split())
        print("Case #{0}: {1}".format(i + 1, solve(nstart, nend)))

# vim: ai ts=4 sts=4 et sw=4
