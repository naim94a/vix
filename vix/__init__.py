"""
    vix
    ---

    A python binding for VMWare's VIX library.

    :copyright: (c) 2016 by Naim A.
    :license: GPLv3, see LICENSE for more details.
"""

__version__ = "1.0.8"

from .VixBackend import VixBackend as _VixBackend
_backend = _VixBackend()
vix = _backend._vix
ffi = _backend._ffi

# should be ascii for windows, utf8 for linux
API_ENCODING = 'utf-8'

from .VixError import VixError
from .VixHost import VixHost
from .VixSnapshot import VixSnapshot
from .VixVM import VixVM
