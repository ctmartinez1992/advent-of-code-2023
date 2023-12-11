from base import *
from itertools import accumulate, combinations


m = []
global l


def process(i, line):
	result = []
	for j, c in enumerate(line):
		if c == '#':
			result.append((i, j))
	return result


def dist(ps):
	calc = []
	for p in range(max(ps) + 1):
		calc.append((1000000, 1)[p in ps])
	exp = list(accumulate(calc))

	comb = []
	for a, b in combinations(ps, 2):
		comb.append(abs(exp[a]-exp[b]))
	return sum(comb)


def final(results: list):
	final = []
	for r in results:
		final.extend(r)

	return sum(map(dist, zip(*final)))


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
