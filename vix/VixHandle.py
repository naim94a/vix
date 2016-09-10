from vix import _backend
vix = _backend._vix
ffi = _backend._ffi


class VixHandle(object):
    VIX_INVALID_HANDLE = 0

    VIX_HANDLETYPE_NONE = 0
    VIX_HANDLETYPE_HOST = 2
    VIX_HANDLETYPE_VM = 3
    VIX_HANDLETYPE_NETWORK = 5
    VIX_HANDLETYPE_JOB = 6
    VIX_HANDLETYPE_SNAPSHOT = 7
    VIX_HANDLETYPE_PROPERTY_LIST = 9
    VIX_HANDLETYPE_METADATA_CONTAINER = 1

    def __init__(self, handle):
        self._handle = handle

    def is_valid(self):
        return self._handle is not None and self._handle != self.VIX_INVALID_HANDLE

    def get_type(self):
        return vix.Vix_GetHandleType(self._handle)

    def add_ref(self):
        vix.Vix_AddRefHandle(self._handle)

    def release(self):
        vix.Vix_ReleaseHandle(self._handle)
