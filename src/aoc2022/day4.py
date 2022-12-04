from ..utils import aoc


fmt = '{:d}-{:d},{:d}-{:d}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    check = lambda x, y: int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[1])
    return sum(int(check(x[:2], x[2:]) or check(x[2:], x[:2])) for x in inp)


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    check = lambda x, y: int(x[0]) <= int(y[0]) <= int(x[1])
    return sum(int(check(x[:2], x[2:]) or check(x[2:], x[:2])) for x in inp)
