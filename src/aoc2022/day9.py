from ..utils import aoc
import math


fmt = '{} {:d}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


moves_map = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}


def needs_to_move(tail, head):
    # Can't do (head[0] - tail[0]) // 2 because -1 // 2 == -1??
    # What a dumb operator
    dx = int((head[0] - tail[0]) / 2)
    dy = int((head[1] - tail[1]) / 2)
    if dx != 0 and head[1] != tail[1]:
        dy = math.copysign(1, head[1] - tail[1])
    elif dy != 0 and head[0] != tail[0]:
        dx = math.copysign(1, head[0] - tail[0])
    return [int(dx), int(dy)]


def simulate(moves, knots):
    visited = {(0, 0)}
    tail = knots[-1]
    for direction, count in moves:
        dx, dy = moves_map[direction]
        for _ in range(count):
            prev = knots[0]
            knots[0][0] += dx
            knots[0][1] += dy
            for i in range(1, len(knots)):
                tx, ty = needs_to_move(knots[i], prev)
                knots[i][0] += tx
                knots[i][1] += ty
                prev = knots[i]
            visited.add(tuple(tail))
    return len(visited)


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    return simulate(inp, [[0, 0], [0, 0]])


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    return simulate(inp, [[0, 0] for _ in range(10)])
