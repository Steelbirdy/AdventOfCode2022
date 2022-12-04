from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


@aoc(fmt, **kwargs)
def part1(inp: list[str]) -> int:
    sacks = [set(line[:len(line) // 2]) & set(line[len(line) // 2:]) for line in inp]
    return sum(priority(c.pop()) for c in sacks)


@aoc(fmt, **kwargs)
def part2(inp: list[str]) -> int:
    badges = []
    for i, line in enumerate(inp):
        if i % 3 == 0:
            badges.append(set(line))
        else:
            badges[-1] &= set(line)
    return sum(priority(b.pop()) for b in badges)
