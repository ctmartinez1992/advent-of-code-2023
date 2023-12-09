from base import *
from math import comb


def process(i, line):
    return [int(n) for n in line.split(" ")]


def bin(ns):
    n, result = len(ns), 0
    for i, x in enumerate(ns):
        bin_coeff = (x * comb(n, i))
        result += bin_coeff * ((-1) ** (n - 1 - i))
    return result


def final(results: list):
    calc = 0
    for r in results:
        calc += bin(r)
    return calc


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
