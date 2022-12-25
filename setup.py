#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "dacite==1.6.0",
    "requests==2.28.1",
]

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
    name="wa_me",
    packages=find_packages(include=["wa_me", "wa_me.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/leandcesar/wa_me",
    version="0.1.0",
    zip_safe=False,
)
