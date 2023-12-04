from base import *
import re


NOT_SYMBOL_LIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
W = 140
H = 140


matrix = Matrix(W, H)


def process(i, line):
    for j, char in enumerate(line):
        matrix.set_value(i, j, char)


def final(_):
    result = 0
    for i in range(W):
        row = matrix.get_row(i)
        for m in re.finditer('\d{1,3}', row):
            start, end, is_valid = m.start(0), m.end(0), False
            for j in range(start - 1, end + 2):
                if i > 0 and j < H and j >= 0:
                    if matrix.get_value(i - 1, j) not in NOT_SYMBOL_LIST:
                        is_valid = True
                        break
                if i < W - 1 and j < H and j >= 0:
                    if matrix.get_value(i + 1, j) not in NOT_SYMBOL_LIST:
                        is_valid = True
                        break
            
            if start > 0 and matrix.get_value(i, start - 1) not in NOT_SYMBOL_LIST:
                is_valid = True
            if end < H and matrix.get_value(i, end) not in NOT_SYMBOL_LIST:
                is_valid = True

            if is_valid:
                result += int(m.group())
    return result


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
