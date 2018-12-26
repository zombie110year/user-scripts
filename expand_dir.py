import pathlib
import shutil
"""
将子文件夹中所有文件剪切到当前目录下
"""
gROOT = pathlib.Path(".").absolute()


def expandFiles(paths):
    for _ in paths:
        if _.is_file():
            try:
                shutil.move(str(_.absolute()), str(gROOT.absolute()))
            except shutil.Error:
                print("文件 {} 已存在".format(_.name))
        else:
            new_path = list(_.iterdir())
            expandFiles(new_path)


def removeDirs(paths):
    for _ in paths:
        if _.is_dir():
            try:
                _.rmdir()
            except OSError:
                removeDirs(list(_.iterdir()))


def main():
    dirs = [_ for _ in gROOT.iterdir() if _.is_dir()]
    expandFiles(dirs)
    removeDirs(dirs)


if __name__ == "__main__":
    main()
