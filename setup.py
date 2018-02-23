import os
import re
from setuptools import setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(BASE_DIR, 'README.rst'), 'rt') as fd:
    long_description = fd.read()

with open(os.path.join(BASE_DIR, 'vix', '__init__.py'), 'rt') as fd:
    version = re.search(r'__version__\W*=\W*(\'|")(.+?)(\'|")', fd.read()).group(2)

setup(
    name='vix',
    version=version,
    description='VMware VIX binding for Python (unofficial)',
    long_description=long_description,
    author='Naim A.',
    author_email='naim94a@gmail.com',
    url='https://github.com/naim94a/vix',
    packages=['vix'],
    package_dir={
        'vix': 'vix',
    },
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System :: Systems Administration',
    ],
    install_requires=[
        'cffi>=1.8.2',
        'six',
    ],
    keywords='vmware python api vix',
    project_urls={
        'Documentation': 'https://naim94a.github.io/vix',
        'Source': 'https://github.com/naim94a/vix',
        'Bugs & Features': 'https://github.com/naim94a/vix/issues'
    }
)
