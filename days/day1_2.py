from base import *


digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_ints = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def process(i, line):
    found = {}
    for i, char in enumerate(line[::1]):
        if char.isdigit():
            found[i] = char
            break
    for i, char in enumerate(line[::-1]):
        if char.isdigit():
            found[len(line) - 1 - i] = char
            break
    for str in digit_strings:
        j = line.find(str)
        if j > -1:
            found[j] = digit_ints[str]
        j = line.rfind(str)
        if j > -1:
            found[j] = digit_ints[str]

    return found[min(found, key=int)], found[max(found, key=int)]


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
