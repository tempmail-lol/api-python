from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(name='tempmail-lol',
      version='2.0.0',
      description='A Python API for TempMail',
      author='Alex Torres, Alexander Epolite',
      author_email='cloudbotsedc@gmail.com',
      url='https://github.com/tempmail-lol/api-python',
      packages=find_packages(),
      install_requires=['requests'],
      keywords=['tempmail', 'api', 'lol', 'tempmail-lol', 'tempmail.lol', 'email', 'free'],
      classifiers=[
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ]
      )
