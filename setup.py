#!/usr/bin/env python
import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="try_pip",
    version="0.1.0",
    author="Matsunoshin",
    # author_email="",
    description="You can receive the message 'Hello!!!'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matsunoshin/try_pip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['try_pip = try_pip.try_pip:main']
    },
    python_requires='>=3.6',
)