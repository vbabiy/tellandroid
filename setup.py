from setuptools import setup

from tellandroid import VERSION

setup(
  name='tellandroid',
  version=VERSION,
  packages=["tellandroid"],
  description=open('README.md').read(),
  author='Vitaly Babiy',
  author_email='vbabiy86@gmail.com',
  url='http://rainfalldesign.com/',
  scripts=['scripts/tellandroid',],
  install_requires=["docopts",]
)