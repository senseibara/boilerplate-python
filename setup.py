# -*- coding: utf-8 -*-

# Learn more: https://github.com/senseibara/boilerplate-python

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='boilerplate-python',
    version='0.1.0',
    description='Boilerplate python package',
    long_description=readme,
    author='Bara Ndiaye',
    author_email='ndiayebara93@gmail.com',
    url='https://github.com/senseibara/boilerplate-python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

