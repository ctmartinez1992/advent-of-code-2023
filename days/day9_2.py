from base import *


def process(i, line):
    return [int(n) for n in line.split(" ")]


def rev(ns):
	if sum(n != 0 for n in ns) == 0:
		return 0
      
	m = []
	for i in range(len(ns) - 1):
		m.append(ns[i + 1] - ns[i])
	return ns[-1] + rev(m)


def final(results: list):
	calc = 0
	for r in results:
		calc += rev(r[::-1])
	return calc


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
