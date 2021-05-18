import re
import sys

class FilePathMissing(Exception):
    __module__ = "tocinator"

def parser(file):
    title = r"^(#) (.*)$"
    chapter = r"^(##) (.*)$"
    subchapter = r"^(###) (.*)$"

    title_pattern = re.compile(title)
    chapter_pattern = re.compile(chapter)
    subchapter_pattern = re.compile(subchapter)

    dct = dict()
    with open(file, "r") as f:
        read_line = f.readline()
        # res1 = title_pattern.match(read_line)
        while read_line:
            res2 = chapter_pattern.match(read_line)
            res3 = subchapter_pattern.match(read_line)
            if res2:
                head = res2.group(2)
            if res2:
                dct[res2.group(2)] = list()
            elif res3:
                dct[head].append(res3.group(2))
            read_line = f.readline()
    return dct


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise FilePathMissing("File path missing as command line argument.")
    file = sys.argv[1]
    for x,y in parser(file).items():
        print(x, end=": ")
        print(*y, sep=", ")
