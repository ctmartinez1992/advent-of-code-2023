from base import *


red_limit = 12
green_limit = 13
blue_limit = 14


def process(i, line):
    game_string = line.split(": ")
    game_id = int(game_string[0].split("Game ")[1])

    r, g, b = 0, 0, 0

    configs = game_string[1].split("; ")
    for config in configs:
        cubes = config.split(", ")
        for cube in cubes:
            cube_value, cube_name = cube.split(" ")
            if "red" in cube_name:
                if int(cube_value) > r:
                    r = int(cube_value)
            if "green" in cube_name:
                if int(cube_value) > g:
                    g = int(cube_value)
            if "blue" in cube_name:
                if int(cube_value) > b:
                    b = int(cube_value)

    return game_id, r, g, b


def final(values):
    result = 0
    for game_id, r, g, b in values:
        result += r * g * b
    return result


print(
    do_func_for_each_line_in_file(
        f"inputs/{Path(os.path.basename(__file__)).stem}.txt",
        process,
        final,
    )
)
