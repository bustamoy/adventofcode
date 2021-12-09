# Advent Of Code
# https://adventofcode.com/2021/day/4
# https://adventofcode.com/2021/day/4#part2
# COMPLETE

from os.path import exists
from typing import List, Tuple

YEAR: int = 2021
DAY: int = 4

INVALID = 100


def get_input() -> List[str]:
    filename = f'input-{YEAR}-{DAY}'
    if exists(filename):
        with open(filename, 'r') as input_file:
            return [line for line in input_file.read().splitlines()]
    else:
        raise FileNotFoundError(f"Did not find input file: '{filename}'.")


def process_data(data) -> Tuple[List[int], List[List[List[int]]]]:
    blocks = []
    block = []
    for i, line in enumerate(data):
        if line == '':
            blocks.append(block)
            block = []
        else:
            block.append([int(n) for n in line.split(',' if ',' in line else None)])
    nums = blocks.pop(0)[0]
    return nums, blocks


def check_line(called: List[int], numbers: List[int]) -> int:
    match = 0
    for pos, num in enumerate(called):
        if num in numbers:
            match += 1
        if match == len(numbers):
            return pos
    return -1


def check_board(called: List[int], board: List[List[int]]) -> int:
    win_num_pos = INVALID
    # diagonals: [[board[i][i] for i in range(size)], [board[i][size-1-i] for i in range(size)]]
    for line in board + [list(zip(*board))[i] for i in range(len(board[0]))]:
        bingo_num = check_line(called, line)
        if bingo_num >= 0:
            win_num_pos = min(bingo_num, win_num_pos)
    return win_num_pos


def check_boards(called: List[int], boards: List[List[List[int]]]) -> List[Tuple[int, int, int]]:
    winners = []
    for pos, board in enumerate(boards):
        win_num_pos = check_board(called, board)
        if win_num_pos != INVALID:
            score = sum([c for r in board for c in r if c not in called[:win_num_pos + 1]]) * called[win_num_pos]
            winners.append((pos, win_num_pos, score))
    return winners


def find_winners(data) -> List[Tuple[int, int, int]]:
    nums, boards = process_data(data)
    winners = check_boards(nums, boards)
    winners.sort(key=lambda b: b[1])
    return winners


def part_one(data) -> int:
    return find_winners(data)[0][2]


def part_two(data):
    return find_winners(data)[-1][2]


def main():
    example = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
               '',
               '22 13 17 11  0',
               ' 8  2 23  4 24',
               '21  9 14 16  7',
               ' 6 10  3 18  5',
               ' 1 12 20 15 19',
               '',
               ' 3 15  0  2 22',
               ' 9 18 13 17  5',
               '19  8  7 25 23',
               '20 11 10 24  4',
               '14 21 16 12  6',
               '',
               '14 21 17 24  4',
               '10 16 15  9 19',
               '18  8 23 26 20',
               '22 11 13  6  5',
               ' 2  0 12  3  7',
               '']
    input_data = get_input()

    assert part_one(example) == 4512
    print(f'Part 1 Answer:\n{part_one(input_data)}')

    assert part_two(example)
    print(f'Part 2 Answer:\n{part_two(input_data)}')


if __name__ == '__main__':
    main()
