from ..utils import aoc
import networkx as nx


fmt = '{}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


def neighbors(i, j, r, c):
    d = (-1, 1)
    for dx in d:
        x, y = i + dx, j
        if x in range(0, r) and y in range(0, c):
            yield (i + dx, j)
    for dy in d:
        x, y = i, j + dy
        if x in range(0, r) and y in range(0, c):
            yield (i, j + dy)


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    r, c = len(inp), len(inp[0])
    start = (0, 0)
    end = (0, 0)
    g = nx.DiGraph()
    for i in range(r):
        for j in range(c):
            if inp[i][j] == 'S':
                start = (i, j)
                inp[i] = inp[i][:j] + 'a' + inp[i][j+1:]
            if inp[i][j] == 'E':
                end = (i, j)
                inp[i] = inp[i][:j] + 'z' + inp[i][j+1:]
    for i in range(r):
        for j in range(c):
            g.add_node((i, j))
            for n_x, n_y in neighbors(i, j, r, c):
                if ord(inp[n_x][n_y:n_y+1]) <= ord(inp[i][j:j+1]) + 1:
                    g.add_node((i, j))
                    g.add_node((n_x, n_y))
                    g.add_edge((i, j), (n_x, n_y), weight=1)
    path = nx.algorithms.shortest_path(g, start, end)
    return len(path) - 1


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    r, c = len(inp), len(inp[0])
    g = nx.DiGraph()
    end = (-1, -1)
    for i in range(r):
        for j in range(c):
            if inp[i][j] == 'S':
                inp[i] = inp[i][:j] + 'a' + inp[i][j + 1:]
            if inp[i][j] == 'E':
                end = (i, j)
                inp[i] = inp[i][:j] + 'z' + inp[i][j + 1:]
            for n_x, n_y in neighbors(i, j, r, c):
                if ord(inp[n_x][n_y:n_y + 1]) <= ord(inp[i][j:j + 1]) + 1:
                    g.add_edge((i, j), (n_x, n_y), weight=1)

    def try_or_inf(start):
        try:
            return len(nx.algorithms.shortest_path(g, start, end)) - 1
        except:
            return 1e20
    return min(try_or_inf((i, j)) for i in range(r) for j in range(c) if inp[i][j] == 'a')
