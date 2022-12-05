from ..utils import aoc
import json


fmt = '{}'
kwargs = {
    'sep': None,
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    count = 0

    def obj(x):
        if any(v == 'red' for v in x.values()):
            for k, v in x.items():
                json.loads(json.dumps(k), object_hook=obj, parse_int=lambda x: parse_int(x, True))
                json.loads(json.dumps(v), object_hook=obj, parse_int=lambda x: parse_int(x, True))
            return None
        return x

    def parse_int(x):
        nonlocal count
        x = int(x)
        count += x
        return x

    json.loads(inp, parse_int=parse_int)
    return count


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    count = 0

    def obj(x):
        if any(v == 'red' for v in x.values()):
            for k, v in x.items():
                json.loads(json.dumps(k), object_hook=obj, parse_int=lambda x: parse_int(x, True))
                json.loads(json.dumps(v), object_hook=obj, parse_int=lambda x: parse_int(x, True))
            return None
        return x

    def parse_int(x, sub=False):
        nonlocal count
        x = int(x)
        if sub:
            count -= x
        else:
            count += x
        return x

    json.loads(inp, object_hook=obj, parse_int=parse_int)
    return count
