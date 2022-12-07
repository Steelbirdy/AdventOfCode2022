from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


def execute(root: dict, tree: dict, cmds: list[str]):
    while cmds:
        cmd = cmds.pop()[2:]
        if cmd.startswith('cd'):
            _, dir = cmd.split(' ')
            if dir == '/':
                tree = root
            else:
                tree = tree[dir]
        elif cmd.startswith('ls'):
            while cmds and not cmds[-1].startswith('$ '):
                cmd = cmds.pop()
                if cmd.startswith('dir '):
                    tree[cmd[4:]] = {'..': tree}
                else:
                    size, name = cmd.split(' ')
                    tree[name] = int(size)
        else:
            print(f'Unexpected command {cmd}')


small_dirs = 0
all_dirs = dict()


def total_size(name, tree):
    global small_dirs, all_dirs
    if isinstance(tree, int):
        return tree
    ret = sum(total_size(k, x) for k, x in tree.items() if k != '..')
    all_dirs[name] = ret
    if ret <= 100000:
        small_dirs += ret
    return ret


@aoc(fmt, **kwargs)
def part1(inp: list[str]) -> int:
    tree = dict()
    root = tree

    execute(root, tree, list(reversed(inp)))
    total_size('/', root)
    return small_dirs


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    tree = dict()
    root = tree

    execute(root, tree, list(reversed(inp)))
    unused = 70000000 - total_size('/', root)
    needed = 30000000 - unused
    return min(v for v in all_dirs.values() if v >= needed)
