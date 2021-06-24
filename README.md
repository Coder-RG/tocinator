# TOCinator

[![MIT license](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) [![Py version](https://img.shields.io/pypi/pyversions/tocinator)](https://pypi.org/project/tocinator/1.0.0/) [![GitHub tag](https://img.shields.io/github/tag/Coder-RG/tocinator.svg)](https://GitHub.com/Coder-RG/tocinator/tags/)

This python module parses your Markdown file and generates a Table of Content(TOC)
for that file. It should be noted that this is still in development and may not
always function as expected.

**The TOC below was completely generated using this module.**

## Table of Content
1. [Features of this module](#features-of-this-module)
2. [Code Generated using tocinator](#code-generated-using-tocinator)
3. [Rendered Code](#rendered-code)
4. [Installation](#installation)
5. [How to use this module](#how-to-use-this-module)
   1. [What not to do](#what-not-to-do)
6. [General Layout](#general-layout)

## Features of this module
1. Generate Markdown-ready code.
2. Generated TOC has links to the actual headings and subheading. Which means you
can just paste the generated code in your README file and click on any of the links
to go to the desired heading.

## Code Generated using tocinator
Below is an example of TOC generated using tocinator.
The README used in the below snippets is from my [other][1] repository.
Do check it out if you code in C, it might be of your interest.
![Code](https://raw.githubusercontent.com/Coder-RG/tocinator/master/images/ss1.png)

## Rendered Code
![Render](https://raw.githubusercontent.com/Coder-RG/tocinator/master/images/ss2.png)

## Installation
**With pip**
```bash
$ pip3 install tocinator
```

**Without pip**

1. Clone this repository.
```bash
$ git clone git@github.com:Coder-RG/tocinator
```
2. Change directory to cloned repository.
```bash
$ cd tocinator
```
3. Run the file at command line:
```bash
$ python3 src/tocinator/tocinator.py <input-file> <output-file>
```

## How to use this module
1. Use `##` for headings
2. Use `###` for subheadings.

**Example 1: (installed with pip)**
```bash
$ python3 -m tocinator README.md OUT.md
```

**Example 2: (installed without pip)**
```bash
$ python3 src/tocinator/tocinator.py README.md OUT.md
```

If the .md file is in another folder, then use absolute path.
```bash
$ python3 src/tocinator/tocinator.py <path-to-folder>/README.md <path-to-folder>/TEST.md
```

**Example 3: (installed without pip)**
```bash
$ python3 src/tocinator/tocinator.py /home/username/project/README.md /home/username/project/OUT.md
```

### What not to do
1. `#` and `####` are not used in the parsing yet and therefore won't be
displayed in the TOC.
2. Only use alphanumeric for heading and subheadings. Otherwise, the links won't work.

## General Layout
![Code](https://raw.githubusercontent.com/Coder-RG/tocinator/master/images/ss4.png)

![Render](https://raw.githubusercontent.com/Coder-RG/tocinator/master/images/ss3.png)

Code is rendered using grip module. Do check out [grip][2] if you want to render your markdown files in your browser.

[1]: https://github.com/Coder-RG/compc
[2]: https://pypi.org/project/grip/
