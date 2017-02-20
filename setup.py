from setuptools import setup
from vix import __version__

setup(
    name='vix',
    version=__version__,
    description='VMware VIX binding for Python (unofficial)',
    author='Naim A.',
    author_email='naim94a@gmail.com',
    url='https://github.com/naim94a/vix',
    packages=['vix'],
    package_dir={
        'vix': 'vix',
    },
    license='GPLv3',
    classifiers=[
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
    ]
)
