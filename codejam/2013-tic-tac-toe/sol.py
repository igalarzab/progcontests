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
from collections import Counter


def solve(game):
    finished = True

    checks = (
        # Rows
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((1, 0), (1, 1), (1, 2), (1, 3)),
        ((2, 0), (2, 1), (2, 2), (2, 3)),
        ((3, 0), (3, 1), (3, 2), (3, 3)),
        # Cols
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((0, 1), (1, 1), (2, 1), (3, 1)),
        ((0, 2), (1, 2), (2, 2), (3, 2)),
        ((0, 3), (1, 3), (2, 3), (3, 3)),
        # Diagonal
        ((0, 0), (1, 1), (2, 2), (3, 3)),
        ((0, 3), (1, 2), (2, 1), (3, 0)),
    )

    # Check rows
    for check in checks:

        c = Counter()
        for pair in check:
            c[game[pair[0]][pair[1]]] += 1

        letter = c.most_common(1)[0]

        if '.' in c:
            finished = False

        if letter[0] == 'X':
            if letter[1] == 4 or letter[1] == 3 and 'T' in c:
                return 'X won'
        elif letter[0] == 'O':
            if letter[1] == 4 or letter[1] == 3 and 'T' in c:
                return 'O won'

    if finished:
        return 'Draw'
    else:
        return 'Game has not completed'


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        xgame = []

        for _ in xrange(4):
            xgame.append(list(sys.stdin.readline().strip()))

        # Empty line
        sys.stdin.readline()

        print('Case #{0}: {1}'.format(i + 1, solve(xgame)))

# vim: ai ts=4 sts=4 et sw=4
