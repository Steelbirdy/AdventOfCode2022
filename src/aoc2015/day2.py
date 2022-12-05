from ..utils import aoc


fmt = '{:d}x{:d}x{:d}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    return sum(2*l*w + 2*l*h + 2*w*h + min(l*w, l*h, w*h) for l, w, h in inp)


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    return sum(
        l*w*h + 2*min(l+w, l+h, w+h) for l, w, h in inp
    )
