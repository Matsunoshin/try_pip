#!/usr/bin/env python
import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="trypip",
    version="0.1.0",
    author="Matsunoshin",
    # author_email="",
    description="You can receive the message 'Hello!!!'",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matsunoshin/trypip",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['trypip = trypip.trypip:main']
    },
    python_requires='>=3.6',
)