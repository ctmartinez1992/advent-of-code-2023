from base import *
import re
from collections import defaultdict


NOT_SYMBOL_LIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
W = 140
H = 140


matrix = Matrix(W, H)


def process(i, line):
    for j, char in enumerate(line):
        matrix.set_value(i, j, char)


def final(_):
    found = defaultdict(list)

    for i in range(W):
        row = matrix.get_row(i)
        for m in re.finditer('\d{1,3}', row):
            start, end, is_valid = m.start(0), m.end(0), False
            for j in range(start - 1, end + 1):
                if i > 0 and j < H and j >= 0:
                    if matrix.get_value(i - 1, j) == "*":
                        is_valid = i - 1, j
                        break
                if i < W - 1 and j < H and j >= 0:
                    if matrix.get_value(i + 1, j) == "*":
                        is_valid = i + 1, j
                        break
            
            if start > 0 and matrix.get_value(i, start - 1) == "*":
                is_valid = i, start - 1
            if end < H and matrix.get_value(i, end) == "*":
                is_valid = i, end

            if is_valid:
                found[is_valid].append(int(m.group()))

    result = 0
    for k, v in found.items():
        if len(v) == 2:
            result += v[0] * v[1]
    return result


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
