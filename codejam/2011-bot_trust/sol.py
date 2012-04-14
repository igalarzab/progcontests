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
    copy = movements[:]
    blue, orange = ([], [])
    mblue, morange = (False, False)
    bpos, opos = (1, 1)
    steps = 0

    # Two lists with separate movements
    for i in xrange(len(movements)):
        if movements[i][0] == 'B':
            blue.append(i)
        else:
            orange.append(i)

    while copy:
        # Blue movement
        if blue and bpos < movements[blue[0]][1]:
            bpos += 1
        elif blue and bpos > movements[blue[0]][1]:
            bpos -= 1
        else:  # ==
            if copy and copy[0][0] == 'B':
                mblue = True

        # Orange movement
        if orange and opos < movements[orange[0]][1]:
            opos += 1
        elif orange and opos > movements[orange[0]][1]:
            opos -= 1
        else:
            if copy and copy[0][0] == 'O':
                morange = True

        steps += 1

        # Blue pulse button
        if mblue:
            mblue = False
            copy.pop(0)
            blue.pop(0)

        # Orange pulse button
        if morange:
            morange = False
            copy.pop(0)
            orange.pop(0)

    return steps


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        line = sys.stdin.readline().split()[1:]
        movs = [(line[j], int(line[j + 1])) for j in xrange(0, len(line), 2)]
        print("Case #%d: %d" % (i + 1, solve(movs)))

# vim: ai ts=4 sts=4 et sw=4
