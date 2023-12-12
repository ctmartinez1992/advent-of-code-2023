from base import *


cache = {}


def combinations_and_cache(string, config):
	if (string, tuple(config)) in cache:
		return cache[(string, tuple(config))]
	if len(config) == 0:
		return 1 if "#" not in string else 0

	total, size = 0, config[0]
	for i in range(len(string)):
		if (
			i + size <= len(string)
			and all(c != "." for c in string[i : i + size])
			and (i == 0 or string[i - 1] != "#")
			and (i + size == len(string) or string[i + size] != "#")
		):
			total += combinations_and_cache(string[i + size + 1 :], config[1:])

		if string[i] == "#":
			break

	cache[(string, tuple(config))] = total

	return total



def process(i, line):
	string, config = line.split(" ")
	config = list(map(int, config.split(",")))

	return string, config


def final(results: list):
	total = 0
	for r in results:
		string, config = r
		total += combinations_and_cache(string, config)
	return total


print(
	do_func_for_each_line_in_file(
		f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
		process,
		final,
	)
)
