#!/usr/bin/env python3
# pylint: disable=E501

from distutils.core import setup

webfaction_classifiers = [
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
]

long_description = """Command-line tool and library for the WebFaction API
https://docs.webfaction.com/xmlrpc-api/

Uses a Python XML-RPC instance to communicate with the Webfaction API.
Most API commands have been turned into Python commands.
"""

setup(
    name='webfaction',
    description='Webfaction Python API (supported Python 2 and 3)',
    long_description=long_description,
    url="https://github.com/bieli/Webfaction-Python-API",
    author="Marcin Bielak",
    author_email="marcin.bieli@gmail.com",
    license="MIT",
    packages=['webfaction'],
    platforms=["all"],
    version="1.1",
    scripts=['bin/webfaction'],
    install_requires=['configobj', ],
    classifiers=webfaction_classifiers,
)
