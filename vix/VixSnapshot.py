from .VixHandle import VixHandle
from .VixError import VixError
from vix import _backend
vix = _backend._vix
ffi = _backend._ffi


class VixSnapshot(VixHandle):
    """Represents a VM's snapshot"""

    def __init__(self, handle):
        super(VixSnapshot, self).__init__(handle)
        assert self.get_type() == VixHandle.VIX_HANDLETYPE_SNAPSHOT, 'Expected VixSnapshot handle.'

    def get_num_children(self):
        """Gets the number of children the current snapshot has.

        :raises vix.VixError: On failure to get child count.
        """

        child_count = ffi.new('int*')
        error_code = vix.VixSnapshot_GetNumChildren(
            self._handle,
            child_count,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return int(child_count[0])

    def get_child(self, child_index):
        """Gets a child snapshot at the designated index

        :param int child_index: Index of child snapshot.

        :returns: Snapshot at specified index.
        :rtype: .VixSnapshot

        :raises vix.VixError: On failure to retrieve snapshot.
        """

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
        """Gets the parent of the current snapshot.

        :returns: Parent of current snapshot.
        :rtype: .VixSnapshot

        :raises vix.VixError: On failure to get snapshot.
        """
        
        parent_handle = ffi.new('VixHandle*')
        error_code = vix.VixSnapshot_GetParent(
            self._handle,
            parent_handle,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return VixSnapshot(parent_handle[0])
