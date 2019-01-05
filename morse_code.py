#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
date
    2019-01-05 13:47:55
author
    Zombie110year
module
    morse_code
description
    编码/解码 摩尔斯电码
"""

from argparse import ArgumentParser
import sys

# char <-> code
gMORSE_MAP = (
    ("a", ".-"),
    ("b", "-..."),
    ("c", "-.-."),
    ("d", "-.."),
    ("e", "."),
    ("f", "..-."),
    ("g", "--."),
    ("h", "...."),
    ("i", ".."),
    ("j", ".---"),
    ("k", "-.-"),
    ("l", ".-.."),
    ("m", "--"),
    ("n", "-."),
    ("o", "---"),
    ("p", ".--."),
    ("q", "--.-"),
    ("r", ".-."),
    ("s", "..."),
    ("t", "-"),
    ("u", "..-"),
    ("v", "...-"),
    ("w", ".--"),
    ("x", "-..-"),
    ("y", "-.--"),
    ("z", "--.."),
    ("0", "-----"),
    ("1", ".----"),
    ("2", "..---"),
    ("3", "...--"),
    ("4", "....-"),
    ("5", "....."),
    ("6", "-...."),
    ("7", "--..."),
    ("8", "---.."),
    ("9", "----."),
    (".", ".-.-.-"),
    (":", "---..."),
    (",", "--..--"),
    (";", "-.-.-."),
    ("?", "..--.."),
    ("=", "-...-"),
    ("'", ".----."),
    ("/", "-..-."),
    ("!", "-.-.--"),
    ("-", "-....-"),
    ("_", "..--.-"),
    ("\"", ".-..-."),
    ("(", "-.--."),
    (")", "-.--.-"),
    ("$", "...-..-"),
    ("&", ".-..."),
    ("@", ".--.-."),
    ("+", ".-.-."),
)


class MorseError(Exception):
    "当遇到不在 ASCII 字符中的字符时, 抛出错误"
    pass


class MorseCode:
    """
    摩尔斯电码的编码/解码器

    :param dot: 用来表示点号 . 的字符
    :param line: 用来表示横线 - 的字符

    :method:`encode` 编码, str -> morse code
    :method:`decode` 解码, morse code -> str
    """

    def __init__(self, dot=".", line="-"):
        self.DECODE_MAP = dict(
            map(
                lambda x: x[::-1], gMORSE_MAP
            )
        )
        self.ENCODE_MAP = dict(
            gMORSE_MAP
        )
        self.DOT = dot
        self.LINE = line

    def _decode(self, content):
        "解码, 假设输入是合法的. morse -> str"
        content = content.split(' ')
        content = list(map(
            lambda x: self.DECODE_MAP[x], content
        ))
        return ''.join(content)

    def _encode(self, content):
        "编码, 假设输入是合法的. str -> morse"
        content = list(content)
        content = list(map(
            lambda x: self.ENCODE_MAP[x], content
        ))
        return ' '.join(content)

    def _transDotLine(self, content, encode=True):
        "将用于表示点 或 线的符号转换"
        if encode:
            content = content.replace('-', self.LINE)
            content = content.replace('.', self.DOT)
        else:
            content = content.replace(self.LINE, "-")
            content = content.replace(self.DOT, ".")
        return content

    def _encodePreprocess(self, content):
        """
        检查是否存在越界字符, 将字母转为小写
        """
        content = list(content.lower())
        content = ''.join(list(filter(
            lambda x: x not in (" ", "\n", "\t"), content
        )))
        for char in content:
            if char not in self.ENCODE_MAP:
                raise MorseError('only ascii char')
        return content

    def encode(self, content):
        "str -> morse"
        content = self._encodePreprocess(content)
        content = self._encode(content)
        content = self._transDotLine(content)
        return content

    def decode(self, content):
        "morse -> str"
        content = self._transDotLine(content, encode=False)
        return self._decode(content)


def main():
    parser = ArgumentParser(
        prog="MorseEncodeDecode",
        description="摩尔斯电码的编码与解码"
    )
    parser.add_argument(
        "--decode", help="运行模式, encode/decode, 默认 encode",
        action="store_true", default=False, required=False
    )
    parser.add_argument(
        "--dot", help="设置点号的字符, 默认为 .",
        metavar=".", default=".", required=False
    )
    parser.add_argument(
        "--line", help="设置点号的字符, 默认为 .",
        metavar=".", default="-", required=False
    )

    args = parser.parse_args()

    m = MorseCode(
        dot=args.dot, line=args.line
    )

    # 提示符
    if args.decode:
        mode = "decode"
    else:
        mode = "encode"

    print("({})>".format(mode), file=sys.stderr, end=' ')
    content = input()

    if args.decode:
        resualt = m.decode(content)
    else:
        resualt = m.encode(content)

    print(resualt, end='')
    sys.exit(0)


if __name__ == "__main__":
    main()
