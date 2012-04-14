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

transform = {
    'a': 'y', 'b': 'h', 'c': 'e', 'd': 's',
    'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x',
    'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g',
    'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r',
    'q': 'z', 'r': 't', 's': 'n', 't': 'w',
    'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
    'y': 'a', 'z': 'q', ' ': ' '}


def solve(sentence):
    new = [transform[letter] for letter in sentence]
    return ''.join(new)


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        sentence = sys.stdin.readline()[:-1]
        print("Case #%d: %s" % (i + 1, solve(sentence)))

# vim: ai ts=4 sts=4 et sw=4
