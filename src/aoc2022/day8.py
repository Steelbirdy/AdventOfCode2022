from ..utils import aoc

fmt = '{}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


def make_range(range_, i=None, j=None):
    range_ = list(range_)
    if i is None:
        return zip(range_, (j for _ in range_))
    else:
        return zip((i for _ in range_), range_)


def scenic_score(inp, i, j):
    tree = inp[i][j]
    r, c = len(inp), len(inp[0])

    def doit(range_, i=None, j=None):
        v = 0
        for i, j in make_range(range_, i, j):
            v += 1
            if inp[i][j] >= tree:
                break
        return v

    return doit(reversed(range(i)), None, j) \
        * doit(reversed(range(j)), i, None)  \
        * doit(range(i + 1, r), None, j)     \
        * doit(range(j + 1, c), i, None)


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    r, c = len(inp), len(inp[0])

    on_edge = lambda x, lim: x in (0, lim - 1)
    visible = [[on_edge(i, r) or on_edge(j, c) for j in range(c)] for i in range(r)]

    def doit(range_, i=None, j=None):
        range_ = make_range(range_, i, j)
        i0, j0 = next(range_)
        prev_max = inp[i0][j0]
        for i, j in range_:
            if prev_max == 9:
                break
            if inp[i][j] > prev_max:
                visible[i][j] = True
                prev_max = inp[i][j]

    for i in range(r):
        doit(range(c), i, None)
        doit(reversed(range(c)), i, None)
    for j in range(c):
        doit(range(r), None, j)
        doit(reversed(range(r)), None, j)
    return sum(map(sum, visible))


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    r, c = len(inp), len(inp[0])
    return max(scenic_score(inp, i, j) for i in range(r) for j in range(c))
