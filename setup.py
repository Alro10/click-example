import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

setup(name='library-example',
      version='0.1.0',
      include_package_data=True,
      install_requires=[
          'click==7.0'],
      entry_points={
          'console_scripts': [
              'bert=main:cli'
          ]
      }
      )
