data = open('inputs/day18_2.txt', 'r').read().strip().split('\n')
dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

x = y = perimeter = 0
borders = []
for row in data:
    a, b, c = row.split()
    c = c[1:-1]
    (dx, dy), m = move[dirs[c[-1]]], int(c[1:-1], 16)
    borders.append((x, y))
    perimeter += m
    x += dx * m
    y += dy * m

area = 0
for i in range(len(borders) - 1):
    x1, y1 = borders[i]
    x2, y2 = borders[i + 1]
    area += x1 * y2 - x2 * y1
area = abs(area) // 2

print((area - perimeter // 2 + 1) + perimeter)
