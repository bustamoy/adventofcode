# Advent Of Code
# https://adventofcode.com/2021/day/2
# https://adventofcode.com/2021/day/2#part2
# COMPLETE

from functools import reduce
from os.path import exists
from typing import List

YEAR: int = 2021
DAY: int = 2


def get_input() -> List[int]:
    result = None
    filename = f'input-{YEAR}-{DAY}'
    if exists(filename):
        with open(filename, 'r') as input_file:
            result = [line for line in input_file.read().splitlines()]
    else:
        raise FileNotFoundError(f"Did not find input file: '{filename}'.")
    return result


def part_one(data):
    data = [cmd.split(' ') for cmd in data]
    x = sum([int(cmd[1]) for cmd in data if cmd[0] == 'forward'])
    y = sum([int(cmd[1]) if cmd[0] == 'down' else -int(cmd[1]) for cmd in data if cmd[0] != 'forward'])
    return x * y


def part_two(data):
    data = [cmd.split(' ') for cmd in data]
    x = sum([int(cmd[1]) for cmd in data if cmd[0] == 'forward'])

    def red(a, b):
        if b[0] == 'forward':
            return a[0], a[1] + a[0] * int(b[1])
        else:
            return a[0] + (-int(b[1]) if b[0] == 'up' else int(b[1])), a[1]

    y = reduce(red, data, (0, 0))[1]
    return x * y


def main():
    example = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    input_data = get_input()

    assert part_one(example) == 150
    print(f'Part 1 Answer:\n{part_one(input_data)}')

    assert part_two(example) == 900
    print(f'Part 2 Answer:\n{part_two(input_data)}')


if __name__ == '__main__':
    main()
