from base import 


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


def final(results):
    final = 0
    for result in results:
        card_result = 0
        game_id, winning_numbers, card_numbers = result
        for n in card_numbers:
            if n in winning_numbers:
                if card_result == 0:
                    card_result = 1
                else:
                    card_result = card_result * 2
        final += card_result
    return final


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
