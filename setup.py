from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pydocless',
    version='0.0.2',
    author='PentairIoT',
    author_email='pentairiot@gmail.com',
    description='Python library for creating markdown documentation from python docstrings',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pentairiot/pydocless',
    packages=["."],
    scripts=["pydocless"],
    install_requires=[],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
