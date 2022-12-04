from ..utils import aoc


fmt = '{:w} {:w}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


def parse(a, x):
    diff = lambda c, c0: ord(c) - ord(c0) + 1
    return diff(a, 'A'), diff(x, 'X')


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    def calc(line):
        da, dx = parse(*line)
        return dx + res[(dx - da) % 3]
    res = [3, 6, 0]
    return sum(map(calc, inp))


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    def calc(line):
        da, dx = parse(*line)
        tmp = (da + res[dx - 1]) % 3
        return 3 * (dx - 1) + (tmp or 3)
    res = [2, 0, 1]
    return sum(map(calc, inp))
