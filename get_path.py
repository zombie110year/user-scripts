#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
date
    2018-12-26 21:42:57
author
    Zombie110year
module
    get_path
description
    获取文件的绝对路径
"""

from pathlib import Path
from argparse import ArgumentParser
import sys

TEMPLATE = "{origin:<LENGTH} => {absolute:<}"


def ipyMain(glob):
    """
    输入通配符, 获取目标对象的绝对路径

    :param glob: 路径通配符字符串

    :return:    包含了 (原路径, 绝对路径) 的列表
    """
    origin = []
    absolutes = []

    _ = Path(glob)
    parent = _.parent
    filename = _.name
    if "*" in filename:
        origin = list(parent.glob(filename))
    else:
        origin.append(_)

    for i in origin:
        absolutes.append(i.absolute())

    result = list(zip(origin, absolutes))
    return result


def main():
    parser = ArgumentParser(
        prog="Get-Location",
        description="获取输入对象的绝对路径"
    )
    parser.add_argument(
        "path",
        nargs="*"
    )
    paths = parser.parse_args().path
    results = []
    max_length = 0

    for glob in paths:
        results.extend(ipyMain(glob))

    for origin, absolute in results:
        length = len(origin.name)
        if length > max_length:
            max_length = length

    temp = TEMPLATE.replace("LENGTH", "{}".format(max_length), 1)

    for origin, absolute in results:
        print(temp.format(
            origin=str(origin),
            absolute=str(absolute),
        ))
    sys.exit(0)


if __name__ == "__main__":
    main()
