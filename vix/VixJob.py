from .VixHandle import VixHandle
from .VixError import VixError
from vix import _backend, API_ENCODING
import datetime

vix = _backend._vix
ffi = _backend._ffi

class VixJob(VixHandle):
    """Represnts a VIX Job handle.

    .. note:: Internal use.
    """

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
    VIX_PROPERTY_JOB_RESULT_ERROR_CODE = 3000
    VIX_PROPERTY_JOB_RESULT_VM_IN_GROUP = 3001
    VIX_PROPERTY_JOB_RESULT_USER_MESSAGE = 3002
    VIX_PROPERTY_JOB_RESULT_EXIT_CODE = 3004
    VIX_PROPERTY_JOB_RESULT_COMMAND_OUTPUT = 3005
    VIX_PROPERTY_JOB_RESULT_HANDLE = 3010
    VIX_PROPERTY_JOB_RESULT_GUEST_OBJECT_EXISTS = 3011
    VIX_PROPERTY_JOB_RESULT_GUEST_PROGRAM_ELAPSED_TIME = 3017
    VIX_PROPERTY_JOB_RESULT_GUEST_PROGRAM_EXIT_CODE = 3018
    VIX_PROPERTY_JOB_RESULT_ITEM_NAME = 3035
    VIX_PROPERTY_JOB_RESULT_FOUND_ITEM_DESCRIPTION = 3036
    VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_COUNT = 3046
    VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_HOST = 3048
    VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_FLAGS = 3049
    VIX_PROPERTY_JOB_RESULT_PROCESS_ID = 3051
    VIX_PROPERTY_JOB_RESULT_PROCESS_OWNER = 3052
    VIX_PROPERTY_JOB_RESULT_PROCESS_COMMAND = 3053
    VIX_PROPERTY_JOB_RESULT_FILE_FLAGS = 3054
    VIX_PROPERTY_JOB_RESULT_PROCESS_START_TIME = 3055
    VIX_PROPERTY_JOB_RESULT_VM_VARIABLE_STRING = 3056
    VIX_PROPERTY_JOB_RESULT_PROCESS_BEING_DEBUGGED = 3057
    VIX_PROPERTY_JOB_RESULT_SCREEN_IMAGE_SIZE = 3058
    VIX_PROPERTY_JOB_RESULT_SCREEN_IMAGE_DATA = 3059
    VIX_PROPERTY_JOB_RESULT_FILE_SIZE = 3061
    VIX_PROPERTY_JOB_RESULT_FILE_MOD_TIME = 3062
    VIX_PROPERTY_JOB_RESULT_EXTRA_ERROR_INFO = 3084
    VIX_PROPERTY_FOUND_ITEM_LOCATION = 4010
    VIX_PROPERTY_SNAPSHOT_DISPLAYNAME = 4200
    VIX_PROPERTY_SNAPSHOT_DESCRIPTION = 4201
    VIX_PROPERTY_SNAPSHOT_POWERSTATE = 4205
    VIX_PROPERTY_GUEST_SHAREDFOLDERS_SHARES_PATH = 4525
    VIX_PROPERTY_VM_ENCRYPTION_PASSWORD = 7001

    VIX_FILE_ATTRIBUTES_DIRECTORY = 0x0001
    VIX_FILE_ATTRIBUTES_SYMLINK = 0x0002

    STR_RESULT_TYPES = (
        VIX_PROPERTY_JOB_RESULT_ITEM_NAME,
        VIX_PROPERTY_JOB_RESULT_VM_VARIABLE_STRING,
        VIX_PROPERTY_JOB_RESULT_COMMAND_OUTPUT,
        VIX_PROPERTY_JOB_RESULT_PROCESS_OWNER,
        VIX_PROPERTY_JOB_RESULT_PROCESS_COMMAND,
    )

    def __init__(self, handle):
        super(VixJob, self).__init__(handle)
        assert self.get_type() == VixHandle.VIX_HANDLETYPE_JOB, 'Expected VixJob handle.'

    def wait(self, *args):
        """Waits for the job to complete and gets requested results.

        :param \*args: A list of properties to retreive (VIX_PROPERTY_JOB_RESULT_*).

        :returns: A tuple of results if more than one object was requested.

        :raises vix.VixError: If job failed.
        """

        c_args = list()
        ret_data = list()

        for arg in args:
            c_args.append(ffi.cast('VixPropertyType', arg))

            # TODO: Check the arg type and allocate accordingly...
            alloc = None
            if arg in self.STR_RESULT_TYPES:
                alloc = ffi.new('char**')
            else:
                alloc = ffi.new('int*')
            ret_data.append(alloc)
            c_args.append(alloc)

        c_args.append(ffi.cast('VixPropertyType', self.VIX_PROPERTY_NONE))

        error_code = vix.VixJob_Wait(self._handle, *c_args)
        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        # deref data...
        result = list()
        for i in range(len(args)):
            if args[i] == self.VIX_PROPERTY_NONE:
                break
            val = ret_data[i]
            if args[i] in self.STR_RESULT_TYPES:
                result.append(str(ffi.string(val[0]), API_ENCODING))
                vix.Vix_FreeBuffer(val[0])
            else:
                result.append(val[0])

        return result[0] if len(result) == 1 else result

    def is_done(self):
        """Checks if the job completed.

        :returns: True if job completed, otherwise False.
        :rtype: bool

        :raises vix.VixError: If failed to get job state.
        """

        result = ffi.new('Bool*')
        error_code = vix.VixJob_CheckCompletion(self._handle, result)
        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return result[0]

    def get_error(self):
        """Gets an exception object.

        :returns: Exception object of job. The error may be VixError(VIX_OK).
        :rtype: .VixError
        """

        error_code = vix.VixJob_GetError(self._handle)
        return VixError(error_code)

    def _get_num_properties(self, property_id):
        count = vix.VixJob_GetNumProperties(
            self._handle,
            property_id,
        )
        return int(count)

    def _get_nth_properties(self, index, *args):

        c_args = list()
        for arg in args:
            alloc = None
            if arg in self.STR_RESULT_TYPES:
                alloc = ffi.new('char**')
            elif arg in (self.VIX_PROPERTY_JOB_RESULT_PROCESS_ID, self.VIX_PROPERTY_JOB_RESULT_FILE_SIZE, self.VIX_PROPERTY_JOB_RESULT_FILE_MOD_TIME):
                alloc = ffi.new('uint64*')
            else:
                alloc = ffi.new('int*')
            c_args.append(ffi.cast('VixPropertyType', arg))
            c_args.append(alloc)

        c_args.append(ffi.cast('VixPropertyType', self.VIX_PROPERTY_NONE))

        error_code = vix.VixJob_GetNthProperties(
            self._handle,
            index,
            *c_args,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        result = list()

        for i in range(len(args)):
            prop_id = int(c_args[i * 2])
            prop_val = c_args[(i * 2) + 1]

            value = None
            if prop_id in self.STR_RESULT_TYPES:
                value = str(ffi.string(prop_val[0]), API_ENCODING)
                vix.Vix_FreeBuffer(prop_val[0])
            elif prop_id == self.VIX_PROPERTY_JOB_RESULT_PROCESS_BEING_DEBUGGED:
                value = bool(ffi.cast('Bool', prop_val[0]))
            elif prop_id in (self.VIX_PROPERTY_JOB_RESULT_PROCESS_START_TIME, self.VIX_PROPERTY_JOB_RESULT_FILE_MOD_TIME):
                value = datetime.datetime.fromtimestamp(int(ffi.cast('int', prop_val[0])))
            else:
                value = int(ffi.cast('int', prop_val[0]))

            result.append(value)

        return tuple(result)

    def get_properties(self, *args):
        num = self._get_num_properties(args[0])
        result = list()

        for i in range(num):
            result.append(self._get_nth_properties(i, *args))

        return result

    def __del__(self):
        self.release()
