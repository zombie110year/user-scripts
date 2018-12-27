#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
date
    2018-12-27 11:25:13
author
    Zombie110year
module
    make_qr
description
    使用 qrcode 库, 生成二维码图像
"""

import qrcode
from argparse import ArgumentParser
import sys


def _getArgs():
    parser = ArgumentParser(
        prog="make QR",
        description="从 stdin 读取文本, 将其转化为 QR 码, 默认以 png 格式保存"
    )
    parser.add_argument(
        "-o",
        dest="output",
        metavar="qr.png",
        help="将图像保存到 %(default)s",
        required=False,
        default="qr.png",
    )

    return parser.parse_args()


def main():

    args = _getArgs()
    content = sys.stdin.read()
    img = qrcode.make(content)
    img.save(args.output)

    sys.exit(0)


if __name__ == "__main__":
    main()
