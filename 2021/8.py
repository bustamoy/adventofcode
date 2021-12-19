# Advent Of Code
# https://adventofcode.com/2021/day/8
# https://adventofcode.com/2021/day/8#part2
# COMPLETE

from typing import List, Tuple

YEAR: int = 2021
DAY: int = 8


def get_input() -> List[str]:
    filename = f'input-{YEAR}-{DAY}'
    from os.path import exists
    if exists(filename):
        with open(filename, 'r') as input_file:
            return input_file.read().splitlines()
    else:
        raise FileNotFoundError(f"Did not find input file: '{filename}'.")


def process_data(data: List[str]) -> List[Tuple[List[str], List[str]]]:
    return [tuple([group.split(' ') for group in line.split(' | ')]) for line in data]


def part_one(data: List[str]) -> int:
    samples = process_data(data)
    outputs = []
    for s in samples:
        outputs.extend(s[1])
    targets = [o for o in outputs if len(o) in [2, 4, 3, 7]]
    return len(targets)


LOOKUPS = {344: 'A', 204: 'B', 304: 'C', 266: 'D', 96: 'E', 396: 'F', 280: 'G'}


def decode_num(nums: List[str], outputs: List[str]) -> int:
    all_nums = ''.join(nums)
    mapping = {}
    for char in 'abcdefg':
        cnt = all_nums.count(char)
        foo = sum([len(n) if char in n else 0 for n in nums])
        mapping[char] = LOOKUPS[cnt * foo]
    outputs = [''.join([mapping[ch] for ch in o]) for o in outputs]
    result = 0
    for digit in outputs:
        result *= 10
        if len(digit) == 2:
            result += 1
        elif len(digit) == 4:
            result += 4
        elif len(digit) == 3:
            result += 7
        elif len(digit) == 7:
            result += 8
        elif len(digit) == 6 and 'D' not in digit:
            result += 0
        elif len(digit) == 6 and 'C' not in digit:
            result += 6
        elif len(digit) == 6 and 'E' not in digit:
            result += 9
        elif len(digit) == 5 and 'B' in digit:
            result += 5
        elif len(digit) == 5 and 'E' in digit:
            result += 2
        else:
            result += 3
    return result


def part_two(data: List[str]) -> int:
    samples = process_data(data)
    return sum([decode_num(sample, digits) for sample, digits in samples])


def main():
    example = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
               'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
               'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
               'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
               'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
               'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
               'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
               'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
               'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
               'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']
    input_data = get_input()

    assert part_one(example)
    print(f'Part 1 Answer:\n{part_one(input_data)}')

    assert part_two(example)
    print(f'Part 2 Answer:\n{part_two(input_data)}')


if __name__ == '__main__':
    main()
