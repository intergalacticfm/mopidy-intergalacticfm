from __future__ import unicode_literals

import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-IntergalacticFM',
    version=get_version('mopidy_intergalacticfm/__init__.py'),
    url='http://github.com/intergalacticfm/mopidy-intergalacticfm/',
    license='MIT License',
    author='Alexandre Petitjean',
    author_email='alpetitjean@gmail.com',
    description='Intergalactic FM extension for Mopidy',
    long_description="%s\n\n%s" % (
        open('README.rst').read(),
        open('CHANGES.rst').read()),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.1',
        'Pykka >= 1.1',
        'requests >= 2.0.0'
    ],
    entry_points={
        'mopidy.ext': [
            'intergalacticfm = mopidy_intergalacticfm:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
