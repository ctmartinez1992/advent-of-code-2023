from base import *


m = {}
rocks = []
h_row, h_col = 0, 0


def process(i, line):
	global m, rocks, h_row, h_col

	for j, c in enumerate(line):
		if c == "O":
			rocks.append((i, j))
		m[i, j] = c
		h_col = j + 1
	h_row = i + 1


def print_map():
	global m, h_row, h_col

	for i in range(h_row):
		for j in range(h_col):
			print(m[i, j], end="")
		print("")
	print("")


def final(results: list):
	global m, rocks, h_col

	for ir, jr in rocks:
		for i in range(ir - 1, -1, -1):
			if m[i, jr] == "#" or m[i, jr] == "O":
				break
			if m[i, jr] == ".":
				swap = m[i, jr]
				m[i, jr] = m[ir, jr]
				m[ir, jr] = swap

				ir = ir - 1

	total = 0
	for i, j in m.keys():
		if m[i, j] == "O":
			total += h_row - i

	return total


print(
	do_func_for_each_line_in_file(
		f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
		process,
		final,
	)
)
