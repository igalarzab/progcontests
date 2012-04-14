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


def solve(reductions, deletions, letters):
    s = letters[0]
    i = 1

    while i < len(letters):
        s += letters[i]
        make_reductions = True

        # First, all the possible reductions
        try:
            while make_reductions:
                if s[-1] + s[-2] in reductions:
                    s = s[:-2] + reductions[s[-1] + s[-2]]
                elif s[-2] + s[-1] in reductions:
                    s = s[:-2] + reductions[s[-2] + s[-1]]
                else:
                    make_reductions = False
        except:
            pass

        # Now, the possible deletions
        for deletion in deletions:
            if deletion[0] in s and deletion[1] in s:
                try:
                    i += 1
                    s = letters[i]
                except:
                    s = ''
                break

        i += 1

    # Convert format
    r = str([str(i) for i in s])
    return r.replace("'", "")


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        line = sys.stdin.readline().split()
        reductions = {}
        deletions = []

        for j in xrange(1, int(line[0]) + 1):
            reductions[line[j][0:2]] = line[j][2]

        offset = 1 + int(line[0])
        for j in xrange(offset + 1, offset + int(line[offset]) + 1):
            deletions.append(line[j])

        offset += 1 + int(line[offset])
        print("Case #%d: %s" % (i + 1,
            solve(reductions, deletions, line[offset + 1])))

# vim: ai ts=4 sts=4 et sw=4
