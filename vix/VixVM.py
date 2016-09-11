from .VixError import VixError
from .VixHandle import VixHandle
from .VixSnapshot import VixSnapshot
from .VixJob import VixJob
from vix import _backend, API_ENCODING
vix = _backend._vix
ffi = _backend._ffi


def _blocking_job(f):
    def decorator(*args, **kwargs):
        job = f(*args, **kwargs)
        VixJob(job).wait()

    # allows sphinx to generate docs normally...
    decorator.__doc__ = f.__doc__

    return decorator


class VixVM(VixHandle):
    """Represents a guest VM."""
    
    VIX_VMDELETE_DISK_FILES = 0x0002

    VIX_POWERSTATE_POWERING_OFF = 0x0001
    VIX_POWERSTATE_POWERED_OFF = 0x0002
    VIX_POWERSTATE_POWERING_ON = 0x0004
    VIX_POWERSTATE_POWERED_ON = 0x0008
    VIX_POWERSTATE_SUSPENDING = 0x0010
    VIX_POWERSTATE_SUSPENDED = 0x0020
    VIX_POWERSTATE_TOOLS_RUNNING = 0x0040
    VIX_POWERSTATE_RESETTING = 0x0080
    VIX_POWERSTATE_BLOCKED_ON_MSG = 0x0100
    VIX_POWERSTATE_PAUSED = 0x0200
    VIX_POWERSTATE_RESUMING = 0x0800

    VIX_TOOLSSTATE_UNKNOWN = 0x0001
    VIX_TOOLSSTATE_RUNNING = 0x0002
    VIX_TOOLSSTATE_NOT_INSTALLED = 0x0004

    VIX_VM_SUPPORT_SHARED_FOLDERS = 0x0001
    VIX_VM_SUPPORT_MULTIPLE_SNAPSHOTS = 0x0002
    VIX_VM_SUPPORT_TOOLS_INSTALL = 0x0004
    VIX_VM_SUPPORT_HARDWARE_UPGRADE = 0x0008

    VIX_LOGIN_IN_GUEST_REQUIRE_INTERACTIVE_ENVIRONMENT = 0x08

    VIX_RUNPROGRAM_RETURN_IMMEDIATELY = 0x0001
    VIX_RUNPROGRAM_ACTIVATE_WINDOW = 0x0002

    VIX_VM_GUEST_VARIABLE = 1
    VIX_VM_CONFIG_RUNTIME_ONLY = 2
    VIX_GUEST_ENVIRONMENT_VARIABLE = 3

    VIX_SNAPSHOT_REMOVE_CHILDREN = 0x0001

    VIX_SNAPSHOT_INCLUDE_MEMORY = 0x0002

    VIX_SHAREDFOLDER_WRITE_ACCESS = 0x04

    VIX_CAPTURESCREENFORMAT_PNG = 0x01
    VIX_CAPTURESCREENFORMAT_PNG_NOCOMPRESS = 0x02

    VIX_CLONETYPE_FULL = 0
    VIX_CLONETYPE_LINKED = 1

    VIX_INSTALLTOOLS_MOUNT_TOOLS_INSTALLER = 0x00
    VIX_INSTALLTOOLS_AUTO_UPGRADE = 0x01
    VIX_INSTALLTOOLS_RETURN_IMMEDIATELY = 0x02

    VIX_VMPOWEROP_NORMAL = 0
    VIX_VMPOWEROP_FROM_GUEST = 0x0004
    VIX_VMPOWEROP_SUPPRESS_SNAPSHOT_POWERON = 0x0080
    VIX_VMPOWEROP_LAUNCH_GUI = 0x0200
    VIX_VMPOWEROP_START_VM_PAUSED = 0x1000

    def __init__(self, handle):
        super(VixVM, self).__init__(handle)

        assert self.get_type() == VixHandle.VIX_HANDLETYPE_VM, 'Expected VixVM handle.'

    # Power
    @_blocking_job
    def pause(self):
        """Pauses the Virtual machine.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_Pause(
            self._handle,
            ffi.cast('int', 0),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def power_off(self, options=VIX_VMPOWEROP_NORMAL):
        """Powers off a VM.

        :param int options: should be VIX_VMPOWEROP_NORMAL or VIX_VMPOWEROP_FROM_GUEST.

        :raises vix.VixError: On failure to power off VM.
        """

        return vix.VixVM_PowerOff(
            self._handle,
            ffi.cast('VixVMPowerOpOptions', options),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def power_on(self, options=VIX_VMPOWEROP_NORMAL):
        """Powers on a VM.

        :param int options: Should be VIX_VMPOWEROP_NORMAL or VIX_VMPOWEROP_LAUNCH_GUI.

        :raises vix.VixError: On failure to power on VM.
        """

        return vix.VixVM_PowerOn(
            self._handle,
            ffi.cast('VixVMPowerOpOptions', options),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def reset(self, options=VIX_VMPOWEROP_NORMAL):
        """Resets a virtual machine.

        :param int options: Should be set to VIX_VMPOWEROP_NORMAL or VIX_VMPOWEROP_FROM_GUEST.
        :raises vix.VixError: On failure to reset VM.
        """

        return vix.VixVM_Reset(
            self._handle,
            ffi.cast('VixVMPowerOpOptions', options),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def suspend(self):
        """Suspends a virtual machine.

        :raises vix.VixError: On failure to suspend VM.
        """

        return vix.VixVM_Suspend(
            self._handle,
            ffi.cast('VixVMPowerOpOptions', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def unpause(self):
        """Resumes execution of a paused virtual machine.

        :raises vix.VixError: On failure to unpause VM.

        .. note:: This method is not supported by all Vmware products.
        """

        return vix.VixVM_Unpause(
            self._handle,
            ffi.cast('int', 0),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    # Snapshots
    def clone(self, dest_vmx, snapshot=None, clone_type=VIX_CLONETYPE_LINKED):
        """Clones the VM to a specified location.

        :param str dest_vms: The clone will be stored here.
        :param .VixSnapshot snapshot: Optional snapshot as the state of the clone.
        :param int clone_type: Must be VIX_CLONETYPE_FULL or VIX_CLONETYPE_LINKED.

        :returns: Instance of the cloned VM.
        :rtype: .VixVM

        :raises vix.VixError: On failure to clone.

        .. note:: This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixVM_Clone(
            self._handle,
            ffi.cast('VixHandle', snapshot._handle if snapshot else 0),
            ffi.cast('VixCloneType', clone_type),
            ffi.new('char[]', bytes(dest_vms, API_ENCODING)),
            ffi.cast('VixCloneOptions', 0),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))

        return VixVM(job.wait(VixJob.VIX_PROPERTY_JOB_RESULT_HANDLE))

    def create_snapshot(self, name=None, description=None, options=VIX_SNAPSHOT_INCLUDE_MEMORY):
        """Create a VM snapshot.

        :param str name: Name of snapshot.
        :param str description: Snapshot description.
        :param int options: 0 or VIX_SNAPSHOT_INCLUDE_MEMORY to include RAM.

        :returns: Instance of the created snapshot
        :rtype: .VixSnapshot

        :raises vix.VixError: On failure to create snapshot.

        .. note:: This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixVM_CreateSnapshot(
            self._handle,
            ffi.new('char[]', bytes(name, API_ENCODING)) if name else ffi.cast('char*', 0),
            ffi.new('char[]', bytes(description, API_ENCODING)) if description else  ffi.cast('char*', 0),
            ffi.cast('int', options),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))

        return VixSnapshot(job.wait(VixJob.VIX_PROPERTY_JOB_RESULT_HANDLE))

    def snapshot_get_current(self):
        """Gets the VMs current active snapshot.

        :returns: The currently active snapshot
        :rtype: .VixSnapshot

        :raises vix.VixError: On failure to get the current snapshot.

        .. note:: This method is not supported by all VMware products.
        """

        snapshot_handle = ffi.new('VixHandle*')
        error_code = vix.VixVM_GetCurrentSnapshot(
            self._handle,
            snapshot_handle,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return VixSnapshot(snapshot_handle[0])

    def snapshot_get_named(self, name):
        """Gets a snapshot matching the given name.

        :param str name: Name of the snapshot to get.
        
        :returns: Instance of requests snapshot.
        :rtype: .VixSnapshot

        :raises vix.VixError: If failed to retreive desired snapshot.

        .. note:: This method is not supported by all VMware products.
        """

        snapshot_handle = ffi.new('VixHandle*')
        error_code = vix.VixVM_GetNamedSnapshot(
            self._handle,
            ffi.new('char[]', bytes(name, API_ENCODING)),
            snapshot_handle,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return VixSnapshot(snapshot_handle[0])

    def snapshots_get_root_count(self):
        """Gets the count of root snapshots the VM owns.

        :returns: Count of VM's root snapshots.
        :rtype: int

        :raises vix.VixError: If failed to retrive root snapshot count.

        .. note:: This method is not supported by all VMware products.
        """

        result = ffi.new('int*')
        error_code = vix.VixVM_GetNumRootSnapshots(
            self._handle,
            result,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return result[0]

    def snapshot_get_root(self, index=0):
        """Gets the specified VM Snapshot.

        :param int index: zero based snapshot index.

        :returns: Root snapshot at specified index.
        :rtype: .VixSnapshot

        :raises vix.VixError: If failed to get specified too snapshot.

        .. note:: This methoid is not supported in all VMware products.
        """

        snapshot_handle = ffi.new('VixHandle*')
        error_code = vix.VixVM_GetRootSnapshot(
            self._handle,
            ffi.cast('int', index),
            snapshot_handle,
        )

        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

        return VixSnapshot(snapshot_handle[0])

    @_blocking_job
    def snapshot_revert(self, snapshot, options=0):
        """Revet VM state to specified snapshot.

        :param .VixSnapshot snapshot: The snapshot to revert to.
        :param int options: Any of VIX_VMPOWEROP_*, VIX_VMPOWEROP_SUPPRESS_SNAPSHOT_POWERON is mutually exclusive.

        :raises vix.VixError: If failed to revert VM to snapshot.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_RevertToSnapshot(
            self._handle,
            snapshot._handle,
            ffi.cast('int', options),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def snapshot_remove(self, snapshot, options=0):
        """Removed specified snapshot from VM.

        :param .VixSnapshot snapshot: The snapshot to remove.
        :param int options: 0 or VIX_SNAPSHOT_REMOVE_CHILDREN to remove child snapshots too.

        :raises vix.VixError: If failed to remove specified snapshot.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_RemoveSnapshot(
            self._handle,
            snapshot._handle,
            ffi.cast('int', options),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    # Guest & Host file mgmt.
    @_blocking_job
    def copy_guest_to_host(self, guest_path, host_path):
        """Copies a file or directory from the VM to host.

        :param str guest_path: Path to copy from on guest.
        :param str host_path: Path to copy to on host.

        :raises vix.VixError: If copy failed.
        """

        return vix.VixVM_CopyFileFromGuestToHost(
            self._handle,
            ffi.new('char[]', bytes(guest_path, API_ENCODING)),
            ffi.new('char[]', bytes(host_path, API_ENCODING)),
            ffi.cast('int', 0),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def copy_host_to_guest(self, host_path, guest_path):
        """Copies a file or directory from host to VM.

        :param str host_path: Path to copy from on host.
        :param str guest_path: Path to copy to on VM.

        :raises vix.VixError: If failed to copy.
        """

        return vix.VixVM_CopyFileFromHostToGuest(
            self._handle,
            ffi.new('char[]', bytes(host_path, API_ENCODING)),
            ffi.new('char[]', bytes(guest_path, API_ENCODING)),
            ffi.cast('int', 0),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def create_directory(self, path):
        """Creates a directory in the guest VM.

        :param str path: Path to create in guest.

        :raises vix.VixError: On failure to create directory.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_CreateDirectoryInGuest(
            self._handle,
            ffi.new('char[]', bytes(path, API_ENCODING)),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    def create_temp(self):
        """Creates a temporary file in guest.

        :returns: Temporary file name.
        :rtype: str

        :raises vix.VixError: On failure to create temporary file.

        .. note:: This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixVM_CreateTempFileInGuest(
            self._handle,
            ffi.cast('int', 0),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))

        return job.wait(VixJob.VIX_PROPERTY_JOB_RESULT_ITEM_NAME)

    @_blocking_job
    def file_rename(self, old_name, new_name):
        """Renames a file or directory in guest.

        :param str old_name: Name of file to rename.
        :param str new_name: The new name to give the file.

        :raises vix.VixError: On failure to rename.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_RenameFileInGuest(
            self._handle,
            ffi.new('char[]', bytes(old_name, API_ENCODING)),
            ffi.new('char[]', bytes(new_name, API_ENCODING)),
            ffi.cast('int', 0),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def dir_delete(self, path):
        """Deletes a directory in guest VM.

        :param str path: Path of directory to delete.

        :raises vix.VixError: If failed to delete directory.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_DeleteDirectoryInGuest(
            self._handle,
            ffi.new('char[]', bytes(path, API_ENCODING)),
            ffi.cast('int', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def file_delete(self, path):
        """Deletes a file in guest VM.

        :param str path: Path of file to delete.

        :raises vix.VixError: If failed to delete directory.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_DeleteFileInGuest(
            self._handle,
            ffi.new('char[]', bytes(path, API_ENCODING)),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    def dir_exists(self, path):
        """Checks if a directory exists in guest VM.

        :param str path: Path to check if exists.

        :returns: True if directory exists, othwerwise False.
        :rtype: bool

        :raises vix.VixError: If failed to check.

        .. note:: This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixVM_DirectoryExistsInGuest(
            self._handle,
            ffi.new('char[]', bytes(path, API_ENCODING)),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))

        return bool(job.wait(VixJob.VIX_PROPERTY_JOB_RESULT_GUEST_OBJECT_EXISTS))

    def file_exists(self, path):
        """Checks if a file exists in guest VM.

        :param str path: File to check.

        :returns: True if file exists, otherwise False.
        :rtype: bool

        :raises vix.VixError: If failed to check file existance.

        .. note:: This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixVM_FileExistsInGuest(
            self._handle,
            ffi.new('char[]', bytes(path, API_ENCODING)),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))

        return bool(job.wait(VixJob.VIX_PROPERTY_JOB_RESULT_GUEST_OBJECT_EXISTS))

    def get_file_info(self):
        raise NotImplemented()

    def dir_list(self):
        raise NotImplemented()

    # Guest execution
    def proc_kill(self):
        raise NotImplemented()

    def proc_list(self):
        raise NotImplemented()

    @_blocking_job
    def login(self, username, password, options=0):
        """Login to the guest to allow further executions.

        :param str username: Guest Login username.
        :param str password: Guest login password.
        :param int options: Must be 0 or VIX_LOGIN_IN_GUEST_REQUIRE_INTERACTIVE_ENVIRONMENT.

        :raises vix.VixError: On failure to authenticate.
        """

        return vix.VixVM_LoginInGuest(
            self._handle,
            ffi.new('char[]', bytes(username, API_ENCODING)) if username else ffi.cast('char*', 0),
            ffi.new('char[]', bytes(password, API_ENCODING)) if password else ffi.cast('char*', 0),
            ffi.cast('int', options),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def logout(self):
        """Logout from guest. Closes any previous login context.

        :raises vix.VixError: If failed to logout.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_LogoutFromGuest(
            self._handle,
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def proc_run(self, program_name, command_line=None, should_block=True):
        """Executes a process in guest VM.

        :param str program_name: Name of program to execute in guest.
        :param str command_line: Command line to execute program with.
        :param bool should_block: If set to True, function will block until process exits in guest.

        :raises vix.VixError: On failure to execute process.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_RunProgramInGuest(
            self._handle,
            ffi.new('char[]', bytes(program_name, API_ENCODING)),
            ffi.new('char[]', bytes(command_line, API_ENCODING)) if command_line else ffi.cast('char*', 0),
            ffi.cast('VixRunProgramOptions', 0 if should_block else self.VIX_RUNPROGRAM_RETURN_IMMEDIATELY),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def run_script(self, script_text, interpreter_path=None, should_block=True):
        """Executes a script in guest VM.

        :param str script_text: The script to execute.
        :param str interpreter_path: Path of the interpreter for the script.
        :param bool should_block: If set to False, function will return immediately. True will block untill script returns.

        :raises vix.VixError: On failure to execute script.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_RunScriptInGuest(
            self._handle,
            ffi.new('char[]', bytes(interpreter_path, API_ENCODING)) if interpreter_path else ffi.cast('char*', 0),
            ffi.new('char[]', bytes(script_text, API_ENCODING)),
            ffi.cast('VixRunProgramOptions', 0 if should_block else self.VIX_RUNPROGRAM_RETURN_IMMEDIATELY),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    # Share mgmt.
    @_blocking_job
    def add_shared_folder(self, share_name, host_path, write_access=True):
        """Shares a folder with the guest VM.

        :param str share_name: Name of share in guest VM.
        :param str host_path: Path to share in host.
        :param bool write_access: True to allow guest to write to share.

        :raises vix.VixError: On failure to add share.

        .. note:: This method is not supported by all VMware products.
        """

        # TODO: return the path of shared folder in guest.
        return vix.VixVM_AddSharedFolder(
            self._handle,
            ffi.new('char[]', bytes(share_name, API_ENCODING)),
            ffi.new('char[]', bytes(host_path, API_ENCODING)),
            ffi.cast('VixMsgSharedFolderOptions', self.VIX_SHAREDFOLDER_WRITE_ACCESS if write_access else 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def share_enable(self, value=True):
        """Enables/Disables shares between Host and guest VM.

        :param bool value: True to enable, False to disable.

        :raises vix.VixError: If failed to enable/disable shares.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_EnableSharedFolders(
            self._handle,
            ffi.cast('Bool', int(value)),
            ffi.cast('int', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    def get_shared_folder_count(self):
        """Gets the count of shared folder of VM with host.

        .. note:: This method is not supported by all VMware products.
        """

        return VixJob(vix.VixVM_GetNumSharedFolders(
            self._handle,
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )).wait(VixJob.VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_COUNT)

    def get_shared_folder_state(self):
        raise NotImplemented()

    @_blocking_job
    def share_remove(self, share_name):
        """Removes a share between host and guest VM.

        :param str share_name: Name of share to remove.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_RemoveSharedFolder(
            self._handle,
            ffi.new('char[]', bytes(share_name, API_ENCODING)),
            ffi.cast('int', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    def share_set_state(self):
        raise NotImplemented()

    # VM environment.
    def var_read(self, name, variable_type=VIX_VM_GUEST_VARIABLE):
        """Reads an environment string.

        :param str name: Name of variable to read.
        :param int variable_type: Must be one of VIX_VM_GUEST_VARIABLE, VIX_VM_CONFIG_RUNTIME_ONLY or VIX_GUEST_ENVIRONMENT_VARIABLE.

        :returns: The value of the variable.
        :rtype: str

        :raises vix.VixError: On failure to get specified variable.

        .. note:: This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixVM_ReadVariable(
            self._handle,
            ffi.cast('int', variable_type),
            ffi.new('char[]', bytes(name, API_ENCODING)),
            ffi.cast('int', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))

        return job.wait(VixJob.VIX_PROPERTY_JOB_RESULT_VM_VARIABLE_STRING)

    @_blocking_job
    def var_write(self, name, value, variable_type=VIX_VM_GUEST_VARIABLE):
        """Writes a string to the VM's environment.

        :param str name: Name of env string to set.
        :param str value: Value of env string to set.
        :param int variable_type: Must be one of VIX_VM_GUEST_VARIABLE, VIX_VM_CONFIG_RUNTIME_ONLY or VIX_GUEST_ENVIRONMENT_VARIABLE.

        :raises vix.VixError: On failure to set environment.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_WriteVariable(
            self._handle,
            ffi.cast('int', variable_type),
            ffi.new('char[]', bytes(name, API_ENCODING)),
            ffi.new('char[]', bytes(value, API_ENCODING)),
            ffi.cast('int', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )


    # Misc. methods
    @_blocking_job
    def upgrade_virtual_hardware(self):
        """Upgrades virtual hardware of a virtual machine.

        :raises vix.VixError: If failed to upgrade virtual hardware.

        .. note:: This method is not supported by all VMware products.
        """

        return vix.VixVM_UpgradeVirtualHardware(
            self._handle,
            ffi.cast('int', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def vm_delete(self, options=0):
        """Deletes VM from host.

        :param int options: settings to VIX_VMDELETE_DISK_FILES will delete associated files.

        :raises vix.VixError: If failed to delete VM.
        """

        return vix.VixVM_Delete(
            self._handle,
            ffi.cast('VixVMDeleteOptions', options),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    def capture_screen_image(self):
        raise NotImplemented()

    # VMware tools
    @_blocking_job
    def wait_for_tools(self, timeout=0):
        """Waits for VMware tools to start in guest.

        :param int timeout: Timeout in seconds. Zero or negative will block forever, Raises an exception if timeout expired.

        :raises vix.VixError: If timeout passed, Or of VIX fails.
        """

        return vix.VixVM_WaitForToolsInGuest(
            self._handle,
            ffi.cast('int', timeout),
            ffi.cast('VixEventProc', 0),
            ffi.cast('void*', 0),
        )

    @_blocking_job
    def install_tools(self, options=VIX_INSTALLTOOLS_MOUNT_TOOLS_INSTALLER):
        """Starts the VMware tools install operation on guest.

        :param int options: Can be VIX_INSTALLTOOLS_MOUNT_TOOLS_INSTALLER or VIX_INSTALLTOOLS_AUTO_UPGRADE, both can be combined with VIX_INSTALLTOOLS_RETURN_IMMEDIATELY.

        :raises vix.VixError: On failure to start install.
        """

        return vix.VixVM_InstallTools(
            self._handle,
            ffi.cast('int', options),
            ffi.cast('char*', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        )

    def __del__(self):
        self.release()
