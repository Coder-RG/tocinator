from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='tocinator',
    version='1.0.1',
    url="https://github.com/Coder-RG/tocinator",
    author="Rishabh Goel",
    author_email="rgoel1999@gmail.com",
    description='Generate a Table of Content from Markdown files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    pymodules=["tocinator.py"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
