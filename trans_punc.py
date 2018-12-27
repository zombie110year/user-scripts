#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
date
    2018-12-27 20:20:46
author
    Zombie110year
module
    trans_punc
description
    转换文本中的标点符号
"""

import re
import sys


TRANS_DICT = {
    "（":   "(",
    "）":   ")",
    "【":   "[",
    "】":   "]",
    "《":   "<",
    "》":   ">",
    "，":   ",",
    "。":   ".",
    "：":   ":",
    "；":   ";",
    "“":   "\"",
    "”":   "\"",
    "‘":   "\'",
    "’":   "\'",
    "？ *":   "?",
    "、 *":   ",",
    "！ *":   "!",
    "…… *":   "...",
    "—":   "--",
}

TRANS_DICT_R = {
    "(":    "（",
    ")":    "）",
    "[":    "【",
    "]":    "】",
    "<":    "《",
    ">":    "》",
    ",":    "，",
    ".":    "。",
    ":":    "：",
    ";":    "；",
    "?":    "？",
    ",":    "、",
    "!":    "！",
    "...":    "……",
    "-":    "—",
}


def _transPunctuation(source: str, reverse=False):
    if reverse:
        mapping = TRANS_DICT_R
    else:
        mapping = TRANS_DICT

    for key in mapping:
        source = re.sub(key, mapping.get(key), source)

    return source


def main():
    source = sys.stdin.read()
    content = _transPunctuation(source)
    print(content, end='')
    sys.exit(0)


if __name__ == "__main__":
    main()
