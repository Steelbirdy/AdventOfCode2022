from ..utils import aoc


fmt = '{}'
kwargs = {
    'sep': '\n',
    'meta_sep': None,
    'case_sensitive': False,
}


@aoc(fmt, **kwargs)
def part1(inp) -> int:
    bad = ('ab', 'cd', 'pq', 'xy')
    vowels = 'aeiou'
    def nice(s) -> bool:
        if any(b in s for b in bad):
            return False
        last = '0'
        rep = False
        vowel_count = 0
        for c in s:
            if last == c:
                rep = True
            vowel_count += c in vowels
            last = c
        return rep and vowel_count >= 3
    return sum(map(nice, inp))


@aoc(fmt, **kwargs)
def part2(inp) -> int:
    def nice(s) -> bool:
        rep = False
        btwn = False
        pairs = set()
        pair = '012'
        for c in s:
            if pair[1:2] == c:
                btwn = True
            pair = pair[1:] + c
            if pair[1:] in pairs:
                rep = True
            pairs.add(pair[:2])
        return rep and btwn
    return sum(map(nice, inp))
