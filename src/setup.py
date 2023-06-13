# Copyright (c) 2022-2023 IO-Aero. All rights reserved. Use of this
# source code is governed by the IO-Aero License, that can
# be found in the LICENSE.md file.

"""The setuptools based setup module."""

import pathlib

from setuptools import find_packages
from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="sua",
    version="1.0.1",
    description="Flight Simulator",
    author="IO-Aero Team",
    author_email="info@io-aero.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: IO-Aero",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Library",
    ],
    keywords="Flight Simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    project_urls={
        "Bug Tracker": "https://github.com/io-aero/sua/issues",
        "Documentation": "https://io-aero.github.io/sua/",
        "Homepage": "https://github.com/io-aero/sua",
        "Release History": "https://io-aero.github.io/sua/release_history/",
        "Release Notes": "https://io-aero.github.io/sua/release_notes/",
        "Source": "https://github.com/io-aero/sua",
    },
    python_requires=">=3.10",
    url="https://github.com/io-aero/sua",
)
