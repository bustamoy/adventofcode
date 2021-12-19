# Advent Of Code
# https://adventofcode.com/2021/day/9
# https://adventofcode.com/2021/day/9#part2
# COMPLETE

from typing import List, Set, Tuple

YEAR: int = 2021
DAY: int = 9


def get_input() -> List[str]:
    filename = f'input-{YEAR}-{DAY}'
    from os.path import exists
    if exists(filename):
        with open(filename, 'r') as input_file:
            return input_file.read().splitlines()
    else:
        raise FileNotFoundError(f"Did not find input file: '{filename}'.")


def process_data(data: List[str]) -> List[List[int]]:
    return [[int(x) for x in list(line)] for line in data]


def check_loc(locs: List[List[int]], x: int, y: int) -> bool:
    is_low = True
    h = len(locs)
    w = len(locs[0])
    loc = locs[y][x]
    is_low &= y == 0 or locs[y - 1][x] > loc        # UP
    is_low &= x == w-1 or loc < locs[y][x + 1]      # RIGHT
    is_low &= y == h - 1 or loc < locs[y + 1][x]    # DOWN
    is_low &= x == 0 or locs[y][x-1] > loc          # LEFT
    return is_low


def part_one(data: List[str]) -> int:
    locs = process_data(data)
    return sum([locs[y][x] + 1 if check_loc(locs, x, y) else 0 for x in range(len(locs[0])) for y in range(len(locs))])


def find_basin(x: int, y: int, z: int, locs: List[List[int]], d: str, seen: Set[Tuple[int, int, int]]) -> int:
    x2, y2 = x, y
    nexts = ['UP', 'RIGHT', 'DOWN', 'LEFT']
    if d == 'UP' and 0 < y <= len(locs)-1:
        y2 = y-1
        nexts.remove('DOWN')
    elif d == 'RIGHT' and 0 <= x < len(locs[0]) - 1:
        x2 = x + 1
        nexts.remove('LEFT')
    elif d == 'DOWN' and 0 <= y < len(locs) - 1:
        y2 = y+1
        nexts.remove('UP')
    elif d == 'LEFT' and 0 < x <= len(locs[0]) - 1:
        x2 = x-1
        nexts.remove('RIGHT')
    else:
        return 0
    check = locs[y2][x2]
    if check == 9:
        return 0
    if check > z and (x2, y2, check) not in seen:
        result = 1
        seen.add((x2, y2, check))
        for next_d in nexts:
            result += find_basin(x2, y2, check, locs, next_d, seen)
        return result
    else:
        return 0


def part_two(data: List[str]) -> int:
    locs = process_data(data)
    lows = [(x, y, locs[y][x]) for x in range(len(locs[0])) for y in range(len(locs)) if check_loc(locs, x, y)]
    seen = set(lows)
    results = []
    for x, y, z in lows:
        size = 1
        for d in ['UP', 'RIGHT', 'DOWN', 'LEFT']:
            size += find_basin(x, y, z, locs, d, seen)
        results.append(size)
    results.sort()
    return results.pop() * results.pop() * results.pop()


def main():
    example = ['2199943210',
               '3987894921',
               '9856789892',
               '8767896789',
               '9899965678']
    input_data = get_input()

    assert part_one(example) == 15
    print(f'Part 1 Answer:\n{part_one(input_data)}')

    assert part_two(example) == 1134
    print(f'Part 2 Answer:\n{part_two(input_data)}')


if __name__ == '__main__':
    main()
