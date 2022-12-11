from ..utils import aoc


class Monkey:
    def __init__(self, start, op, test):
        self.items = start
        self.op = op
        self.test = test
        self.inspections = 0

    def __str__(self):
        return f"Monkey({self.items}, {self.op}, {self.test}, {self.inspections})"

    def __repr__(self):
        return self.__str__()


fmt = '{}'
kwargs = {
    'sep': None,
    'meta_sep': None,
    'case_sensitive': False,
}


def parse(m):
    m = m.split('\n')[1:]
    start = [int(x) for x in m[0][len("  Starting items: "):].split(', ')]
    op = m[1][len('  Operation: new = '):]
    cond = int(m[2][len('  Test: divisible by '):])
    if_t = int(m[3][len('    If true: throw to monkey '):])
    if_f = int(m[4][len('    If true: throw to monkey '):])
    return Monkey(start, op, (cond, if_t, if_f))


def product(l):
    ret = 1
    for x in l:
        ret *= x
    return ret


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    monkies = inp.split('\n\n')
    monkies = [parse(m) for m in monkies]

    for _ in range(20):
        for m in monkies:
            for worry in m.items:
                m.inspections += 1
                old = worry
                worry = eval(m.op)
                worry //= 3
                if worry % m.test[0] == 0:
                    monkies[m.test[1]].items.append(worry)
                else:
                    monkies[m.test[2]].items.append(worry)
            m.items = []
    insp = [m.inspections for m in monkies]
    insp.sort()
    return insp[-1] * insp[-2]


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    monkies = inp.split('\n\n')
    monkies = [parse(m) for m in monkies]

    divisor = product([m.test[0] for m in monkies])

    for i in range(10000):
        for m in monkies:
            for worry in m.items:
                m.inspections += 1
                old = worry
                worry = eval(m.op)

                # Note that all the test divisors are prime numbers
                # This means that we can safely take `worry % product(divisors)`
                # without changing the result (sort of Chinese Remainder Theorem-ish)
                worry %= divisor
                if worry % m.test[0] == 0:
                    monkies[m.test[1]].items.append(worry)
                else:
                    monkies[m.test[2]].items.append(worry)
            m.items = []
    insp = [m.inspections for m in monkies]
    insp.sort()
    return insp[-1] * insp[-2]
