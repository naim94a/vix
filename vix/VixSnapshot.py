from .VixHandle import VixHandle
from .VixError import VixError
from vix import _backend
vix = _backend._vix
ffi = _backend._ffi


class VixSnapshot(VixHandle):
    def __init__(self, handle):
        super(VixSnapshot, self).__init__(handle)
        assert self.get_type() == VixHandle.VIX_HANDLETYPE_SNAPSHOT, 'Expected VixSnapshot handle.'

    def get_num_children(self):
        child_count = ffi.new('int*')
        error_code = vix.VixSnapshot_GetNumChildren(
            self._handle,
            child_count,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return int(child_count[0])

    def get_child(self, child_index):
        child_handle = ffi.new('VixHandle*')
        error_code = vix.VixSnapshot_GetChild(
            self._handle,
            child_index,
            child_handle,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return VixSnapshot(child_handle[0])

    def get_parent(self):
        parent_handle = ffi.new('VixHandle*')
        error_code = vix.VixSnapshot_GetParent(
            self._handle,
            parent_handle,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return VixSnapshot(parent_handle[0])
