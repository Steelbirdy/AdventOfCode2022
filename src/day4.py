import utils


def part1(inp: list[str]) -> int:
    lines = [[y.split('-') for y in x.split(',')] for x in inp]
    check = lambda x, y: int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[1])
    return sum(int(check(x, y) or check(y, x)) for x, y in lines)


def part2(inp: list[str]) -> int:
    lines = [[y.split('-') for y in x.split(',')] for x in inp]
    check = lambda x, y: int(x[0]) <= int(y[0]) <= int(x[1])
    return sum(int(check(x, y) or check(y, x)) for x, y in lines)


if __name__ == '__main__':
    utils.aoc(part1, part2)
