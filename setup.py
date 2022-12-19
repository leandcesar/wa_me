#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Leandro César Cassimiro",
    author_email="ccleandroc@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A modern, easy to use, feature-rich ready API wrapper for WhatsApp Business Cloud written in Python",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="whatsapp",
    name="whatsapp",
    packages=find_packages(include=["whatsapp", "whatsapp.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/leandcesar/whatsapp",
    version="0.1.0",
    zip_safe=False,
)
