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
    game_string, number_string = line.split(":")
    game_id = int(game_string[5:8])
    winning_string, number_string = number_string.split("|")

    return game_id, get_all_numbers(winning_string), get_all_numbers(number_string)


def final(results: list):
    scratchcards = defaultdict(lambda: 1)
    for result in results:
        game_id, winning_numbers, card_numbers = result

        for i in range(scratchcards[game_id]):
            id_won = game_id + 1
            for n in card_numbers:
                if n in winning_numbers:
                    scratchcards[id_won] += 1
                    id_won += 1
                
    return sum(scratchcards.values())


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
