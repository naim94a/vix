from __future__ import absolute_import

from collections import namedtuple
from .compat import _bytes, _str
from .VixJob import VixJob
from .VixVM import VixVM
from .VixHandle import VixHandle
from .VixError import VixError
from vix import _backend, API_ENCODING
vix = _backend._vix
ffi = _backend._ffi

_find_results = dict()

@ffi.callback('void(*)(VixHandle, VixEventType, VixHandle, void*)')
def _find_items_callback(job_handle, event_type, event_info, client_data):
    """Callback that collects found VMs.

    .. note:: Internal use.
    """

    VIX_EVENTTYPE_JOB_COMPLETED = 2
    VIX_EVENTTYPE_JOB_PROGRESS = 3
    VIX_EVENTTYPE_FIND_ITEM = 8

    if event_type != VIX_EVENTTYPE_FIND_ITEM:
        return

    idx = int(ffi.cast('int', client_data))
    str_ptr = ffi.new('char**')

    error_code = vix.Vix_GetProperties(
        ffi.cast('VixHandle', event_info),
        ffi.cast('VixPropertyID', VixJob.VIX_PROPERTY_FOUND_ITEM_LOCATION),
        ffi.cast('char**', str_ptr),
        ffi.cast('VixPropertyID', VixJob.VIX_PROPERTY_NONE),
    )

    if error_code != VixError.VIX_OK:
        return

    vmx = _str(ffi.string(str_ptr[0]), API_ENCODING)

    _find_results[idx].append(vmx)
    vix.Vix_FreeBuffer(str_ptr[0])

VixHostInfo = namedtuple('VixHostInfo', 'host_type api_version software_version')


class VixHost(object):
    """Represents a VMware virtualization host."""

    VIX_API_VERSION = -1

    VIX_HOSTOPTION_VERIFY_SSL_CERT = 0x4000

    VIX_SERVICEPROVIDER_DEFAULT = 1
    VIX_SERVICEPROVIDER_VMWARE_SERVER = 2
    VIX_SERVICEPROVIDER_VMWARE_WORKSTATION = 3
    VIX_SERVICEPROVIDER_VMWARE_PLAYER = 4
    VIX_SERVICEPROVIDER_VMWARE_VI_SERVER = 10
    VIX_SERVICEPROVIDER_VMWARE_WORKSTATION_SHARED = 11

    VIX_FIND_RUNNING_VMS = 1
    VIX_FIND_REGISTERED_VMS = 4

    @property
    def host_info(self):
        """property returns the Host's version.

        :returns: Host's type, api and software version.
        :rtype: .VixHostInfo

        :raises vix.VixError: If failed to get version information.
        """
        res = VixHandle(self._handle).get_properties(
            VixHandle.VIX_PROPERTY_HOST_HOSTTYPE,
            VixHandle.VIX_PROPERTY_HOST_API_VERSION,
            VixHandle.VIX_PROPERTY_HOST_SOFTWARE_VERSION,
        )
        return VixHostInfo(host_type=res[0], api_version=res[1], software_version=res[2])

    def __init__(self, service_provider=VIX_SERVICEPROVIDER_DEFAULT, host=None, credentials=None):
        """Connects to a VMware host.

        :param int service_provider: Specifies the service to connect to, may be any of VIX_SERVICEPROVIDER_* constants.
        :param tuple host: (hostname, port).
        :param tuple credentials: (username, password).

        :raises AssertionError: If passed arguments are not the right types/sizes.
        :raises vix.VixError: On connection failure.
        """
        self._handle = None

        assert self._handle == None, 'Instance is already connected.'

        if not host:
            host = (None, 0, )
        if not credentials:
            credentials = (None, None, )

        assert len(host) == 2 and type(host) == tuple, 'Host must be a tuple of size 2'
        assert len(credentials) == 2 and type(credentials) == tuple, 'Credentials must be a tuple of size 2'

        job = VixJob(vix.VixHost_Connect(
            self.VIX_API_VERSION,
            service_provider,
            ffi.cast('const char*', _bytes(host[0], API_ENCODING) if host[0] else 0),
            host[1],
            ffi.cast('const char*', _bytes(credentials[0], API_ENCODING) if credentials[0] else 0),
            ffi.cast('const char*', _bytes(credentials[1], API_ENCODING) if credentials[1] else 0),
            0,
            0,
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))

        self._handle = job.wait(VixJob.VIX_PROPERTY_JOB_RESULT_HANDLE)

    def disconnect(self):
        """Disconnects from the host."""

        if self._handle:
            vix.VixHost_Disconnect(self._handle)
            VixHandle(self._handle).release()
            self._handle = None

    def register_vm(self, vmx_path):
        """Registers a VM to host.

        :param str vmx_path: Path of VM configuration to register.

        :raises vix.VixError: If failed to register VM.
        
        .. note:: This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixHost_RegisterVM(
            self._handle,
            ffi.cast('const char*', _bytes(vmx_path, API_ENCODING)),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))
        error_code = job.wait()
        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

    def unregister_vm(self, vmx_path):
        """Unregisters a VM from host.

        :param str vmx_path: Path of VM configuration to unregister.
        
        :raises vix.VixError: If failed to unregister VM.

        .. note:: This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixHost_UnregisterVM(
            self._handle,
            ffi.cast('const char*', _bytes(vmx_path, API_ENCODING)),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))
        error_code = job.wait()
        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

    def open_vm(self, vmx_path):
        """Opens a VM in host.

        :param str vmx_path: Path to requested VM's configuration.

        :rtype: vix.VixVM

        :raises vix.VixError: If failed to open requested VM.
        """

        assert self._handle is not None, 'Must be connected.'

        job = VixJob(vix.VixHost_OpenVM(
            self._handle,
            ffi.new('char[]', _bytes(vmx_path, API_ENCODING)),
            ffi.cast('VixVMOpenOptions', 0),
            ffi.cast('VixHandle', 0),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))

        return VixVM(job.wait(VixJob.VIX_PROPERTY_JOB_RESULT_HANDLE), vmx_path)

    def find_items(self, search_type=VIX_FIND_RUNNING_VMS, names_only=False):
        """Finds VMs on host with requested citeria.

        :param int search_type: Any of VIX_FIND_*.
        :param bool names_only: True will return a list of vmx paths, False will return VixVM instances.

        :returns: List of found VMs.
        :rtype: list

        :raises vix.VixError: On failure to find items.
        """

        key = len(_find_results)
        _find_results[key] = list()

        job = VixJob(vix.VixHost_FindItems(
            self._handle,
            ffi.cast('VixFindItemType', search_type),
            ffi.cast('VixHandle', 0),
            ffi.cast('int32', -1),
            ffi.cast('VixEventProc*', _find_items_callback),
            ffi.cast('void*', key),
        ))

        job.wait()

        items = _find_results.pop(key)

        if names_only:
            return items
        else:
            return [self.open_vm(vmx_path) for vmx_path in items]

    def __del__(self):
        self.disconnect()
