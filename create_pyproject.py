from pathlib import Path
from argparse import ArgumentParser
from subprocess import run


def getName():
    parser = ArgumentParser(
        description="在当前目录下创建一个 Python Package 项目"
    )
    parser.add_argument(
        "name", help="项目的名称", metavar="proj_name", type=str
    )
    args = parser.parse_args()
    return args.name


def main():
    proj_name = getName()

    resource_dir = Path(__file__).parent / "_static"
    gitignore_file = resource_dir / "Python.gitignore"
    setup_file = resource_dir / "setup.temp.py"
    cwd = Path()

    # 创建 .gitignore 文件
    with gitignore_file.open("rb") as file:
        content = file.read()
    gitignore = cwd / ".gitignore"
    with gitignore.open("wb") as file:
        file.write(content)

    # 创建 setup.py 文件
    with setup_file.open("rb") as file:
        content = file.read()
    setup = cwd / "setup.py"
    with setup.open("wb") as file:
        file.write(content)

    # 创建 proj_name 目录以及 __init__.py __main__.py 文件
    proj_dir = cwd / proj_name
    proj_dir.mkdir(exist_ok=True)
    with (proj_dir / "__init__.py").open("wb") as file:
        pass
    with (proj_dir / "__main__.py").open("wb") as file:
        pass

    # 创建 MANIFEST.in 文件
    with (resource_dir / "py.manifest.in").open("rb") as file:
        content = file.read()
    with (cwd / "MANIFEST.in").open("wb") as file:
        file.write(content)

    # 创建 README.md 文件
    (cwd / "README.md").touch(exist_ok=True)
    # 创建 test 目录
    (cwd / "test").mkdir(exist_ok=True)
    # 创建 docs 目录
    (cwd / "docs").mkdir(exist_ok=True)
    # 创建 example 目录
    (cwd / "example").mkdir(exist_ok=True)

    # 创建 git 仓库
    run(["git", "init"])


if __name__ == "__main__":
    main()
