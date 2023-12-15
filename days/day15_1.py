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

	total = 0
	for string in results:
		total += _hash(string)
	return total


print(
	do_func_for_each_line_in_file(
		f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
		process,
		final,
	)
)
