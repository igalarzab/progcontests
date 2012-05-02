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


def solve(R, k, G, groups):
    person, amount, gasoline, cycle = (0, 0, 0, [])

    # Create the possible cycles
    for race in xrange(G):
        while (person != race or amount == 0) and amount + groups[person] <= k:
            amount += groups[person]
            person = (person + 1) % G

        cycle.append((person, amount))
        amount -= groups[race]

    person, race, cache = (0, 0, {})

    # Run the race
    while race < R:
        gasoline += cycle[person][1]
        person = cycle[person][0]
        race += 1

        if person in cache:
            i, amount = cache[person]
            mult = (R - i) / (race - i)
            race = i + (mult * (race - i))
            gasoline = amount + (mult * (gasoline - amount))
        else:
            cache[person] = (race, gasoline)

    return gasoline


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        R, k, G = map(int, sys.stdin.readline().split())
        groups = map(int, sys.stdin.readline().split())
        assert G == len(groups)
        print(solve(R, k, G, groups))

# vim: ai ts=4 sts=4 et sw=4
