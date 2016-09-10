import cffi
import platform
import sys


class VixBackend(object):
	"""This class creates the ffi and vix objects that will be used by other classes of this module.

	.. note:: Internal use.
	"""
	def __init__(self):

		# Allow automatic services to build docs without having VIX installed.
		if 'sphinx' in sys.modules:
			self._ffi = None
			self._vix = None
			return

		self._ffi = cffi.FFI()

		self._ffi.cdef('''
// Basic Types
typedef char          Bool;
typedef uint64_t    uint64;
typedef  int64_t     int64;
typedef uint32_t    uint32;
typedef  int32_t     int32;
typedef uint16_t    uint16;
typedef  int16_t     int16;
typedef  uint8_t    uint8;
typedef   int8_t     int8;

// VIX Types
typedef int VixHandle;
typedef int VixHandleType;
typedef uint64 VixError;
typedef int VixPropertyType;
typedef int VixPropertyID;
typedef int VixEventType;
typedef int VixHostOptions;
typedef int VixServiceProvider;
typedef int VixFindItemType;
typedef int VixVMOpenOptions;
typedef int VixVMPowerOpOptions;
typedef int VixVMDeleteOptions;
typedef int VixPowerState;
typedef int VixToolsState;
typedef int VixRunProgramOptions;
typedef int VixRemoveSnapshotOptions;
typedef int VixCreateSnapshotOptions;
typedef int VixMsgSharedFolderOptions;
typedef int VixCloneType;
typedef void VixEventProc(VixHandle handle, VixEventType eventType, VixHandle moreEventInfo, void *clientData);

// VIX functions
const char *Vix_GetErrorText(VixError err, const char *locale);

// Vix Handle functions
void Vix_ReleaseHandle(VixHandle handle);
void Vix_AddRefHandle(VixHandle handle);
VixHandleType Vix_GetHandleType(VixHandle handle);
VixError Vix_GetProperties(VixHandle handle, VixPropertyID firstPropertyID, ...);
VixError Vix_GetPropertyType(VixHandle handle, VixPropertyID propertyID, VixPropertyType *propertyType);
void Vix_FreeBuffer(void *p);

// Vix Host
VixHandle VixHost_Connect(int apiVersion, VixServiceProvider hostType, const char *hostName, int hostPort, const char *userName, const char *password, VixHostOptions options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData); 
void VixHost_Disconnect(VixHandle hostHandle);

// VM Registration
VixHandle VixHost_RegisterVM(VixHandle hostHandle, const char *vmxFilePath, VixEventProc *callbackProc, void *clientData);
VixHandle VixHost_UnregisterVM(VixHandle hostHandle, const char *vmxFilePath, VixEventProc *callbackProc, void *clientData);

// VM search
VixHandle VixHost_FindItems(VixHandle hostHandle, VixFindItemType searchType, VixHandle searchCriteria, int32 timeout, VixEventProc *callbackProc, void *clientData);

VixHandle VixHost_OpenVM(VixHandle hostHandle, const char *vmxFilePathName, VixVMOpenOptions options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);

// Property list
VixError VixPropertyList_AllocPropertyList(VixHandle hostHandle, VixHandle *resultHandle,  int firstPropertyID, ...);

// Vix VM
VixHandle VixVM_PowerOn(VixHandle vmHandle, VixVMPowerOpOptions powerOnOptions, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_PowerOff(VixHandle vmHandle, VixVMPowerOpOptions powerOffOptions, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_Reset(VixHandle vmHandle, VixVMPowerOpOptions resetOptions, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_Suspend(VixHandle vmHandle, VixVMPowerOpOptions suspendOptions, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_Pause(VixHandle vmHandle, int options, VixHandle propertyList, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_Unpause(VixHandle vmHandle, int options, VixHandle propertyList, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_Delete(VixHandle vmHandle, VixVMDeleteOptions deleteOptions, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_WaitForToolsInGuest(VixHandle vmHandle, int timeoutInSeconds, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_LoginInGuest(VixHandle vmHandle, const char *userName, const char *password, int options, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_LogoutFromGuest(VixHandle vmHandle, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_RunProgramInGuest(VixHandle vmHandle, const char *guestProgramName, const char *commandLineArgs, VixRunProgramOptions options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_ListProcessesInGuest(VixHandle vmHandle, int options, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_KillProcessInGuest(VixHandle vmHandle, uint64 pid, int options, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_RunScriptInGuest(VixHandle vmHandle, const char *interpreter, const char *scriptText, VixRunProgramOptions options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_CopyFileFromHostToGuest(VixHandle vmHandle, const char *hostPathName, const char *guestPathName, int options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_CopyFileFromGuestToHost(VixHandle vmHandle, const char *guestPathName, const char *hostPathName, int options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_DeleteFileInGuest(VixHandle vmHandle, const char *guestPathName, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_FileExistsInGuest(VixHandle vmHandle, const char *guestPathName, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_RenameFileInGuest(VixHandle vmHandle, const char *oldName, const char *newName, int options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_CreateTempFileInGuest(VixHandle vmHandle, int options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_GetFileInfoInGuest(VixHandle vmHandle, const char *pathName, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_ListDirectoryInGuest(VixHandle vmHandle, const char *pathName, int options, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_CreateDirectoryInGuest(VixHandle vmHandle, const char *pathName, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_DeleteDirectoryInGuest(VixHandle vmHandle, const char *pathName, int options, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_DirectoryExistsInGuest(VixHandle vmHandle, const char *pathName, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_ReadVariable(VixHandle vmHandle, int variableType, const char *name, int options, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_WriteVariable(VixHandle vmHandle, int variableType, const char *valueName, const char *value, int options, VixEventProc *callbackProc, void *clientData);

VixError VixVM_GetNumRootSnapshots(VixHandle vmHandle, int *result);
VixError VixVM_GetRootSnapshot(VixHandle vmHandle, int index, VixHandle *snapshotHandle);
VixError VixVM_GetCurrentSnapshot(VixHandle vmHandle, VixHandle *snapshotHandle);
VixError VixVM_GetNamedSnapshot(VixHandle vmHandle, const char *name,VixHandle *snapshotHandle);
VixHandle VixVM_RemoveSnapshot(VixHandle vmHandle, VixHandle snapshotHandle, VixRemoveSnapshotOptions options, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_RevertToSnapshot(VixHandle vmHandle, VixHandle snapshotHandle, VixVMPowerOpOptions options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_CreateSnapshot(VixHandle vmHandle, const char *name, const char *description, VixCreateSnapshotOptions options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_EnableSharedFolders(VixHandle vmHandle, Bool enabled,       int options,        VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_GetNumSharedFolders(VixHandle vmHandle, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_GetSharedFolderState(VixHandle vmHandle, int index, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_SetSharedFolderState(VixHandle vmHandle, const char *shareName, const char *hostPathName, VixMsgSharedFolderOptions flags, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_AddSharedFolder(VixHandle vmHandle, const char *shareName, const char *hostPathName, VixMsgSharedFolderOptions flags, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_RemoveSharedFolder(VixHandle vmHandle, const char *shareName, int flags, VixEventProc *callbackProc, void *clientData);

VixHandle VixVM_CaptureScreenImage(VixHandle vmHandle, int captureType, VixHandle additionalProperties, VixEventProc *callbackProc, void *clientdata);

VixHandle VixVM_Clone(VixHandle vmHandle, VixHandle snapshotHandle, VixCloneType cloneType, const char *destConfigPathName, int options, VixHandle propertyListHandle, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_UpgradeVirtualHardware(VixHandle vmHandle, int options, VixEventProc *callbackProc, void *clientData);
VixHandle VixVM_InstallTools(VixHandle vmHandle, int options, const char *commandLineArgs, VixEventProc *callbackProc, void *clientData);

VixError VixJob_Wait(VixHandle jobHandle,  VixPropertyID firstPropertyID,  ...);
VixError VixJob_CheckCompletion(VixHandle jobHandle, Bool *complete);
VixError VixJob_GetError(VixHandle jobHandle);

int VixJob_GetNumProperties(VixHandle jobHandle, int resultPropertyID);
VixError VixJob_GetNthProperties(VixHandle jobHandle, int index, int propertyID, ...);

VixError VixSnapshot_GetNumChildren(VixHandle parentSnapshotHandle, int *numChildSnapshots);
VixError VixSnapshot_GetChild(VixHandle parentSnapshotHandle, int index, VixHandle *childSnapshotHandle);
VixError VixSnapshot_GetParent(VixHandle snapshotHandle, VixHandle *parentSnapshotHandle);
		''')
		self._vix = self._ffi.dlopen(VixBackend._get_vix_path())

	@staticmethod
	def _get_vix_path():
		"""Finds the expected install path for the so/dll.

		:returns: Expected path.
		:rtype: str

		:raises NotImplented: If the OS/architecture are not recognized.
		"""

		os_name = platform.system()

		if os_name == 'Linux':
			return '/usr/lib/libvixAllProducts.so'
		elif os_name == 'Windows':
			arch = platform.architecture()[0].lower()
			if arch == '64bit':
				return r'C:\Program Files (x86)\VMware\VMware VIX\Vix64AllProductsDyn.dll'
			elif arch == '32bit':
				return r'C:\Program Files\VMware\VMware VIX\VixAllProductsDyn.dll'
			else:
				raise NotImplemented('VixAllProductsDyn.dll could not be found.')
		else:
			raise NotImplemented("This VIX wrapper doesn't cover this OS")
