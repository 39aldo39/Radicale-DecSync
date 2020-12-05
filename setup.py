#!/usr/bin/env python3

from setuptools import setup

setup(
    name="radicale_storage_decsync",
    version="1.2.0",
    author="Aldo Gunsing",
    author_email="dev@aldogunsing.nl",
    url="https://github.com/39aldo39/Radicale-DecSync",
    description="DecSync storage plugin for Radicale",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=["decsync", "radicale"],
    license="GPLv3+",
    packages=["radicale_storage_decsync"],
    install_requires=[
        "radicale>=3",
        "libdecsync>=1.3.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: End Users/Desktop"
    ]
)
