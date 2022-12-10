from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    cycle = 0
    X = 1
    ret = 0

    incr = None
    i = 0
    while i < len(inp):
        instr = inp[i]
        cycle += 1
        if cycle % 40 == 20:
            ret += cycle * X
        if incr is not None:
            X += incr
            incr = None
            i += 1
        elif instr == 'noop':
            i += 1
        elif instr.startswith('addx'):
            _, num = instr.split(' ')
            incr = int(num)
    return ret


@aoc(fmt, **kwargs)
def part2(inp):
    CRT = [[False for _ in range(40)] for _ in range(6)]
    pxl = [0, 0]
    cycle = 0
    X = 1

    incr = None
    i = 0
    while i < len(inp):
        instr = inp[i]
        cycle += 1
        CRT[pxl[1]][pxl[0]] = abs(X % 40 - (cycle - 1) % 40) <= 1
        pxl[0] += 1
        if pxl[0] == 40:
            pxl = [0, pxl[1] + 1]
        if incr is not None:
            X += incr
            incr = None
            i += 1
        elif instr == 'noop':
            i += 1
        elif instr.startswith('addx'):
            _, num = instr.split(' ')
            incr = int(num)

    for row in CRT:
        print(''.join('#' if x else '.' for x in row))
