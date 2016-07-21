#!/usr/bin/env python

import re
import sys

from setuptools import setup, find_packages


def version():
    with open('poppy_right_gripper/_version.py') as f:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read()).group(1)

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='poppy-right-gripper',
      version=version(),
      packages=find_packages(),

      install_requires=['pypot >= 2.2', 'poppy-creature'],

      setup_requires=['setuptools_git >= 0.3', ],

      include_package_data=True,

      zip_safe=False,

      author='Sebastien MICK',
      author_email='smick@ensc.fr',
      description=' Poppy Right Gripper Software Library',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      **extra
	  
	  )