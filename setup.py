import ast
import re
import os
import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

PACKAGE_NAME = "trypip"

with open(os.path.join(PACKAGE_NAME, '__init__.py')) as f:
    match = re.search(r'__version__\s+=\s+(.*)', f.read())
version = str(ast.literal_eval(match.group(1)))

setuptools.setup(
    name=PACKAGE_NAME,
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
    # entry_points = {
    #     'console_scripts': ['trypip = trypip.trypip:main']
    # },
    python_requires='>=3.6',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=3',
            'coverage',
            'tox',
        ],
    },
    entry_points='''
        [console_scripts]
        {app}={pkg}.cli:main
    '''.format(app=PACKAGE_NAME.replace('_', '-'), pkg=PACKAGE_NAME),
)