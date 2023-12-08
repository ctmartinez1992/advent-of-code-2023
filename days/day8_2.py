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


def is_over(follow):
    for f in follow:
        if f[-1] != "Z":
            return False
    return True


def final(results: list):
    global path, dsts
    i = 0

    follow = []
    for d in dsts.keys():
        if d[-1] == "A":
            follow.append(d)

    while not is_over(follow):
        finish = []

        j = i % (len(path))
        for f in follow:
            finish.append(dsts[f][path[j]])
        i = i + 1
        follow = finish
    return i


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
