# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pymfx4',
    version='0.1.0',
    description='Control of MFX_4 Series Devices',
    long_description=readme,
    author='Alexander Angold',
    author_email='alexander@angold.eu',
    url='https://www.m-f.tech/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
          'serial>=0.0.97',
          'jsonpickle'
      ],
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
)
