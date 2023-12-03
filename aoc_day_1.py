import regex as re


def txt_loader(file_path: str) -> list:
    with open(file_path) as f:
        return f.readlines()


mapper = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
number_strings = list(mapper.keys())


def extract_digits(input_string: str,
                   include_number_strings: bool = False) -> list:
    if include_number_strings is False:
        return [int(i) for i in input_string if i.isdigit()]
    else:
        pattern = r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)'
        matches = re.findall(pattern, input_string, overlapped=True)
        matches = [int(mapper[i]) if i in mapper.keys() else int(i) for i in matches]
        return matches


def combine_first_and_last_digits_in_list(input_list: list) -> int:
    return int(str(input_list[0]) + str(input_list[-1]))


def main_day_1(file_path: str,
               include_number_strings: bool = False) -> int:
    lines_list = txt_loader(file_path)
    total_sum = 0
    for line in lines_list:
        digits_list = extract_digits(line, include_number_strings=include_number_strings)
        total_sum += combine_first_and_last_digits_in_list(digits_list)
    return total_sum


if __name__ == '__main__':
    print(main_day_1("data/input.txt"))
    print(main_day_1("data/input.txt", include_number_strings=True))

