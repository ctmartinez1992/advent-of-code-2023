from base import *
from itertools import chain


with open('inputs/day14_2.txt') as f:
    txt = f.read()

grid = txt.replace('\n', '')
lines = txt.split('\n')
width, height = len(lines[0]), len(lines)

	
def reorder(sub, direction):
    return ''.join(reversed(sorted(sub)) if direction in 'nw' else sorted(sub))


def one_direction(grid, direction):
    if direction in 'ns':
        columns = [grid[i::height] for i in range(width)]
        for e,c in enumerate(columns):
            columns[e] = '#'.join(reorder(subc, direction) for subc in c.split('#'))
        return ''.join(chain(*zip(*columns)))
    else:   # we
        rows = [grid[i*width:(i+1)*width] for i in range(height)]
        for e,r in enumerate(rows):
            rows[e] = '#'.join(reorder(subr, direction) for subr in r.split('#'))
        return ''.join(rows)
	

def load(grid):
    columns = [grid[i::height] for i in range(width)]
    return sum(sum(i for i,c in zip(range(len(col), 0, -1), col) if c == 'O') for col in columns)


cycle = 0
goal = 1000000000
cycle_cache = {}
found_cycle = False

while cycle < goal:
    for d in 'nwse':
        grid = one_direction(grid, d)
    cycle += 1

    if not found_cycle and (found_cycle := grid in cycle_cache):
        cycle_length = cycle - cycle_cache[grid]
        cycle += cycle_length * ((goal - cycle) // cycle_length)
    else:
        cycle_cache[grid] = cycle

print(load(grid))