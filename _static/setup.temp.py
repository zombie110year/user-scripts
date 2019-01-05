"""
#########################
关于编写 setup 的一些说明
#########################

install_requires
================

``install_requires`` 是一个列表, 里面每一项字符串都书写依赖项的版本规则.

例如::

    install_requires = [
        "example1==1.0.0", # 依赖该项目的 1.0.0 版本
        "example2!=1.0.1", # != 表示不依赖对应版本, 而是其他版本
        "example3<=1.0.2",
        "example4>=1.0.3",
        "example5<1.0.4",
        "example6>1.0.5",
    ]

多个版本之间可以用逗号 ``,`` 连接, 表示 且 关系. 如果是 ``==`` 运算符, 则是 或 关系::

    "example==1.0.0, ==1.0.1, < 2"
"""

from setuptools import setup, find_packages

# * 项目的名字
PROJ_NAME = ''

# * 项目主页
URL = ''

# * 版本号
VERSION = "0.0"

# * 短描述
DESCRIPTION = ""

# * 长描述
with open("README.md", "rt", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()

# * 协议
with open("LICENSE", "rt", encoding="utf-8") as file:
    LICENSE = file.read()

# * 包的分类
CLASSIFIERS = [
    "Programming Language :: Python",
]

# * 搜索包的关键字
KEYWORDS = [
    "",
]

# * 包所支持的平台
PLATFORMS = [
    "win32",
]

# * entry_points 包的程序入口.

ENTRY = {
    'console_script': [
        "command=package.module::function",
    ],
    'gui_script': [
        "cmmand=pkg.mod::func",
    ],
}

# * 该程序的依赖项

REQUIRE = [
    "package==version",
]

AUTHOR = "Zombie110year"
EMAIL = "zombie110year@outlook.com"


setup(
    name=PROJ_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    platforms=PLATFORMS,
    entry_points=ENTRY,
)
