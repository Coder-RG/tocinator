#!/usr/bin/env python3

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

def toc(dct):
    if len(dct) == 0:
        return -1
    else:
        for x,y in dct.items():
            print(x, end="\n\t")
            print(*y, sep="\n\t")
    with open("TEST2.md", "w") as f:
        f.write("## Table of Content\n")
        i_out = 1
        for head,subhead in dct.items():
            f.write("{} [{}](README.md)\n".format(str(i_out)+".", head))
            i_in = 1
            for sub in subhead:
                f.write("   {} [{}](README.md)\n".format(str(i_in)+".", sub))
                i_in += 1
            f.write("\n")
            i_out += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise FilePathMissing("File path missing as command line argument.")
    file = sys.argv[1]
    sys.exit(toc(parser(file)))
