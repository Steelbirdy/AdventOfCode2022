import __main__
import inspect
from pathlib import Path
from typing import Any, Callable, Optional, Type


AocInput = str | list[str]
AocFunc = Callable[[Any], Any]


def get_input() -> str:
    script = Path(__main__.__file__)    \
        .relative_to(Path.cwd())        \
        .with_suffix('.txt')            \
        .name
    input_path = Path.cwd().parent / "input" / script
    with open(input_path) as fp:
        return fp.read()


def get_input_lines() -> list[str]:
    return [line.strip() for line in get_input().split('\n')]


input_funcs: dict[Type[AocInput], Callable[[], Any]] = {
    str: get_input,
    list[str]: get_input_lines,
}


def _aoc(func: AocFunc):
    sig = inspect.signature(func)
    assert len(sig.parameters) == 1
    param = list(sig.parameters.values())[0]
    inp = input_funcs[param.annotation]()
    return func(inp)


def aoc(part1: AocFunc, part2: Optional[AocFunc] = None):
    print("Part 1:", _aoc(part1))
    if part2 is not None:
        print("Part 2:", _aoc(part2))
