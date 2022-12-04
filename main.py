from datetime import datetime, timezone, timedelta
import dotenv
import importlib
import os
from pathlib import Path
import requests
import sys
from typing import Any, Callable, Optional


_cwd = Path(__file__).parent
_template_file = _cwd / "templates" / "template.py.example"

assert dotenv.load_dotenv(), ".env file not found!"
_year = os.getenv('AOC_YEAR')
_year_folder = os.getenv('AOC_FOLDER_FORMAT').format(year=_year)

cmd = None


def get_day(day: Optional[int]) -> int:
    if day is None:
        today = datetime.now(tz=timezone(timedelta(hours=-5)))
        if today.month != 12:
            print("You specify the day number in months other than December.")
            raise ValueError
        day = today.day
        if day > 24:
            print("You must specify the day number after advent ends.")
            raise ValueError
        if day != 24 and today.hour == 23 and cmd == 'init':
            day = day - 1

    if not (1 <= day <= 24):
        print("Invalid day, must be between 1 and 24 inclusive.")
        raise ValueError
    return day


def retrieve_aoc_input(day: int, dest: Optional[Path] = None):
    if dest is not None and dest.exists():
        return

    session_token = os.getenv('AOC_SESSION_TOKEN')
    if session_token == "your-session-token-here":
        print('You need to put your session token into the `.env` file!')
        raise ValueError

    response = requests.get(f"https://adventofcode.com/{_year}/day/{day}/input", cookies={'session': session_token})
    if response.status_code != 200:
        raise ValueError(str(response.content))
    text = response.text
    if dest is not None:
        with open(dest, mode='w') as fp:
            fp.write(text.strip())


def get_input(day: int, fpath: Path) -> str:
    script = fpath.with_suffix('.txt').name
    input_folder = _cwd / "input" / _year_folder
    if not input_folder.exists():
        input_folder.mkdir(parents=True, exist_ok=False)
    input_path = input_folder / script
    retrieve_aoc_input(day, input_path)
    with open(input_path) as fp:
        return fp.read()


def get_input_lines(day: int, fpath: Path) -> list[str]:
    return [line.strip() for line in get_input(day, fpath).split('\n')]


input_funcs: dict[type, Callable[[int, Path], Any]] = {
    str: get_input,
    list[str]: get_input_lines,
}


def show_usage():
    print("""Usage: python main.py [run|init] [day:int]
    Default behavior is to run the current day's file. """)


def get_aoc_file(day: int) -> Path:
    day_file = os.getenv('AOC_FILE_FORMAT').format(day=day)
    return _cwd / "src" / _year_folder / f"{day_file}.py"


def init_aoc(day: Optional[str] = None):
    day = get_day(int(day) if day is not None else None)
    fpath = get_aoc_file(day)
    if not fpath.parent.exists():
        fpath.parent.mkdir(parents=True, exist_ok=False)
    if not fpath.exists():
        with open(_template_file) as fp:
            template = fp.read()
        with open(fpath, mode='w') as fp:
            fp.write(template)
    print(f"Initialized at .\\{fpath.relative_to(_cwd)}")


def run_aoc(day: Optional[str] = None):
    gave_day = day is not None
    day = get_day(int(day) if day is not None else None)
    fpath = get_aoc_file(day)
    if not fpath.exists():
        if gave_day:
            print(f"File does not exist. Please run `python main.py init {day}` to create a new file for day "
                  f"{day}'s puzzle.")
        else:
            print("File does not exist. Please specify the day if you do not want to run today's puzzle.")
        return
    try:
        mod = importlib.import_module(f"src.{_year_folder}.{fpath.name[:-3]}")
    except Exception as e:
        print(f'Error in file: {e}')
        return

    if not hasattr(mod, 'part1'):
        print("File does not have function 'part1', which is required.")
        return
    part1_func = mod.part1
    print(f'Part 1: {run_aoc_func(day, part1_func, fpath)}')

    if hasattr(mod, 'part2'):
        part2_func = mod.part2
        print(f'Part 2: {run_aoc_func(day, part2_func, fpath)}')
    else:
        print('Part 2: Not implemented')


def run_aoc_func(day: int, func, fpath: Path):
    return func(get_input(day, fpath))


def main(args):
    global cmd

    if not args:
        run_aoc()
        return

    cmd = args[0]
    day = args[1] if len(args) > 1 else None
    if cmd == "run":
        run_aoc(day=day)
    elif cmd == "init":
        init_aoc(day=day)
    else:
        show_usage()


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Exception as e:
        print(f"Error: {e}")
        show_usage()
