from base import *


def process(i, line):
	return line.split(",")


def _hash(s):
	t = 0
	for c in s:
		a = int(ord(c))
		c = (int)
		t += a
		t *= 17
		t = t % 256
	return t


def final(results: list):
	results = results[0]

	boxes = [dict() for _ in range(256)]
	for step in results:
		match step.strip('-').split('='):
			case [l, f]: boxes[_hash(l)][l] = int(f)
			case [l]:    boxes[_hash(l)].pop(l, 0)

	total = 0
	for i, b in enumerate(boxes, 1):
		vals = b.values()
		for j, f in enumerate(vals, 1):
			total += i * j * f
	return total


print(
	do_func_for_each_line_in_file(
		f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
		process,
		final,
	)
)
