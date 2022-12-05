import hashlib
from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': None,
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    i = 1
    while True:
        if hashlib.md5((inp + str(i)).encode('utf-8')).hexdigest()[:5] == '00000':
            return i
        i += 1


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    i = 1
    while True:
        if hashlib.md5((inp + str(i)).encode('utf-8')).hexdigest()[:6] == '000000':
            return i
        i += 1
