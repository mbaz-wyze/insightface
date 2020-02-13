#!/usr/bin/env python
import os
import io
import re
import shutil
import sys
from setuptools import setup, find_packages

def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

VERSION = find_version('insightface', '__init__.py')

requirements = [
    'Cython==0.29.14',
    'scikit-learn==0.22.1',
    'scikit-image==0.16.2',
    'opencv-python==4.2.0.32',
]

setup(
    # Metadata
    name='wyzeinsightfaceruntime',
    version=VERSION,
    author='InsightFace Contributors',
    url='https://github.com/deepinsight/insightface',
    description='InsightFace Toolkit',
    long_description=long_description,
    license='Apache-2.0',
    # Package info
    packages=find_packages(exclude=('python-package')),
    zip_safe=True,
    include_package_data=True,
    install_requires=requirements,
)