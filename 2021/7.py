# Advent Of Code
# https://adventofcode.com/2021/day/7
# https://adventofcode.com/2021/day/7#part2
# COMPLETE


from typing import List

YEAR: int = 2021
DAY: int = 7


def get_input() -> List[str]:
    filename = f'input-{YEAR}-{DAY}'
    from os.path import exists
    if exists(filename):
        with open(filename, 'r') as input_file:
            return input_file.read().splitlines()
    else:
        raise FileNotFoundError(f"Did not find input file: '{filename}'.")


def process_data(data: List[str]) -> List[int]:
    return [int(c) for c in data[0].split(',')]


def part_one(data: List[int]) -> int:
    crabs = process_data(data)
    costs = [sum([abs(c - pos) for c in crabs]) for pos in range(max(crabs) + 1)]
    return min(costs)


def part_two(data: List[int]) -> int:
    crabs = process_data(data)
    costs = [sum([(abs(c - pos)) * (abs(c - pos)+1)/2 for c in crabs]) for pos in range(max(crabs) + 1)]
    return int(min(costs))


def main():
    example = ['16,1,2,0,4,2,7,1,2,14']
    input_data = get_input()

    assert part_one(example) == 37
    print(f'Part 1 Answer:\n{part_one(input_data)}')

    assert part_two(example)
    print(f'Part 2 Answer:\n{part_two(input_data)}')


if __name__ == '__main__':
    main()
