from ..utils import aoc
import networkx as nx


fmt = '{} -> {}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


def try_int(x: str):
    try:
        return int(x)
    except Exception:
        return None


def not_try_int(x: str):
    try:
        int(x)
        return False
    except Exception:
        return True


def resolve(vars, arg):
    if (iarg := try_int(arg)) is not None:
        return iarg
    else:
        return vars[arg]


ops = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y,
}


def get_inputs(cmd) -> list:
    parts = cmd.split(' ')
    ret = []
    if len(parts) == 1:
        if not_try_int(parts[0]):
            ret.append(parts[0])
    elif len(parts) == 2:
        if not_try_int(parts[1]):
            ret.append(parts[1])
    else:
        if not_try_int(parts[0]):
            ret.append(parts[0])
        if not_try_int(parts[2]):
            ret.append(parts[2])
    return ret


def apply(cmd, outp, vars):
    parts = cmd.split(' ')
    if len(parts) == 1:
        arg = resolve(vars, parts[0])
        vars[outp] = arg
    elif len(parts) == 2:
        arg = resolve(vars, parts[1])
        vars[outp] = ~arg
    else:
        op = ops[parts[1]]
        larg = resolve(vars, parts[0])
        rarg = resolve(vars, parts[2])
        vars[outp] = op(larg, rarg)


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    g = nx.DiGraph()
    lhs = dict()
    rhs = dict()
    for i, (cmd, outp) in enumerate(inp):
        for v in get_inputs(cmd):
            lhs.setdefault(v, list()).append(i)
        rhs.setdefault(outp, list()).append(i)
        g.add_node(i)

    for i, (cmd, outp) in enumerate(inp):
        tmp = lhs.get(outp)
        if tmp is None:
            continue
        for j in tmp:
            g.add_edge(i, j)

    ordered = list(nx.topological_sort(g))
    vars = dict()
    for i in ordered:
        cmd, outp = inp[i]
        apply(cmd, outp, vars)
    return vars['a']


@aoc(fmt, **kwargs)
def part2(inp, raw) -> int:
    g = nx.DiGraph()
    lhs = dict()
    rhs = dict()
    for i, (cmd, outp) in enumerate(inp):
        if outp == 'b':
            continue
        for v in get_inputs(cmd):
            lhs.setdefault(v, list()).append(i)
        rhs.setdefault(outp, list()).append(i)
        g.add_node(i)

    for i, (cmd, outp) in enumerate(inp):
        if outp == 'b':
            continue
        tmp = lhs.get(outp)
        if tmp is None:
            continue
        for j in tmp:
            g.add_edge(i, j)

    ordered = list(nx.topological_sort(g))
    vars = {'b': part1(raw)}
    for i in ordered:
        cmd, outp = inp[i]
        apply(cmd, outp, vars)
    return vars['a']
