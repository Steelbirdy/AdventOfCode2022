from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    in_code = sum(len(s) for s in inp)
    in_mem = sum(len(eval(s)) for s in inp)
    return in_code - in_mem


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    in_code = sum(len(s) for s in inp)
    T = str.maketrans({
        '"': '\\"',
        '\\': '\\\\',
    })
    return 2 * len(inp) + sum(len(s.translate(T)) for s in inp) - in_code
