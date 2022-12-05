import inspect
import parse
from typing import Any, Callable, Optional, TypeVar, Union


def next_permutation(x: list, lt=...):
    N = len(x)
    if lt is ...:
        lt = lambda a, b: a < b

    i = 0
    j = 0
    for i in range(N - 2, -1, -1):
        if lt(x[i], x[i+1]):
            break

    if i < 0:
        x.reverse()
    else:
        for j in range(N - 1, i, -1):
            if lt(x[i], x[j]):
                break
        x[i], x[j] = x[j], x[i]
        x[i+1:N] = x[i+1:N][::-1]


_In = TypeVar('_In')
_Out = TypeVar('_Out')


def __aoc_decorator(func: Callable[[_In], _Out], fmt: Optional[str], sep: Optional[str], meta_sep: Optional[str], case_sensitive: bool):
    def decorated(inp: str) -> _Out:
        raw_inp = inp
        unnest = 0
        raw_inp = inp
        if meta_sep is None:
            inp = [inp]
            unnest += 1
        else:
            inp = inp.split(meta_sep)
        if sep is None:
            inp = [inp]
            unnest += 1
        else:
            inp = [x.split(sep) for x in inp]
        if fmt is not None:
            maybe_unwrap = lambda x: x
            if fmt.count('{') == 1:
                maybe_unwrap = lambda x: x[0]
            res: list[list[parse.Result]] = [
                [maybe_unwrap(parse.parse(fmt, y, case_sensitive=case_sensitive).fixed) for y in x]
                for x in inp]
        else:
            res: list[list[str]] = inp
        for _ in range(unnest):
            res = res[0]
        res: _In

        if len(inspect.signature(func).parameters) == 2:
            return func(res, raw_inp)
        return func(res)
    return decorated


def aoc(fmt: str, *, sep: str = '\n', meta_sep: str = None, case_sensitive: bool = False):
    def inner(func: Callable[[Any], Any]):
        return __aoc_decorator(func=func, fmt=fmt, sep=sep, meta_sep=meta_sep, case_sensitive=case_sensitive)
    return inner
