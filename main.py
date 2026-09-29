import argparse

import sys
from pathlib import Path
import reestr
import match


parser = argparse.ArgumentParser(
    prog="figures",
    description="Разбор геометрических фигур из файла.",
)
parser.add_argument(
    "-f", "--file",
    required=True,
    type=Path,
    metavar="PATH",
    help="путь к входному файлу",
)
parser.add_argument(
    "-o", "--oper",
    required=True,
    choices=["print", "count"],
    help="операция: print или count",
)
parser.add_argument(
    "--log",
    nargs="?",
    const="",
    default=None,
    metavar="PATH",
    help="вывод логов",
)

args = parser.parse_args()


if args.log:                                   # --log path.log
    log_path = Path(args.log).expanduser().resolve()
    reestr.set_seen(str(log_path))              # запоминаем в реестре
else:                                          # --log или без --log вовсе
    saved = reestr.get_seen()
    log_path = Path(saved) if saved else None


log_buffer: list[str] = []

def log(msg: str) -> None:
    log_buffer.append(msg)


def flush_logs() -> None:
    if log_path is None:
        for line in log_buffer:
            print(line, file=sys.stderr)
    else:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as f:
            f.write("\n".join(log_buffer) + "\n")
objects=[]
errors=[]

try:
    with open(args.file, "r", encoding="utf-8") as f:
        objects = f.read().split("\n")
except FileNotFoundError:
    log(f"error: file not found: {args.file}")
    flush_logs()
    sys.exit(1)

list_of_object, bad_lines = match.list_str_to_list_obj(objects)

for line in bad_lines:
    log(f"string not right: {line}")

if args.oper == "print":
    strs = match.list_obj_to_list_str(list_of_object)
    if not strs:
        print("(no objects)")
    else:
        print("Objects in file:")
        for s in strs:
            print(f"  {s}")

elif args.oper == "count":
    print(f"Objects: {len(list_of_object)}")


flush_logs()



