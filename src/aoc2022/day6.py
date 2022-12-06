from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': None,
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    for i in range(len(inp) - 4):
        x = set(inp[i:i+4])
        if len(x) == 4:
            return i + 4


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    for i in range(len(inp) - 14):
        x = set(inp[i:i + 14])
        if len(x) == 14:
            return i + 14
