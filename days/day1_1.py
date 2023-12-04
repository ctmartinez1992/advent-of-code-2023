from base import *


def process(line):
    first = 0
    for char in line[::1]:
        if char.isdigit():
            first = char
    last = 0
    for char in line[::-1]:
        if char.isdigit():
            last = char
    return first, last


def final(values):
    result = 0
    for first, last in values:
        result += int(f"{first}{last}")
    return result


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
