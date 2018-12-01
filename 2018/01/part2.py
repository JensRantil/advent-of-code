#!env python
import sys
import itertools

with open(sys.argv[1]) as f:
    lines = itertools.cycle(f)
    lines = itertools.imap(int, lines)

    def accumulator(i):
        s = 0
        for e in i:
            yield s
            s += e
    lines = (e for e in accumulator(lines))

    seen_before = set()
    def pred(e):
        res = e in seen_before
        seen_before.add(e)
        return not res

    lines = itertools.dropwhile(pred, lines)
    lines = itertools.islice(lines, 1)

    print list(lines)[0]
