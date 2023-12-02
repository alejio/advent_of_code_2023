import re


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


def replace_number_strings_with_digits(input_string: str) -> str:
    matches = re.findall(r"(?=("+'|'.join(number_strings)+r"))", input_string)
    if len(matches) == 0:
        return input_string
    elif len(matches) == 1:
        return input_string.replace(matches[0], str(mapper[matches[0]]))
    else:
        if len(set(matches)) == 1:
            return input_string.replace(matches[0], str(mapper[matches[0]]))
        else:
            return input_string.replace(matches[0], str(mapper[matches[0]])).replace(matches[-1], str(mapper[matches[-1]]))


def extract_digits(input_string: str) -> list:
    return [int(i) for i in input_string if i.isdigit()]


def combine_first_and_last_digits_in_list(input_list: list) -> int:
    return int(str(input_list[0]) + str(input_list[-1]))


def main_day_1(file_path: str,
               replace_number_strings: bool=False) -> int:
    lines_list = txt_loader(file_path)
    total_sum = 0
    for line in lines_list:
        if replace_number_strings:
            line = replace_number_strings_with_digits(line)
        digits_list = extract_digits(line)
        total_sum += combine_first_and_last_digits_in_list(digits_list)
    return total_sum


if __name__ == '__main__':
    print(main_day_1("data/input.txt"))
    print(main_day_1("data/input.txt", replace_number_strings=True))

