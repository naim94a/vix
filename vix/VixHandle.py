from __future__ import absolute_import

from vix import _backend, VixError, API_ENCODING
from .compat import _str, _bytes
vix = _backend._vix
ffi = _backend._ffi


class VixHandle(object):
    """Represents a handle of the VIX library.

    .. note:: Internal use.
    """

    VIX_INVALID_HANDLE = 0

    VIX_HANDLETYPE_NONE = 0
    VIX_HANDLETYPE_HOST = 2
    VIX_HANDLETYPE_VM = 3
    VIX_HANDLETYPE_NETWORK = 5
    VIX_HANDLETYPE_JOB = 6
    VIX_HANDLETYPE_SNAPSHOT = 7
    VIX_HANDLETYPE_PROPERTY_LIST = 9
    VIX_HANDLETYPE_METADATA_CONTAINER = 1

    VIX_PROPERTYTYPE_ANY = 0
    VIX_PROPERTYTYPE_INTEGER = 1
    VIX_PROPERTYTYPE_STRING = 2
    VIX_PROPERTYTYPE_BOOL = 3
    VIX_PROPERTYTYPE_HANDLE = 4
    VIX_PROPERTYTYPE_INT64 = 5
    VIX_PROPERTYTYPE_BLOB = 6

    VIX_PROPERTY_NONE = 0
    VIX_PROPERTY_META_DATA_CONTAINER = 2
    VIX_PROPERTY_HOST_HOSTTYPE = 50
    VIX_PROPERTY_HOST_API_VERSION = 51
    VIX_PROPERTY_HOST_SOFTWARE_VERSION = 52
    VIX_PROPERTY_VM_NUM_VCPUS = 101
    VIX_PROPERTY_VM_VMX_PATHNAME = 103
    VIX_PROPERTY_VM_VMTEAM_PATHNAME = 105
    VIX_PROPERTY_VM_MEMORY_SIZE = 106
    VIX_PROPERTY_VM_READ_ONLY = 107
    VIX_PROPERTY_VM_NAME = 108
    VIX_PROPERTY_VM_GUESTOS = 109
    VIX_PROPERTY_VM_IN_VMTEAM = 128
    VIX_PROPERTY_VM_POWER_STATE = 129
    VIX_PROPERTY_VM_TOOLS_STATE = 152
    VIX_PROPERTY_VM_IS_RUNNING = 196
    VIX_PROPERTY_VM_SUPPORTED_FEATURES = 197
    VIX_PROPERTY_VM_SSL_ERROR = 293
    VIX_PROPERTY_FOUND_ITEM_LOCATION = 4010
    VIX_PROPERTY_SNAPSHOT_DISPLAYNAME = 4200
    VIX_PROPERTY_SNAPSHOT_DESCRIPTION = 4201
    VIX_PROPERTY_SNAPSHOT_POWERSTATE = 4205
    VIX_PROPERTY_GUEST_SHAREDFOLDERS_SHARES_PATH = 4525
    VIX_PROPERTY_VM_ENCRYPTION_PASSWORD = 7001

    def __init__(self, handle):
        self._handle = handle

    def is_valid(self):
        """Checks that the handle is valid.

        :returns: True if handle is valid, otherwise False.
        :rtype: bool
        """

        return self._handle is not None and self._handle != self.VIX_INVALID_HANDLE

    def get_type(self):
        """Gets the handle's type.

        :returns: Type of handle from VIX_HANDLETYPE_*.
        :rtype: int
        """

        return vix.Vix_GetHandleType(self._handle)

    def add_ref(self):
        """Increases the handle's refcount."""

        vix.Vix_AddRefHandle(self._handle)

    def release(self):
        """Decreases refcount or Releases the handle."""

        vix.Vix_ReleaseHandle(self._handle)

    def get_properties(self, *args):
        c_args = list()
        ret_vals = list()

        for arg in args:
            prop_type = self.get_property_type(arg)

            alloc = None
            if prop_type in (self.VIX_PROPERTYTYPE_STRING, self.VIX_PROPERTYTYPE_BLOB):
                alloc = ffi.new('char**')
            elif prop_type == self.VIX_PROPERTYTYPE_INT64:
                alloc = ffi.new('int64*')
            else:
                alloc = ffi.new('int*')

            c_args.append(ffi.cast('VixPropertyID', arg))
            c_args.append(alloc)
            ret_vals.append((alloc, prop_type))

        print(ret_vals)
        c_args.append(ffi.cast('VixPropertyID', self.VIX_PROPERTY_NONE))

        error_code = vix.Vix_GetProperties(self._handle, *c_args)

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        results = list()
        for ret_val in ret_vals:
            val, val_type = ret_val

            if val_type in (self.VIX_PROPERTYTYPE_INT64, self.VIX_PROPERTYTYPE_INTEGER, self.VIX_PROPERTYTYPE_HANDLE):
                results.append(int(val[0]))
            elif val_type == self.VIX_PROPERTYTYPE_STRING:
                results.append(_str(ffi.string(val[0]), API_ENCODING))
            elif val_type == self.VIX_PROPERTYTYPE_BOOL:
                results.append(bool(val[0]))
            else:
                assert False, "Can't handle property type."

        return results[0] if len(results) == 1 else results


    def get_property_type(self, property_id):
        prop_type = ffi.new('VixPropertyType*')
        error_code = vix.Vix_GetPropertyType(
            self._handle,
            ffi.cast('VixPropertyID', property_id),
            prop_type
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return int(prop_type[0])
