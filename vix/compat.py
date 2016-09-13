# This file is for backward compatibility with Python2.
# If you are using Python2, please do upgrade to Python3 :)
import sys


if sys.version_info.major < 3:
	def _bytes(data, encoding=None):
		if encoding:
			return str(data).encode(encoding)
		else:
			return str(data)

	def _str(data, encoding):
		return str(data).decode(encoding)

else:
	_bytes = bytes
	_str = str
