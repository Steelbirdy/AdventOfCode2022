from ..utils import aoc
import parse


fmt = '{}'
kwargs = {
    'sep': None,
    'meta_sep': None,
    'case_sensitive': False,
}


def parse_input(inp) -> (list[list[str]], list[str]):
    crane, instr = inp.split('\n\n')
    instrs = [parse.parse('move {:d} from {:d} to {:d}', x) for x in instr.split('\n')]
    stacks = []
    for line in crane.split('\n')[:-1]:
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                while len(stacks) <= i // 4:
                    stacks.append([])
                stacks[i // 4].insert(0, line[i])
    return stacks, instrs


@aoc(fmt, **kwargs)
def part1(inp) -> str:
    stacks, instrs = parse_input(inp)
    for st, src, dest in instrs:
        for _ in range(st):
            if stacks[src - 1]:
                stacks[dest - 1].append(stacks[src - 1].pop())
    return ''.join(st.pop() for st in stacks if st)


@aoc(fmt, **kwargs)
def part2(inp) -> str:
    stacks, instrs = parse_input(inp)
    for st, src, dest in instrs:
        stacks[dest - 1].extend(stacks[src - 1][-st:])
        stacks[src - 1] = stacks[src - 1][:-st]
    return ''.join(st.pop() for st in stacks if st)
