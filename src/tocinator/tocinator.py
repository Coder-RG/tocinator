#!/usr/bin/env python3

import re
import sys

class FilePathMissing(Exception):
    """Custom Exception class for missing command line arguments"""
    __module__ = "tocinator"
    def __init__(self):
        self.message = ("\033[31mError:\033[0m Some command line arguments missing\n"
        "Usage: python3 -m tocinator <input-file> <output-file>")
        super().__init__(self.message)

class tocinator():
    """
    The main class that contains all the necessary functions
    for the functioning of this module. This will parse input
    Markdown(.md) file and generate an output Markdown file.
    You can just copy-paste the generated code and it should
    perform as expected.

    Usage: python3 -m tocinator <input-file> <output-file>

    """
    def __init__(self, ifile, ofile):
        self.ifile = ifile
        self.ofile = ofile

    def parse(self):
        chapter = r"^## (\[(.*?)\]|(.*))(.*)$"
        subchapter = r"^### (\[(.*?)\]|(.*))(.*)$"

        chapter_pattern = re.compile(chapter)
        subchapter_pattern = re.compile(subchapter)

        dct = dict()
        with open(self.ifile, "r") as f:
            read_line = f.readline()
            while read_line:
                res2 = chapter_pattern.match(read_line)
                res3 = subchapter_pattern.match(read_line)
                if res2:
                    head = res2.group(2) if res2.group(2) else res2.group(3)
                    dct[head] = list()
                elif res3:
                    subhead = res3.group(2) if res3.group(2) else res3.group(3)
                    dct[head].append(subhead)
                read_line = f.readline()
        return self.toc(dct)

    def toc(self, dct):
        if len(dct) == 0:
            return 1
        # for x,y in dct.items():
        #     print(x, end="\n\t")
        #     print(*y, sep="\n\t")
        with open(self.ofile, "w") as f:
            f.write("## Table of Content\n")
            i_out = 1
            for head,subhead in dct.items():
                ref = self.anchors(head)
                f.write("{} [{}](#{})\n".format(str(i_out)+".", head, ref))
                i_in = 1
                for sub in subhead:
                    subref = self.anchors(sub)
                    f.write("   {} [{}](#{})\n".format(str(i_in)+".", sub, subref))
                    i_in += 1
                i_out += 1
        return 0

    def anchors(self, string):
        p = r"\W+"
        result = re.split(p, string)
        for index,i in enumerate(result):
            if i == '':
                del result[index]
            else:
                result[index] = i.lower()
        return '-'.join(result)

def main():
    try:
        if len(sys.argv) < 3:
            raise FilePathMissing()
    except FilePathMissing as e:
        print(e.message)
        sys.exit(1)
    infile = sys.argv[1]
    outfile = sys.argv[2]
    script = tocinator(infile, outfile)
    sys.exit(script.parse())

if __name__ == "__main__":
    main()
