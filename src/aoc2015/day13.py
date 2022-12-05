from ..utils import aoc
from itertools import permutations


fmt = '{} would {} {:d} happiness units by sitting next to {}.'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    nodes = set()
    edges = dict()
    for p1, dh, h, p2 in inp:
        h = -h if dh == 'lose' else h
        nodes |= {p1, p2}
        edges.setdefault(p1, dict())[p2] = h
    return max(
        sum(map(lambda x, y: edges[x][y] + edges[y][x], p, list(p[1:]) + [p[0]]))
        for p in permutations(nodes)
    )


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    nodes = {'me'}
    edges = {'me': dict()}
    for p1, dh, h, p2 in inp:
        h = -h if dh == 'lose' else h
        nodes |= {p1, p2}
        edges.setdefault(p1, dict())[p2] = h
        edges['me'][p1] = 0
        edges[p1]['me'] = 0
        edges['me'][p2] = 0
        edges.setdefault(p2, dict())['me'] = 0
    return max(
        sum(map(lambda x, y: edges[x][y] + edges[y][x], p, list(p[1:]) + [p[0]]))
        for p in permutations(nodes)
    )
