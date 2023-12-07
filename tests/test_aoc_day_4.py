from aoc_day_4 import load_and_parse_txt_lines, Scratchcard


def test_load_and_parse_txt_lines():
    expected = Scratchcard([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])
    full_output = load_and_parse_txt_lines("fixtures/test_fixture_day_4.txt")
    assert full_output[0] == expected
