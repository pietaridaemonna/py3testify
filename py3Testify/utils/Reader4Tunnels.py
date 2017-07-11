#!/usr/bin/python3


def read_file():
    with open('../../data.txt') as f: lines = [line.rstrip('\n') for line in f]
    return lines


def parse_jumps():
    return 42

f = read_file()
print(f)
