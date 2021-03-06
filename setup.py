#!/usr/bin/env python

"""Setup script for the pyparsing module distribution."""

from setuptools import setup
from pyparsing import __version__ as pyparsing_version

modules = ["pyparsing",]

setup(# Distribution meta-data
    name = "pyparsing",
    version = pyparsing_version,
    description = "Python parsing module",
    author = "Paul McGuire",
    author_email = "ptmcg@users.sourceforge.net",
    url = "https://github.com/pyparsing/pyparsing/",
    download_url = "https://pypi.org/project/pyparsing/",
    license = "MIT License",
    py_modules = modules,
    python_requires='>=3.5',
    test_suite="unitTests.suite",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ]
    )
