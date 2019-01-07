#! /usr/bin/env python

import re
import json
from io import StringIO
import sys
from argparse import ArgumentParser

"""
将 markdown 文件转化为 ipynb, 使用 <!--%%--> 分割 Cell (借鉴了 #%% 在 .py 中的语法)

使用方法

md_to_ipynb.py -o output.ipynb input.md
"""

CELL_TYPE = [
    'markdown'
    'code',
]

META_DATA = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.7.1"
    }
}


class Cell:
    """
    一个 cell 是位于 NoteBook 下的 cells 对应的数组中的一个元素
    含有

    - cell_type = 'markdown'
    - execlution_count = None
    - metadata = dict()
    - source = list()
    - outputs = list()

    等属性.

    其中, execlution_count 是代码块运行计数, 可以不用设置, 当程序重新运行一次后就能正常排列.

    source 和 output 是输入和输出, 都是一个按行划分(包括换行符)的数组

    """

    def __init__(self, cell_type='markdown'):
        self.cell_type = cell_type
        # self.execlution_count = None  # 只有 code - type cell 才有这项属性
        self.metadata = dict()
        self.source = list()
        self.outputs = list()

    def toDict(self):
        resualt = dict()
        resualt['cell_type'] = self.cell_type
        resualt['metadata'] = self.metadata
        resualt['source'] = self.source
        resualt['outputs'] = self.outputs
        # resualt['execlution_count'] = self.execlution_count
        return resualt

    def setSource(self, content: str):
        buffer = StringIO()
        buffer.write(content)
        buffer.flush()
        buffer.seek(0, 0)
        self.source = buffer.readlines()
        buffer.close()
        return self.source


class NoteBook:
    """
    notebook 以 cells, metadata 以及 nbformat, nbformat_minor 四个部分组成, 前两者是容器元素, 后两者是两个整数.
    """

    def __init__(self, nbformat=4, nbformat_minor=2):
        self.cells = list()
        self.metadata = dict()
        self.nbformat = nbformat
        self.nbformat_minor = nbformat_minor

    def toDict(self):
        resualt = dict()
        resualt['cells'] = self.cells
        resualt['metadata'] = self.metadata
        resualt['nbformat'] = self.nbformat
        resualt['nbformat_minor'] = self.nbformat_minor
        return resualt

    def addCell(self, cell: Cell):
        one = cell.toDict()
        self.cells.append(one)
        return one

    def setMetadata(self, metadata=META_DATA):
        "设置元数据, 默认为 META_DATA 变量"
        self.metadata = metadata
        return metadata

    def setCells(self, content: str):
        """
        将文本按 <!--%%--> 分隔符划分为 Cell, 存储在 NoteBook 对象中
        """

        for source in re.split(r'<!--%%-->', content):
            cell = Cell()
            cell.setSource(source)
            self.addCell(cell)

        return self.cells


def getConf():
    parser = ArgumentParser(
        prog="md to ipynb",
        description="将 Markdown 文件转换为 jupyter notebook, 用 <!--%%--> 划分 cell"
    )
    parser.add_argument("path", help="输入", metavar="input.md")
    parser.add_argument("-o", dest="output", help="输出",
                        metavar="output.ipynb", default="output.ipynb")
    return parser.parse_args()


def main():
    args = getConf()
    path = args.path
    output = args.output
    with open(path, "rt", encoding="utf-8") as file:
        content = file.read()
    notebook = NoteBook()
    notebook.setMetadata()
    notebook.setCells(content)
    resualt = notebook.toDict()
    resualt = json.dumps(resualt, indent=1, ensure_ascii=False)
    with open(output, "wt", encoding="utf-8") as file:
        file.write(resualt)
    print("output file: {}".format(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
