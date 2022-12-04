import parse
from typing import Any, Callable, Optional, TypeVar, Union


_In = TypeVar('_In')
_Out = TypeVar('_Out')


def __aoc_decorator(func: Callable[[_In], _Out], fmt: Optional[str], sep: Optional[str], meta_sep: Optional[str], case_sensitive: bool):
    def decorated(inp: str) -> _Out:
        unnest = 0
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
        return func(res)
    return decorated


def aoc(fmt: str, *, sep: str = '\n', meta_sep: str = None, case_sensitive: bool = False):
    def inner(func: Callable[[Any], Any]):
        return __aoc_decorator(func=func, fmt=fmt, sep=sep, meta_sep=meta_sep, case_sensitive=case_sensitive)
    return inner
