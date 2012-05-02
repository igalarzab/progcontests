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
from operator import itemgetter


def solve(samples):
    winner = (0, 0, 0)
    maxx = (0, 0)
    biggest = 0

    # First create an ordered list to not traverse the hole list always
    ordered = sorted(
        [(i, samples[i]) for i in xrange(len(samples))],
        key=itemgetter(1)
    )

    # Then look for the biggest difference
    for i in xrange(len(samples)):
        while i > maxx[0]:
            maxx = ordered.pop()

        diff = maxx[1] - samples[i]
        if diff > biggest:
            biggest = diff
            winner = (i, maxx[0], diff)

    return winner[0] * 100, winner[1] * 100, winner[2]


if __name__ == '__main__':
    samples = []

    for i in sys.stdin.readlines():
        try:
            samples.append(int(i))
        except ValueError:
            pass

    print('%d %d %d' % solve(samples))

# vim: ai ts=4 sts=4 et sw=4
