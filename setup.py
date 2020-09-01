from setuptools import setup


NAME = 'graftr'
VERSION = '0.1.1'
DESCRIPTION = 'graftr: an interactive shell to view and edit PyTorch checkpoints.'
AUTHOR = 'LMNT, Inc.'
AUTHOR_EMAIL = 'graftr@lmnt.com'
URL = 'https://graftr.lmnt.com'
LICENSE = 'Apache 2.0'
KEYWORDS = []  # TODO
CLASSIFIERS = [
  'Development Status :: 4 - Beta',
  'Environment :: Console',
  'Intended Audience :: Developers',
  'Intended Audience :: Education',
  'Intended Audience :: Science/Research',
  'License :: OSI Approved :: Apache Software License',
  'Programming Language :: Python :: 3.6',
  'Programming Language :: Python :: 3.7',
  'Programming Language :: Python :: 3.8',
  'Topic :: Scientific/Engineering :: Artificial Intelligence',
  'Topic :: Scientific/Engineering :: Mathematics',
  'Topic :: Software Development',
]

setup(name= NAME,
    scripts=['graftr'],
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS)
