#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

path = os.path.abspath(os.path.dirname(__file__))
try:
    LONG_DESCRIPTION = open(os.path.join(path, 'README.rst')).read()
except IOError:
    LONG_DESCRIPTION = ''

setup(
    name              = "setor",
    packages          = ['setor'],
    version           = "1.0",
    platforms         = ['Linux'],
    url               = 'https://github.com/agusmakmun/setor/',
    download_url      = 'https://github.com/agusmakmun/setor/tarball/v1.0',
    description       = "SETOR (SEO TOR) - Bot TOR to visit the webpages with unique IP's and random times.",
    long_description  = LONG_DESCRIPTION,
    license           = 'MIT',
    author            = 'Agus Makmun (Summon Agus)',
    author_email      = 'ags@dracos-linux.id',
    keywords          = ['SETOR', 'SEO TOR', 'Bot TOR'],
    entry_points={
        'console_scripts': ['setor=setor.setor:main',],
    },
    classifiers       = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Networking'
    ],
)