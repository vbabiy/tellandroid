from setuptools import setup

from tellandroid import VERSION

setup(
  name='tellandroid',
  version=VERSION,
  packages=["tellandroid"],
  description = "A set of utilities to make it easier to work with the android emulator telnet protocol.",
  long_description=open('README.md').read(),
  author='Vitaly Babiy',
  author_email='vbabiy86@gmail.com',
  url='http://rainfalldesign.com/',
  scripts=['scripts/tellandroid',],
  install_requires=["docopts",]
)