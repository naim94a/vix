from distutils.core import setup

setup(
	name='vix',
	version='1.0.0',
	description='VIX binding for Python',
	author='Naim A.',
	author_email='naim94a@gmail.com',
	url='https://github.com/naim94a/vix',
	packages=['vix'],
	package_dir={
		'vix': 'vix',
	},
	license='GPLv3',
	classifiers=[
		'Development Status :: 4 - Beta', 
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
	]
)
