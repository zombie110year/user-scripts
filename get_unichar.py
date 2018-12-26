#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import win32clipboard as c
import sys
"""
date
    2018-12-26 20:05:16
author
    Zombie110year
module
    get_unichar
description
    获取一些特殊的 Unicode 字符. 直接放入剪贴板中
interactivation
    ipyMain 针对 ipython shell 提供的接口
    main     针对命令行调用提供的接口
"""

ERROR_MSG = """

没找到你需要的字符, 支持的字符如下表:

=============== ================================================================
代码            含义
--------------- ----------------------------------------------------------------
ZWS             零宽空格
ZWNJ            零宽非连字符
ZWJ             零宽度连字符
LTRO            从左到右控制符
RTLO            从右到左控制符
BOM             0xFEFF BOM 头 标记
================================================================================
"""


def __getdoc():
    print(ERROR_MSG, file=sys.stderr)
    return False


gUNICODE_MAP = {
    "ZWS": "\u200b",
    "ZWNJ": "\u200c",
    "ZWJ": "\u200d",
    "LTRO": "\u202d",
    "RTLO": "\u202e",
    "BOM": "\ufeff",
}


def __get(key, self=gUNICODE_MAP):
    """
    获取 gUNICODE_MAP 中的字符
    """
    if key in self:
        return self[key]
    else:
        sys.exit(404)


def ipyMain(key, self=gUNICODE_MAP):
    """
    为 Ipython Shell 设计.

    返回需要获取的字符.
    """
    key = key.upper()

    target = gUNICODE_MAP.get(key, False)

    if target:
        return target
    else:
        print(ERROR_MSG, file=sys.stderr)


def main():
    """
    为 CLI 设计的接口
    """
    parser = ArgumentParser(
        prog="get_unichar",
        description="获取一些特殊的 Unicode 字符, 直接存入剪贴板"
    )
    parser.add_argument("key", help="对应 Unicode 字符的名称简写")
    key = parser.parse_args().key.upper()

    target = gUNICODE_MAP.get(key, False)

    if target:
        c.OpenClipboard()
        c.EmptyClipboard()
        c.SetClipboardData(c.CF_UNICODETEXT, target)
        c.CloseClipboard()
        sys.exit(0)
    else:
        __getdoc()


if __name__ == "__main__":
    main()
