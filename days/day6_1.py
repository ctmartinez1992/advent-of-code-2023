from base import *
from collections import defaultdict


def get_all_numbers(line):
    numbers = []
    splitted = line.split("  ")
    for split in splitted:
        final = split.split(" ")
        numbers.extend([int(f) for f in final if f])
    return numbers


def process(i, line):
    results = []
    splitted = line.split(" ")
    for s in splitted:
        try:
            r = int(s)
            results.append(r)
        except:
            pass
    return results


def final(results: list):
    possibilities = []
    times, distances = results
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]

        beats = 0
        for j in range(1, time, 1):
            time_left = time - j
            speed = j
            distance_done = time_left * speed
            if distance_done > distance:
                beats = beats + 1
        possibilities.append(beats)

    product = 1
    for num in possibilities:
        product *= num
    return product


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
