from ..utils import aoc


fmt = '{:d}'
kwargs = {
    'sep': '\n',
    'meta_sep': '\n\n',
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    return max(sum(x) for x in inp)


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    elves = list(sum(x) for x in inp)
    return sum(sorted(elves)[-3:])
