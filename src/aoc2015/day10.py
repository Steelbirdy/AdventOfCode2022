from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': None,
    'meta_sep': None,
    'case_sensitive': False,
}


def advance(s: str) -> str:
    last = 't'
    count = 0
    ret = ''
    for c in s:
        if c == last:
            count += 1
            continue
        if count != 0:
            ret += f"{count}{last}"
        count = 1
        last = c
    if count != 0:
        ret += f"{count}{last}"
    return ret


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    for i in range(40):
        inp = advance(inp)
    return len(inp)


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    for i in range(50):
        inp = advance(inp)
    return len(inp)
