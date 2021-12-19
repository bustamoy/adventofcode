# Advent Of Code
# https://adventofcode.com/2021/day/6
# https://adventofcode.com/2021/day/6#part2
# COMPLETE

from os.path import exists
from typing import List

YEAR: int = 2021
DAY: int = 6


def get_input() -> List[str]:
    filename = f'input-{YEAR}-{DAY}'
    if exists(filename):
        with open(filename, 'r') as input_file:
            return input_file.read().splitlines()
    else:
        raise FileNotFoundError(f"Did not find input file: '{filename}'.")


def process_data(data: List[str]) -> List[int]:
    return [int(f) for f in data[0].split(',')]


def part_one(data: List[int], days: int) -> int:
    fish = process_data(data)
    for day in range(days):
        fish = [f-1 if f > 0 else 6 for f in fish] + [8 for f in fish if f == 0]
    return len(fish)


def part_two(data: List[int], days: int) -> int:
    fish = process_data(data)
    fc = tuple([fish.count(f) for f in range(9)])
    for day in range(1, days + 1):
        fc = (fc[1], fc[2], fc[3], fc[4], fc[5], fc[6], fc[7] + fc[0], fc[8], fc[0])
    return sum(fc)


def main():
    example = ['3,4,3,1,2']
    input_data = get_input()

    assert part_one(example, 18) == 26
    assert part_one(example, 80) == 5934
    print(f'Part 1 Answer:\n{part_one(input_data, 80)}')

    assert part_two(example, 18) == 26
    assert part_two(example, 80) == 5934
    assert part_two(example, 256) == 26984457539
    print(f'Part 2 Answer:\n{part_two(input_data, 256)}')


if __name__ == '__main__':
    main()
