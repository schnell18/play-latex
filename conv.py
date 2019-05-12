#!/usr/bin/env python

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        print('%s \\\\' % ' & '.join([ '\\colorcard{%s}' % x for x in line.split()]))
