#!/bin/env python
# pyzmail/setup.py
# (c) alain.spineux@gmail.com
# http://www.magiksys.net/pyzmail

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

basename='pyzmail'
# retrieve $version
version=''
for line in open('pyzmail/version.py'):
    if line.startswith("__version__ ="):
        version=line[15:].rstrip()[:-1]
        break

if not version:
    print('!!!!!!!!!!!!!!!!!!!!!! VERSION NOT FOUND !!!!!!!!!!!!!!!!!!!!!!!!!')
    sys.exit(1)

print('VERSION', version)

extra_options = {}
doc_dir='share/doc/%s-%s' % (basename, version)

cmdclass = {}
data_files=[ ]

data_files.append( (doc_dir, [ 'README.md', 'Changelog.txt', 'LICENSE.txt']) )

setup(
      version=version,
#      maintainer = 'email', #
      test_suite = 'pyzmail.tests',
      data_files=data_files,
      cmdclass = cmdclass,
      **extra_options)

if 'sdist' in sys.argv and 'upload' in sys.argv:
    print("After an upload, don't forget to change 'maintainer' to 'email' to be hight in pypi index")
