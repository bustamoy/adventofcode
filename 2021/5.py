# Advent Of Code
# https://adventofcode.com/2021/day/5
# https://adventofcode.com/2021/day/5#part2
# COMPLETE

from os.path import exists
from typing import Dict, List, Tuple

YEAR: int = 2021
DAY: int = 5


def get_input() -> List[str]:
    filename = f'input-{YEAR}-{DAY}'
    if exists(filename):
        with open(filename, 'r') as input_file:
            return input_file.read().splitlines()
    else:
        raise FileNotFoundError(f"Did not find input file: '{filename}'.")


def process_data(data: List[str]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    return [(tuple(tuple([int(n) for n in p.split(',')]) for p in line.split() if ',' in p)) for line in data]


def find_overlaps(data: List[Tuple[Tuple[int, int], Tuple[int, int]]], diagonal: bool = False) -> int:
    vents: Dict[Tuple[int, int], int] = dict()
    pairs = []
    for line in process_data(data):
        if line[0][0] == line[1][0]:
            start = min(line[0][1], line[1][1])
            end = max(line[0][1], line[1][1])
            others = [line[0][0]] * (end - start + 1)
            pairs = list(zip(others, range(start, end + 1)))
        elif line[0][1] == line[1][1]:
            start = min(line[0][0], line[1][0])
            end = max(line[0][0], line[1][0])
            others = [line[0][1]] * (end - start + 1)
            pairs = list(zip(range(start, end + 1), others))
        elif diagonal and abs(line[1][0] - line[0][0]) == abs(line[1][1] - line[0][1]):
            line = sorted(list(line), key=lambda pair: pair[0])
            xs = range(line[0][0], line[1][0] + 1)
            ys = range(line[0][1], line[1][1] + 1) if line[0][1] < line[1][1] else range(line[0][1], line[1][1] - 1, -1)
            pairs = list(zip(xs, ys))
        for p in pairs:
            vents[p] = vents.get(p, 0) + 1
        pairs.clear()
    return len([v for v in vents.values() if v >= 2])


def part_one(data: List[str]) -> int:
    vents = process_data(data)
    return find_overlaps(vents)


def part_two(data: List[str]) -> int:
    vents = process_data(data)
    return find_overlaps(vents, diagonal=True)


def main():
    example = ['0,9 -> 5,9',
               '8,0 -> 0,8',
               '9,4 -> 3,4',
               '2,2 -> 2,1',
               '7,0 -> 7,4',
               '6,4 -> 2,0',
               '0,9 -> 2,9',
               '3,4 -> 1,4',
               '0,0 -> 8,8',
               '5,5 -> 8,2']
    input_data = get_input()

    assert part_one(example) == 5
    print(f'Part 1 Answer:\n{part_one(input_data)}')

    assert part_two(example) == 12
    print(f'Part 2 Answer:\n{part_two(input_data)}')


if __name__ == '__main__':
    main()
