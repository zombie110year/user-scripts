#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
date
    2018-12-26 21:53:52
author
    Zombie110year
module
    get_date
description
    获取 YYYY-MM-DD hh:mm:ss 格式的时间字符串
"""

from time import localtime
import sys

gDATE_STYLE = {
    'default': "{year:>d}-{month:>02d}-{day:>02d} {hour:>02d}:{minute:>02d}:{second:>02d}"
}


def __getDate(raw=None, style='default'):
    tm = localtime(raw)
    year = tm.tm_year
    month = tm.tm_mon
    day = tm.tm_mday
    hour = tm.tm_hour
    minute = tm.tm_min
    second = tm.tm_sec
    return gDATE_STYLE.get(style).format(
        year=year,
        month=month,
        day=day,
        hour=hour,
        minute=minute,
        second=second
    )


def ipyMain(raw=None, style='default'):
    return __getDate(raw, style)


def main():
    print(__getDate(), end='')
    sys.exit(0)


if __name__ == "__main__":
    main()
