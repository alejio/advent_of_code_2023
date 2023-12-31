from dataclasses import dataclass

import regex as re


@dataclass
class Game:
    game_number: int
    reds: list
    blues: list
    greens: list

    def max_of_reds(self) -> int:
        return max(self.reds)

    def max_of_blues(self) -> int:
        return max(self.blues)

    def max_of_greens(self) -> int:
        return max(self.greens)


def load_and_parse_games(input_file: str) -> list[Game]:
    # regex for game: ^Game (\d+)\:.*
    # regex for blue \d+ blue
    games = []
    with open(input_file) as input_file:
        lines = input_file.readlines()
        for line in lines:
            game_match = re.findall(r'^Game (\d+)\:.*', line)
            game = int(game_match[0])
            blue_matches = re.findall(r'(\d+) blue', line)
            if len(blue_matches) == 0:
                blues = [0]
            else:
                blues = [int(i) for i in blue_matches]
            red_matches = re.findall(r'(\d+) red', line)
            if len(red_matches) == 0:
                reds = [0]
            else:
                reds = [int(i) for i in red_matches]
            green_matches = re.findall(r'(\d+) green', line)
            if len(green_matches) == 0:
                greens = [0]
            else:
                greens = [int(i) for i in green_matches]
            games.append(Game(game, reds, blues, greens))
    return games


def check_game_is_valid(game: Game, constraint_red: int, constraint_blue: int, constraint_green: int) -> bool:
    reds = game.max_of_reds()
    blues = game.max_of_blues()
    greens = game.max_of_greens()
    if reds <= constraint_red and blues <= constraint_blue and greens <= constraint_green:
        return True
    else:
        return False


def calculate_power_of_set_of_cubes(n_reds: int, n_blues: int, n_greens: int) -> int:
    return n_reds * n_blues * n_greens


def calculate_minimum_set_of_cubes(game: Game) -> dict:
    reds = game.max_of_reds()
    blues = game.max_of_blues()
    greens = game.max_of_greens()
    return {"reds": reds, "blues": blues, "greens": greens}


def main_day_2(input_file: str) -> tuple[int, int]:
    games = load_and_parse_games(input_file)
    sum_of_valid_game_ids = 0
    sum_of_minimum_set_powers = 0
    for game in games:
        if check_game_is_valid(game, 12, 14, 13):
            sum_of_valid_game_ids += game.game_number
        minimum_set = calculate_minimum_set_of_cubes(game)
        sum_of_minimum_set_powers += calculate_power_of_set_of_cubes(n_reds=minimum_set["reds"],
                                        n_blues=minimum_set["blues"],
                                        n_greens=minimum_set["greens"])
    return sum_of_valid_game_ids, sum_of_minimum_set_powers


if __name__ == "__main__":
    print(main_day_2("data/input_day_2.txt"))