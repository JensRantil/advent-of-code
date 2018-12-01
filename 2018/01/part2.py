#!env python
import sys
import itertools

seen_before = set()
s = 0
with open(sys.argv[1]) as f:
    lines = [int(line) for line in f]

for line in itertools.cycle(lines):
    seen_before.add(s)
    s += line
    print line, s, len(seen_before)
    if s in seen_before:
        print "Answer:", s
        break
else:
    print "Found no duplicate."
