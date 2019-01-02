#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
date
    2019-01-01 01:59:21
author
    Zombie110year
module
    splitChapter
description
    解析 Markdown 的目录结构
"""
from pathlib import Path
import re
from sys import argv
# %%

# %%


class EbookNode:
    """
    一个电子书单元, 拥有属性:

    - ``code`` 编号
    - ``name`` 名称或标题
    - ``childs`` 子节点, 如, "书" 下有 "卷", "卷" 下有 "章"
    - ``content`` 内容, 为每一章所有. 是按行存储的列表.

    拥有方法:

    - ``setCode`` 设置编号.
    - ``setName`` 设置名称.
    - ``addChild`` 添加子节点.
    - ``setParent`` 设置父节点, 在父节点 addChild 时自动调用子节点的 setParrent 方法.
    - ``setContent`` 设置内容.
    - ``addContent`` 将新的内容添加到原有内容的后面.
    """

    level = 1
    regex_pattern = r"# (?P<code>)(?P<name>\S+)"

    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name
        self.content = []
        self.childs = []
        self.parent = None
        self.file = None

    def setCode(self, code):
        if code in ('', None):
            self.code == None
        else:
            self.code = int(code)

    def setName(self, name):
        self.name = name

    def addChild(self, child):
        self.childs.append(child)
        child.setParent(self)

    def setParent(self, parent):
        self.parent = parent

    def setContent(self, content):
        self.content = content

    def addContent(self, new_content):
        self.content.append(new_content)

    def toFileSystem(self):
        """
        将此书写入文件系统
        """
        self.file = Path("{}".format(self.name))
        self.file.mkdir()
        if self.content:
            with (self.file / "__this__.txt").open("wt", encoding="utf-8") as file:
                file.write("\n\n".join(self.content))
        for child in self.childs:
            child.toFileSystem()


class Volumn(EbookNode):
    level = 2
    regex_pattern = r"^## 第(?P<code>\d{0,1})卷 ?(?P<name>\S+)$"

    def toFileSystem(self):
        parent_dir = self.parent.file
        self.file = parent_dir / "{}-{}".format(self.code, self.name)
        self.file.mkdir()
        if self.content:
            with (self.file / "__this__.txt").open("wt", encoding="utf-8") as file:
                file.write("\n\n".join(self.content))
        for child in self.childs:
            child.toFileSystem()


class Chapter(EbookNode):
    level = 3
    regex_pattern = r"^### 第(?P<code>\d{1,4})章 ?(?P<name>\S+)$"
    content_template = """{symbol}
第{code:0>4d}章 {name}
{symbol}

{content}
"""

    def toFileSystem(self):
        parent_dir = self.parent.file
        self.file = parent_dir / "{:0>4d}-{}.rst".format(self.code, self.name)
        output = self.file.open("wt", encoding="utf-8")
        content = self.content_template.format(
            code=self.code,
            name=self.name,
            symbol="#"*(len(self.name) * 2 + 9),
            content="\n\n".join(self.content),
        )
        output.write(content)
        output.close()


class Line(str):
    def getLevel(self):
        level = 0
        for char in self:
            if char == "#":
                level += 1
                continue
            else:
                break
        return level

# %%


def readFile(path: str) -> list:
    """
    读取对应路径的文件, 转化为按行分隔的字符串列表.

    :para path: 字符串, 文件的相对/绝对路径.
    :return: list, 按行分隔的内容.
    """
    with open(path, encoding="utf-8") as file:
        content = file.readlines()
    content = list(map(lambda x: x.rstrip(), content))                  # 去掉换行
    content = list(
        filter(lambda x: True if x else False, content)
    )  # 去掉空字符串
    return content

# %%


LEVEL_NODE = {
    1: EbookNode,
    2: Volumn,
    3: Chapter,
}


def parseFile(content: list):
    """
    将按行分隔的内容解析为 书/卷/章

    :para content: list, 由 readFile 函数得到的内容列表.
    :return: 一个以 EbookNode 为根节点的树.
    """
    stack = []
    level = 0
    while True:
        this_line = Line(content.pop(0))
        this_level = this_line.getLevel()
        if this_level == 0:
            stack[-1].addContent(this_line)
        else:
            new = LEVEL_NODE[this_level]()
            matched = re.match(new.regex_pattern, this_line)
            new.setCode(matched.group('code'))
            new.setName(matched.group('name'))

            if this_level > level:
                stack.append(new)
                if this_level > EbookNode.level:
                    stack[-2].addChild(new)
            elif this_level == level:
                stack[-1] = new
                stack[-2].addChild(new)
            else:
                stack = stack[:this_level-1]
                stack.append(new)
                stack[-2].addChild(new)
            level = this_level
        if len(content) == 0:
            return stack[0]


# %%


def writeFile(root: EbookNode):
    root.toFileSystem()


if __name__ == "__main__":
    content = readFile(argv[1])
    root = parseFile(content)
    writeFile(root)
