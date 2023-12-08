from base import *


path = []
dsts = {}


def process(i, line):
    global path, dsts
    if i == 0:
        path = [c for c in line]
    elif line:
        src, dst = line.split(" = ")
        l, r = dst[1:len(dst)-1].split(", ")
        dsts[src] = {"L": l, "R": r}
    return None


def final(results: list):
    global path, dsts
    i = 0
    f = "AAA"
    while f != "ZZZ":
        j = i % (len(path))
        f = dsts[f][path[j]]
        i = i + 1
    return i


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
