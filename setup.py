#!/usr/bin/env python
# encoding: utf-8

# The MIT License (MIT)

# Copyright (c) 2015-2018 CNRS

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# AUTHORS
# Herve BREDIN - http://herve.niderb.fr


from setuptools import setup, find_packages
import versioneer

setup(

    # package
    namespace_packages=['pyannote'],
    packages=find_packages(),
    scripts=[
        "scripts/pyannote-structure.py",
        "scripts/pyannote-face.py"
    ],
    install_requires=[
        'pyannote.core >= 2.0',
        'pyannote.algorithms >= 0.8',
        'sortedcollections >= 1.0.1',
        'numpy >= 1.8',
        'docopt >= 0.6.2',
        'tqdm >= 4.23.2',
        'dlib',
        'opencv-python >= 3.4.1.15',
        'munkres >= 1.0.7',
        'moviepy == 0.2.3.4',
        'pandas >= 0.20.3',        
        'imageio'
    ],

    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    # PyPI
    name='pyannote.video',
    description=('Video processing (including face detection, tracking, and clustering)'),
    author='Herve Bredin',
    author_email='bredin@limsi.fr',
    url='http://herve.niderb.fr/',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering"
    ],
)
