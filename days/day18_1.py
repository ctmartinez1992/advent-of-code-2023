data = open("inputs/day18_1.txt", "r").read().strip().split("\n")
dirs = {"0": "R", "1": "D", "2": "L", "3": "U"}
moves = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

x, y, borders = 0, 0, []
for row in data:
    d, m, _ = row.split()
    dx, dy = moves[d]
    for _ in range(int(m) ):
        borders.append( (x, y) )
        x, y = x + dx, y + dy

area = 0
for i in range(len(borders) - 1):
    x1, y1 = borders[i]
    x2, y2 = borders[i + 1]
    area += x1 * y2 - x2 * y1

per = len(borders)
i_area = abs(area) // 2 - per // 2 + 1

print(i_area + per)