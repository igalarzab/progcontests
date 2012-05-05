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

MOVS = {'V': 300, 'H': 200, 'D': 350, 'P': 100, 'WAIT': 500}

POS = {'0': (4, 2), 'CAPS': (4, 3)}
POS.update(dict.fromkeys([' ', '1'], (1, 1)))
POS.update(dict.fromkeys(['a', 'b', 'c', '2'], (1, 2)))
POS.update(dict.fromkeys(['d', 'e', 'f', '3'], (1, 3)))
POS.update(dict.fromkeys(['g', 'h', 'i', '4'], (2, 1)))
POS.update(dict.fromkeys(['j', 'k', 'l', '5'], (2, 2)))
POS.update(dict.fromkeys(['m', 'n', 'o', '6'], (2, 3)))
POS.update(dict.fromkeys(['p', 'q', 'r', 's', '7'], (3, 1)))
POS.update(dict.fromkeys(['t', 'u', 'v', '8'], (3, 2)))
POS.update(dict.fromkeys(['w', 'x', 'y', 'z', '9'], (3, 3)))

PUL = {'7': 5, '9': 5}
PUL.update(dict.fromkeys(['0', ' ', 'CAPS', 'a', 'd', 'g', 'j', 'm', 'p', 't', 'w'], 1))
PUL.update(dict.fromkeys(['1', 'b', 'e', 'h', 'k', 'n', 'q', 'u', 'x'], 2))
PUL.update(dict.fromkeys(['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y'], 3))
PUL.update(dict.fromkeys(['2', '3', '4', '5', '6', '8', 's', 'z'], 4))


def move(actual, obj):
    time = 0
    diff = map(abs, (actual[0] - obj[0], actual[1] - obj[1]))

    # Diagonal
    if diff[0] != 0 and diff[1] != 0:
        minn = min(diff[0], diff[1])
        diff = (diff[0] - minn, diff[1] - minn)
        time += minn * MOVS['D']

    time += diff[0] * MOVS['V']  # Vertical
    time += diff[1] * MOVS['H']  # Horizontal
    return time


def solve(text):
    time, upper = 0, False
    actual = (4, 2)

    for letter in text:
        if letter.lower() not in POS:
            continue

        # Check if we have to change the CAPS
        if upper != letter.isupper():
            time += move(actual, POS['CAPS'])
            time += MOVS['P'] * PUL['CAPS']
            actual, upper = POS['CAPS'], not upper

        pos = POS[letter.lower()]
        time += move(actual, pos)
        time += MOVS['P'] * PUL[letter.lower()]
        if actual == pos:
            time += MOVS['WAIT']
        actual = pos

    return time


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        text = sys.stdin.readline().rstrip('\n')
        print(solve(text))

# vim: ai ts=4 sts=4 et sw=4
