#!/usr/bin/env python3

import sys

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
    value = line.strip()
    print(value)

