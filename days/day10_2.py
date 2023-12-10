from base import *


inp = []
m = {}
s = ""


def process(i, line):
	global m, s
	for j, c in enumerate(line):
		if c == "S":
			s = (i, j)
		m[i, j] = c
	inp.append([l for l in line])


def pipe(c, i, j):
	match c:
		case '-': return (i, j - 1), (i, j + 1)
		case '|': return (i - 1, j), (i + 1, j)
		case 'L': return (i - 1, j), (i, j + 1)
		case 'J': return (i - 1, j), (i, j - 1)
		case '7': return (i + 1, j), (i, j - 1)
		case 'F': return (i + 1, j), (i, j + 1)
		case _: return (i, j), (i, j)


def con_to(pt):
    return set(pipe(m[*pt], *pt))


def final(results: list):
	global m, s

	end1, end2 = 0, 0
	bla = []
	for di, dj in ((-1, 0), (0, 1), (0, -1), (1, 0)):
		pt = (s[0] + di, s[1] + dj)
		if pt in m and s in con_to(pt):
			bla.append(pt)
	end1, end2 = bla


	for c in '-LJ7F|':
		if set(pipe(c, *s)) == set([end1, end2]):
			m[s] = c

	visited, steps = set([s, end1, end2]), 1
	while end1 != end2:
		end1 = (con_to(end1) - visited).pop()
		end2 = (con_to(end2) - visited).pop()
		visited |= set([end1, end2])

	enclosed = 0
	for i in range(len(inp)):
		inside = False
		for j in range(len(inp[0])):
			if (i, j) in visited:
				if m[i, j] in '|LJ':
					inside = not inside
				continue
			if inside:
				enclosed += 1
	return enclosed


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
