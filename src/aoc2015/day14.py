from ..utils import aoc


fmt = '{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


T = 2503


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    M = 0
    for _, v, tf, tr in inp:
        t = tf + tr
        dt, r = divmod(T, t)
        f = dt * v * tf
        if r <= tf:
            f += r * v
        else:
            f += v * tf
        M = max(M, f)
    return M


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    p = [0 for _ in inp]
    for sec in range(1, T + 1):
        M = 0
        ties = []
        for i, (_, v, tf, tr) in enumerate(inp):
            t = tf + tr
            dt, r = divmod(sec, t)
            f = dt * v * tf
            if r <= tf:
                f += r * v
            else:
                f += v * tf
            if f > M:
                M = f
                ties = []
            if f >= M:
                ties.append(i)
        for i in ties:
            p[i] += 1
    return max(p)
