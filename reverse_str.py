#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
date
    2018-12-26 21:26:24
author
    Zombie110year
module
    reverse_str
description
    从 stdin 中读取所有输入, 直到 EOF
    向 stdout 打印逆序排列的字符串
"""

import sys


def main():
    """
    从 stdin 中读取所有输入, 直到 EOF
    向 stdout 打印逆序排列的字符串
    """
    string = sys.stdin.read()
    print(string[::-1], end='')
    sys.exit(0)


if __name__ == "__main__":
    main()
