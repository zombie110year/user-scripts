#! env python
# -*- coding: utf-8 -*-
import sys
from argparse import ArgumentParser

def _conv(path: str, from_encoding: str, to_encoding: str):
    with open(path, "rt", encoding=from_encoding) as file:
        content = file.read()
    print(content)
    flag = input(
            "conv correct? {}->{} [y/n] n> ".format(from_encoding, to_encoding)
    )
    if flag:
        with open(path, "wt", encoding=to_encoding) as file:
            file.write(content)

def main():
    parser = ArgumentParser(
            prog="conv",
            description="转换文件字符编码"
    )
    parser.add_argument(
            "path", help="欲转换文件", metavar="example.txt"
    )
    parser.add_argument(
            "--from", help="原编码", metavar="gbk", default="gbk",
            required=False, dest="_from"
    )
    parser.add_argument(
            "--to", help="目标编码", metavar="utf-8", default="utf-8",
            required=False, dest="_to"
    )
    args = parser.parse_args()

    _conv(args.path, args._from, args._to)
    sys.exit(0)

if __name__ == "__main__":
    main()
