# Advent Of Code
# https://adventofcode.com/2021/day/1
# https://adventofcode.com/2021/day/1#part2
# COMPLETE

from os.path import exists
from typing import List

YEAR: int = 2021
DAY: int = 1


def get_input() -> List[int]:
    result = None
    filename = f'input-{YEAR}-{DAY}'
    if exists(filename):
        with open(filename, 'r') as input_file:
            result = [int(depth) for depth in input_file.read().splitlines()]
    else:
        raise FileNotFoundError(f"Did not find input file: '{filename}'.")
    return result


def part_one(data):
    total = 0
    for i, depth in enumerate(data):
        if depth > data[i-1]:
            total += 1
    return total


def part_two(data):
    triples = [sum(t) for t in zip(data[:-2], data[1:-1], data[2:])]
    return sum([1 if c[1] > c[0] else 0 for c in zip(triples[:-1], triples[1:])])


def main():
    input_data = get_input()

    assert part_one([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7
    print(f'Part 1 Answer:\n{part_one(input_data)}')

    assert part_two([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 5
    print(f'Part 2 Answer:\n{part_two(input_data)}')


if __name__ == '__main__':
    main()
