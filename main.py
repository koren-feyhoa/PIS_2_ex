import argparse
import sys
from pathlib import Path

import match
import re
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

args = parser.parse_args()
objects=[]

try:
    objects=open(sys.argv[2],'r').read().split('\n')
    list_of_object= match.list_str_to_list_obj(objects)
except FileNotFoundError:
    print(f"error: file not found: {args.file}", file=sys.stderr)

if args.oper == "print":
    if not objects:
        print("(no objects)")
    else:
        print("Objects in file:")
        for obj in objects:
            print(f"  {obj}")

elif args.oper == "count":
    print(f"Objects: {len(objects)}")




