from aoc_day_2 import main_day_2, load_and_parse_games, check_game_is_valid


def test_load_and_parse_games():
    games = load_and_parse_games("fixtures/test_fixture_day_2.txt")
    assert len(games) == 5
    assert games[0].game_number == 1
    assert games[0].reds == [4, 1]
    assert games[0].blues == [3, 6]
    assert games[0].greens == [2, 2]


def test_check_game_is_valid():
    games = load_and_parse_games("fixtures/test_fixture_day_2.txt")
    assert check_game_is_valid(games[0], 12, 14, 13) is True
    assert check_game_is_valid(games[1], 12, 14, 13) is True
    assert check_game_is_valid(games[4], 12, 14, 13) is True
    assert check_game_is_valid(games[2], 12, 14, 13) is False
    assert check_game_is_valid(games[3], 12, 14, 13) is False


def test_main_day_2():
    assert main_day_2("fixtures/test_fixture_day_2.txt") == 8