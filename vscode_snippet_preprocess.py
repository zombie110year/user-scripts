#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
date
    2019-01-05 01:41:21
author
    Zombie110year
module
    vscode_snippet_description_preprocess
description
    预处理 VsCode 的代码片段 json, 将 list 格式的 description 项目合成为 换行符 ``\n`` 分隔的 string.
    从 stdin 读取, 向 stdout 输出, 善用 pipeline.
"""

import json
import sys
import re


def _parse(content):
    """
    输入 json 格式的字符串, 返回处理后的
    """
    root = json.loads(content)
    for snippet in root:
        if isinstance(root[snippet]["description"], list):
            root[snippet]["description"] = "\n".join(
                root[snippet]["description"]
            )

    content = json.dumps(root, sort_keys=True, indent=4)

    content = re.sub(r"^ {4}", "\t", content)
    content = re.sub(r"^ {8}", "\t\t", content)
    content = re.sub(r"^ {12}", "\t\t\t", content)

    return content


def ipyMain(content):
    return _parse(content)


def main():
    content = sys.stdin.read()
    resualt = _parse(content)
    print(resualt, end='')
    sys.exit(0)


def test():
    with open("test.json", "rt", encoding="utf-8") as file:
        content = file.read()

    resualt = _parse(content)
    print(resualt, end='')
    sys.exit(0)


if __name__ == "__main__":
    main()
