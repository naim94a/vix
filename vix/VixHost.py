from .VixJob import VixJob
from .VixVM import VixVM
from .VixHandle import VixHandle
from .VixError import VixError
from vix import _backend, API_ENCODING
vix = _backend._vix
ffi = _backend._ffi

@ffi.callback('void(*)(VixHandle, VixEventType, VixHandle, void*)')
def _find_items_callback(job_handle, event_type, event_info, client_data):
    pass

class VixHost(object):
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

    def __init__(self):
        self._handle = None

    def connect(self, service_provider=VIX_SERVICEPROVIDER_DEFAULT, host=None, credentials=None):
        """Connects to a VMware host.

        Arguments:
        service_provider    Specifies the service to connect to, may be any of VIX_SERVICEPROVIDER_*.
        host                A tuple (hostname, port).
        credentials         A tuple (username, password).
        """

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
            ffi.cast('const char*', bytes(host[0], API_ENCODING) if host[0] else 0),
            host[1],
            ffi.cast('const char*', bytes(credentials[0], API_ENCODING) if credentials[0] else 0),
            ffi.cast('const char*', bytes(credentials[1], API_ENCODING) if credentials[1] else 0),
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

        Arguments:
        vmx_path        Path of VM configuration to register.
        
        This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixHost_RegisterVM(
            self._handle,
            ffi.cast('const char*', bytes(vmx_path, API_ENCODING)),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))
        error_code = job.wait()
        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

    def unregister_vm(self, vmx_path):
        """Unregisters a VM from host.

        Arguments:
        vmx_path        Path of VM configuration to unregister.
        
        This method is not supported by all VMware products.
        """

        job = VixJob(vix.VixHost_UnregisterVM(
            self._handle,
            ffi.cast('const char*', bytes(vmx_path, API_ENCODING)),
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))
        error_code = job.wait()
        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

    def open_vm(self, vmx_path):
        """Opens a VM in host.

        Arguments:
        vmx_path        Path to requested VM's configuration.
        """

        assert self._handle is not None, 'Must be connected.'

        job = VixJob(vix.VixHost_OpenVM(
            self._handle,
            ffi.new('char[]', bytes(vmx_path, API_ENCODING)),
            0,
            0,
            ffi.cast('VixEventProc*', 0),
            ffi.cast('void*', 0),
        ))

        return VixVM(job.wait(VixJob.VIX_PROPERTY_JOB_RESULT_HANDLE))

    def find_items(self, search_type=VIX_FIND_RUNNING_VMS):
        """Finds VMs on host with requested citeria.

        Arguments:
        search_type         Any of VIX_FIND_*.
        """
        job = VixJob(vix.VixHost_FindItems(
            self._handle,
            ffi.cast('VixFindItemType', search_type),
            ffi.cast('VixHandle', 0),
            ffi.cast('int32', -1),
            ffi.cast('VixEventProc*', _find_items_callback),
            ffi.cast('void*', 0),
        ))

        error_code = job.wait()
        if error_code != VixError.VIX_OK:
            raise VixError(error_code)

    def __del__(self):
        self.disconnect()
