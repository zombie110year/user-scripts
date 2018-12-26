#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from base64 import b64encode
from base64 import b64decode
from argparse import ArgumentParser
import sys


def main():
    parser = ArgumentParser(
        prog="Base64 编码解码",
        description="可用于编码, 解码. 默认是编码模式"
    )
    parser.add_argument(
        "-r", "--decode",
        dest="decode",
        help="解码",
        required=False,
        action="store_true",
        default=False,
    )
    args = parser.parse_args()

    strings = map(
        lambda x: x.rstrip(),
        sys.stdin.readlines()
    )

    sys.stdout.flush()

    if args.decode:
        for line in strings:
            print(decode(line))
    else:
        for line in strings:
            print(encode(line))

    sys.exit(0)


def encode(string: str) -> str:
    b_string = string.encode()
    b_string = b64encode(b_string)
    string = b_string.decode()
    return string


def decode(string: str) -> str:
    b_string = string.encode()
    b_string = b64decode(b_string)
    string = b_string.decode()
    return string


if __name__ == "__main__":
    main()
