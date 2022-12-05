from ..utils import aoc
from itertools import permutations


fmt = '{} to {} = {:d}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    nodes = set()
    edges = dict()
    for src, dest, d in inp:
        nodes |= {src, dest}
        edges.setdefault(src, dict())[dest] = d
        edges.setdefault(dest, dict())[src] = d
    return min(
        sum(map(lambda x, y: edges[x][y], p[:-1], p[1:]))
        for p in permutations(nodes)
    )


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    nodes = set()
    edges = dict()
    for src, dest, d in inp:
        nodes |= {src, dest}
        edges.setdefault(src, dict())[dest] = d
        edges.setdefault(dest, dict())[src] = d
    return max(
        sum(map(lambda x, y: edges[x][y], p[:-1], p[1:]))
        for p in permutations(nodes)
    )
