from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': None,
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    visited = set()
    x = 0
    y = 0
    d = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    for dir in inp:
        dx, dy = d[dir]
        x += dx
        y += dy
        visited.add((x, y))
    return len(visited)


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    visited = set()
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    d = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    for i, dir in enumerate(inp):
        dx, dy = d[dir]
        if i % 2 == 0:
            x1 += dx
            y1 += dy
            visited.add((x1, y1))
        else:
            x2 += dx
            y2 += dy
            visited.add((x2, y2))
    return len(visited)
