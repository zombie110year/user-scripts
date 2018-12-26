from pathlib import Path
from hashlib import md5

__gPROCESSED = [
    "New                                      Old",
    "======================================== ===",
]
# 用于生成转换说明


def __splitName(name):
    parts = name.split(".")
    ext_name = parts[-1]
    base_name = ".".join(parts[:-1])
    return base_name, ext_name


def __renameFile(file: Path, do):
    "重命名为其自身 md5 值, 保留扩展名, 如果已经命名为md5sum, 则跳过"
    global __gPROCESSED

    base_name, ext = __splitName(file.name)

    with open(file, "rb") as context:
        md5sum = md5(context.read())
    md5name = md5sum.hexdigest()+"."+ext

    if file.name != md5name:
        __gPROCESSED.append(
            "{new} <- {raw}".format(raw=file.name, new=md5name)
        )
        if do:
            file.rename(md5name)
    else:
        __gPROCESSED.append(
            "{new} == {raw}".format(raw=file.name, new=md5name)
        )


def __getFiles(glob: str):
    "通过通配符获取当前目录下所有符合条件的文件"
    CURRENT_DIR = Path(".")
    for _ in CURRENT_DIR.glob(glob):
        if _.is_file():
            yield _


def __md5lizeFileName(glob, do):
    """
    重命名当前目录下所有满足通配符的文件
    """
    files = __getFiles(glob)
    for file in files:
        __renameFile(file, do)
    with open("./change.log", "at", encoding="utf-8") as log:
        for line in __gPROCESSED:
            print(line, file=log)
            print(line)
    return 0


def main():
    import argparse
    parser = argparse.ArgumentParser(
        prog="md5filename",
        description="将当前目录下指定文件(们)重命名为其自身的 md5 值的 16 进制表示",
    )
    parser.add_argument("glob", help="通配符")
    parser.add_argument("--do", dest="do",
                        action="store_true", help="实际操作, 否则只预览效果")
    args = parser.parse_args()

    return __md5lizeFileName(args.glob, args.do)


if __name__ == "__main__":
    main()
