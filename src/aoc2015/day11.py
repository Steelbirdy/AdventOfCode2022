from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': None,
    'meta_sep': None,
    'case_sensitive': False,
}


def next_pw(pw: str) -> str:
    N = len(pw)
    i = N - 1
    while i >= 0 and pw[i:i+1] == 'z':
        pw = pw[:i] + 'a' + pw[i+1:]
        i = i - 1
    if i >= 0:
        pw = pw[:i] + chr(ord(pw[i:i+1]) + 1) + pw[i+1:]
    return pw


def check(pw: str) -> bool:
    last = '012'
    bad = 'iol'
    strt = False
    pairs = 0
    if any(b in pw for b in bad):
        return False
    for c in pw:
        if ord(last[1:2]) == ord(c) - 2 and ord(last[2:3]) == ord(c) - 1:
            strt = True
        if last[2:] == c and last[1:2] != c:
            pairs += 1
        last = last[1:] + c
    return pairs >= 2 and strt


@aoc(fmt, **kwargs)
def part1(inp) -> str:
    pw = next_pw(inp)
    while not check(pw):
        pw = next_pw(pw)
        # print(pw)
    return pw


@aoc(fmt, **kwargs)
def part2(_, raw) -> str:
    pw = next_pw(part1(raw))
    while not check(pw):
        pw = next_pw(pw)
        # print(pw)
    return pw
