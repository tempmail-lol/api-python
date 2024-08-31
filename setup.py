from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(name='tempmail-lol',
      version='3.0.0',
      description='A Python API for TempMail',
      author='Alexander Epolite, Alex Torres',
      author_email='contact@bananacrumbs.us',
      url='https://github.com/tempmail-lol/api-python',
      maintainer='Alexander Epolite',
      maintainer_email="contact@bananacrumbs.us",
      packages=find_packages(),
      install_requires=['requests'],
      keywords=['tempmail', 'api', 'lol', 'tempmail-lol', 'tempmail.lol', 'email', 'free'],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ]
    )
