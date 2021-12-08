# Advent Of Code
# https://adventofcode.com/2021/day/3
# https://adventofcode.com/2021/day/3#part2
# COMPLETE

from os.path import exists
from typing import List

YEAR: int = 2021
DAY: int = 3


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
    bitsum = [sum([int(d[i]) for d in data]) for i in range(len(data[0]))]
    gamma = int(''.join(['1' if t > (len(data) // 2) else '0' for t in bitsum]), 2)
    epsilon = 2**len(data[0]) - 1 - gamma
    return gamma * epsilon


def part_two(data):
    data2 = data.copy()
    for i in range(len(data[0])):
        if len(data) == 1:
            break
        bit = '0' if sum([int(d[i]) for d in data]) < (len(data) / 2) else '1'
        data = [d for d in data if d[i] == bit]
    gen = int(data[0], 2)
    data = data2
    for i in range(len(data[0])):
        if len(data) == 1:
            break
        bit = '0' if sum([int(d[i]) for d in data]) >= (len(data) / 2) else '1'
        data = [d for d in data if d[i] == bit]
    scrub = int(data[0], 2)
    return gen * scrub


def main():
    example = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010',
               '01010']
    input_data = get_input()

    assert part_one(example) == 198
    print(f'Part 1 Answer:\n{part_one(input_data)}')

    assert part_two(example) == 230
    print(f'Part 2 Answer:\n{part_two(input_data)}')


if __name__ == '__main__':
    main()
