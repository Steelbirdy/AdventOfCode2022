from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': None,
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    return inp.count('(') - inp.count(')')


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    flr = 0
    for i, c in enumerate(inp):
        flr += 1 if c == '(' else -1
        if flr < 0:
            return i + 1
