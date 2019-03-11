#!/usr/bin/env python

from setuptools import setup

setup(
    name='refract',
    version='0.3.1',
    description='A Python library for interacting with Refract.',
    url='https://github.com/kylef/refract.py',
    packages=['refract', 'refract.elements', 'refract.contrib'],
    author='Kyle Fuller',
    author_email='kyle@fuller.li',
    license='BSD',
    classifiers=(
      'Development Status :: 5 - Production/Stable',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'License :: OSI Approved :: BSD License',
    )
)
