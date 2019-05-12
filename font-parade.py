#!/usr/bin/env python

import sys

if __name__ == '__main__':
    fns = []
    for line in sys.stdin:
        if line.startswith('Fandol'):
            continue
        rec = line.split(',')
        fc = rec[0].rstrip().lstrip()
        fn = '' if len(rec)== 1 else rec[1].rstrip().lstrip()
        fns.append((fc, fn))

    fns.sort()
    for fn in set(fns):
        print('%s & %s & \\Large \\CJKfontspec{%s} xxx \\\\' % (fn[1], fn[0], fn[0]))
