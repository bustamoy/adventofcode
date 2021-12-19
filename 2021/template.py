# Advent Of Code
# https://adventofcode.com/2021/day/{DAY}
# https://adventofcode.com/2021/day/{DAY}#part2
# (NOT) COMPLETE

from typing import List

YEAR: int = 2021
DAY: int = 0


def get_input() -> List[str]:
    filename = f'input-{YEAR}-{DAY}'
    from os.path import exists
    if exists(filename):
        with open(filename, 'r') as input_file:
            return input_file.read().splitlines()
    else:
        raise FileNotFoundError(f"Did not find input file: '{filename}'.")


def process_data(data: List[str]) -> List:
    return None


def part_one(data: List[str]) -> int:
    return 0


def part_two(data: List[str]) -> int:
    return 0


def main():
    example = ['']
    # input_data = get_input()

    assert part_one(example)
    # print(f'Part 1 Answer:\n{part_one(input_data)}')

    # assert part_two(example)
    # print(f'Part 2 Answer:\n{part_two(input_data)}')


if __name__ == '__main__':
    main()
