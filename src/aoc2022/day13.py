from ..utils import aoc
from .. import utils


fmt = '{}'
kwargs = {
    'sep': '\n',
    'meta_sep': '\n\n',
    'case_sensitive': False,
}


def cmp(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x - y
    if isinstance(x, list) and isinstance(y, list):
        x = x.copy()
        y = y.copy()
        x.reverse()
        y.reverse()
        while x and y:
            a = x.pop()
            b = y.pop()
            tmp = cmp(a, b)
            if tmp != 0:
                return tmp
        if (not x) and y:
            return -1
        if (not y) and x:
            return 1
        return 0
    if isinstance(x, int):
        return cmp([x], y)
    return cmp(x, [y])


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    inp = [(eval(x), eval(y)) for [x, y] in inp]
    return sum((i if cmp(x, y) < 0 else 0) for i, (x, y) in enumerate(inp, start=1))


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    inp = [eval(x) for t in inp for x in t] + [[[2]], [[6]]]
    utils.sort_by(inp, cmp)
    return (inp.index([[2]]) + 1) * (inp.index([[6]]) + 1)
