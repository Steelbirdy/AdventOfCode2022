from ..utils import aoc


fmt = '{} {:d},{:d} through {:d},{:d}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    lights = [([False] * 1000) for _ in range(1000)]
    for cmd, x0, y0, x1, y1 in inp:
        if cmd == 'toggle':
            doit = lambda x: not x
        elif cmd == 'turn on':
            doit = lambda x: True
        else:
            doit = lambda x: False
        for row in range(x0, x1 + 1):
            lights[row][y0:y1 + 1] = map(doit, lights[row][y0:y1 + 1])
    return sum(sum(x) for x in lights)


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    lights = [([0] * 1000) for _ in range(1000)]
    for cmd, x0, y0, x1, y1 in inp:
        if cmd == 'toggle':
            doit = lambda x: x + 2
        elif cmd == 'turn on':
            doit = lambda x: x + 1
        else:
            doit = lambda x: max(x - 1, 0)
        for row in range(x0, x1 + 1):
            lights[row][y0:y1 + 1] = map(doit, lights[row][y0:y1 + 1])
    return sum(sum(x) for x in lights)
