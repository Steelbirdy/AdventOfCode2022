import utils


def part1(inp: str) -> int:
    elves = inp.split('\n\n')
    return max(sum(int(line) for line in elf.split('\n')) for elf in elves)


def part2(inp: str) -> int:
    elves = inp.split('\n\n')
    elves = [sum(int(line) for line in elf.split('\n')) for elf in elves]
    return sum(sorted(elves)[-3:])


if __name__ == '__main__':
    utils.aoc(part1, part2)
