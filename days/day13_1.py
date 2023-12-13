from base import *

from collections import defaultdict


def bset(lines):
	s = set()
	for r, line in enumerate(lines):
		for c, char in enumerate(line):
			s.add((r, c, char))
	return s


def mirror(pattern, index):
	part1, part2 = zip(*zip(pattern[index:], reversed(pattern[:index])))
	return len(bset(part1) - bset(part2))


def solve():
	patterns = [pattern.splitlines() for pattern in open("inputs/day13_1.txt").read().split("\n\n")]
	summary = defaultdict(int)
	for pat in patterns:
		for mult, pattern in [(100, pat), (1, list(zip(*pat)))]:
			for index in range(1, len(pattern)):
				summary[mirror(pattern, index)] += mult * index
	return summary[0]
	
print(solve())
