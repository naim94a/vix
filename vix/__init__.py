"""
	vix
	---

	A python binding for VMWare's VIX library.

	:copyright: (c) 2016 by Naim A.
	:license: GPLv3, see LICENSE for more details.
"""

from .VixBackend import VixBackend
_backend = VixBackend()
vix = _backend._vix
ffi = _backend._ffi

# should be ascii for windows, utf8 for linux
API_ENCODING = 'utf-8'

from .VixError import VixError
from .VixHost import VixHost

__all__ = ('VixHost', 'VixSnapshot', 'VixError')
