import utils


def parse(a, x):
    diff = lambda c, c0: ord(c) - ord(c0) + 1
    return diff(a, 'A'), diff(x, 'X')


def part1(inp: list[str]) -> int:
    def calc(line):
        da, dx = parse(*line.split(' '))
        return dx + res[(dx - da) % 3]
    res = [3, 6, 0]
    return sum(map(calc, inp))


def part2(inp: list[str]) -> int:
    def calc(line):
        da, dx = parse(*line.split(' '))
        tmp = (da + res[dx - 1]) % 3
        return 3 * (dx - 1) + (tmp or 3)
    res = [2, 0, 1]
    return sum(map(calc, inp))


if __name__ == '__main__':
    utils.aoc(part1, part2)
