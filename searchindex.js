Search.setIndex({envversion:50,filenames:["index","vix"],objects:{"vix.VixBackend":{VixBackend:[1,0,1,""]},"vix.VixBackend.VixBackend":{_get_vix_path:[1,1,1,""]},"vix.VixError":{ERRORS:[1,3,1,""],VIX_ASYNC:[1,3,1,""],VIX_E_ALREADY_EXISTS:[1,3,1,""],VIX_E_ANON_GUEST_OPERATIONS_PROHIBITED:[1,3,1,""],VIX_E_ARGUMENT_TOO_BIG:[1,3,1,""],VIX_E_ASYNC_MIXEDMODE_UNSUPPORTED:[1,3,1,""],VIX_E_AUTHENTICATION_FAIL:[1,3,1,""],VIX_E_BAD_VM_INDEX:[1,3,1,""],VIX_E_BUFFER_TOOSMALL:[1,3,1,""],VIX_E_CANCELLED:[1,3,1,""],VIX_E_CANNOT_AUTHENTICATE_WITH_GUEST:[1,3,1,""],VIX_E_CANNOT_CONNECT_TO_HOST:[1,3,1,""],VIX_E_CANNOT_CONNECT_TO_VM:[1,3,1,""],VIX_E_CANNOT_POWER_ON_VM:[1,3,1,""],VIX_E_CANNOT_READ_VM_CONFIG:[1,3,1,""],VIX_E_CANNOT_START_READ_ONLY_VM:[1,3,1,""],VIX_E_CONSOLE_GUEST_OPERATIONS_PROHIBITED:[1,3,1,""],VIX_E_CRYPTO_BAD_BUFFER_SIZE:[1,3,1,""],VIX_E_CRYPTO_BAD_FORMAT:[1,3,1,""],VIX_E_CRYPTO_BAD_PASSWORD:[1,3,1,""],VIX_E_CRYPTO_EMPTY:[1,3,1,""],VIX_E_CRYPTO_ERROR:[1,3,1,""],VIX_E_CRYPTO_INVALID_OPERATION:[1,3,1,""],VIX_E_CRYPTO_KEYSAFE_LOCATOR:[1,3,1,""],VIX_E_CRYPTO_LOCKED:[1,3,1,""],VIX_E_CRYPTO_NEED_PASSWORD:[1,3,1,""],VIX_E_CRYPTO_NOT_IN_DICTIONARY:[1,3,1,""],VIX_E_CRYPTO_NO_CRYPTO:[1,3,1,""],VIX_E_CRYPTO_RANDOM_DEVICE:[1,3,1,""],VIX_E_CRYPTO_UNKNOWN_ALGORITHM:[1,3,1,""],VIX_E_DISK_ATTACH_ROOTLINK:[1,3,1,""],VIX_E_DISK_CANTREPAIR:[1,3,1,""],VIX_E_DISK_CANTSHRINK:[1,3,1,""],VIX_E_DISK_CAPACITY_MISMATCH:[1,3,1,""],VIX_E_DISK_CID_MISMATCH:[1,3,1,""],VIX_E_DISK_ENCODING:[1,3,1,""],VIX_E_DISK_FULL:[1,3,1,""],VIX_E_DISK_INVAL:[1,3,1,""],VIX_E_DISK_INVALIDCHAIN:[1,3,1,""],VIX_E_DISK_INVALIDDISK:[1,3,1,""],VIX_E_DISK_INVALIDPARTITIONTABLE:[1,3,1,""],VIX_E_DISK_INVALID_CONNECTION:[1,3,1,""],VIX_E_DISK_KEY_NOTFOUND:[1,3,1,""],VIX_E_DISK_NEEDKEY:[1,3,1,""],VIX_E_DISK_NEEDSREPAIR:[1,3,1,""],VIX_E_DISK_NEEDVMFS:[1,3,1,""],VIX_E_DISK_NODEVICE:[1,3,1,""],VIX_E_DISK_NOINIT:[1,3,1,""],VIX_E_DISK_NOIO:[1,3,1,""],VIX_E_DISK_NOKEY:[1,3,1,""],VIX_E_DISK_NOKEYOVERRIDE:[1,3,1,""],VIX_E_DISK_NOLICENSE:[1,3,1,""],VIX_E_DISK_NOTENCDESC:[1,3,1,""],VIX_E_DISK_NOTENCRYPTED:[1,3,1,""],VIX_E_DISK_NOTNORMAL:[1,3,1,""],VIX_E_DISK_NOTSUPPORTED:[1,3,1,""],VIX_E_DISK_OPENPARENT:[1,3,1,""],VIX_E_DISK_OUTOFRANGE:[1,3,1,""],VIX_E_DISK_PARENT_NOTALLOWED:[1,3,1,""],VIX_E_DISK_PARTIALCHAIN:[1,3,1,""],VIX_E_DISK_PARTMISMATCH:[1,3,1,""],VIX_E_DISK_RAWTOOBIG:[1,3,1,""],VIX_E_DISK_RAWTOOSMALL:[1,3,1,""],VIX_E_DISK_SUBSYSTEM_INIT_FAIL:[1,3,1,""],VIX_E_DISK_TOOMANYOPENFILES:[1,3,1,""],VIX_E_DISK_TOOMANYREDO:[1,3,1,""],VIX_E_DISK_UNSUPPORTEDDEVICE:[1,3,1,""],VIX_E_DISK_UNSUPPORTEDDISKVERSION:[1,3,1,""],VIX_E_DUPLICATE_NAME:[1,3,1,""],VIX_E_EMPTY_PASSWORD_NOT_ALLOWED_IN_GUEST:[1,3,1,""],VIX_E_FAIL:[1,3,1,""],VIX_E_FILE_ACCESS_ERROR:[1,3,1,""],VIX_E_FILE_ALREADY_EXISTS:[1,3,1,""],VIX_E_FILE_ALREADY_LOCKED:[1,3,1,""],VIX_E_FILE_ERROR:[1,3,1,""],VIX_E_FILE_NAME_INVALID:[1,3,1,""],VIX_E_FILE_NAME_TOO_LONG:[1,3,1,""],VIX_E_FILE_NOT_FOUND:[1,3,1,""],VIX_E_FILE_READ_ONLY:[1,3,1,""],VIX_E_FILE_TOO_BIG:[1,3,1,""],VIX_E_GUEST_OPERATIONS_PROHIBITED:[1,3,1,""],VIX_E_GUEST_USER_PERMISSIONS:[1,3,1,""],VIX_E_GUEST_VOLUMES_NOT_FROZEN:[1,3,1,""],VIX_E_HOST_CONNECTION_LOST:[1,3,1,""],VIX_E_HOST_DISK_INVALID_VALUE:[1,3,1,""],VIX_E_HOST_DISK_SECTORSIZE:[1,3,1,""],VIX_E_HOST_FILE_ERROR_EOF:[1,3,1,""],VIX_E_HOST_NBD_HASHFILE_INIT:[1,3,1,""],VIX_E_HOST_NBD_HASHFILE_VOLUME:[1,3,1,""],VIX_E_HOST_NETBLKDEV_HANDSHAKE:[1,3,1,""],VIX_E_HOST_NETWORK_CONN_REFUSED:[1,3,1,""],VIX_E_HOST_NOT_CONNECTED:[1,3,1,""],VIX_E_HOST_SERVER_NOT_FOUND:[1,3,1,""],VIX_E_HOST_SOCKET_CREATION_ERROR:[1,3,1,""],VIX_E_HOST_TCP_CONN_LOST:[1,3,1,""],VIX_E_HOST_TCP_SOCKET_ERROR:[1,3,1,""],VIX_E_HOST_USER_PERMISSIONS:[1,3,1,""],VIX_E_INCORRECT_FILE_TYPE:[1,3,1,""],VIX_E_INTERACTIVE_SESSION_NOT_PRESENT:[1,3,1,""],VIX_E_INTERACTIVE_SESSION_USER_MISMATCH:[1,3,1,""],VIX_E_INVALID_ARG:[1,3,1,""],VIX_E_INVALID_AUTHENTICATION_SESSION:[1,3,1,""],VIX_E_INVALID_HANDLE:[1,3,1,""],VIX_E_INVALID_HOSTNAME_SPECIFICATION:[1,3,1,""],VIX_E_INVALID_MESSAGE_BODY:[1,3,1,""],VIX_E_INVALID_MESSAGE_HEADER:[1,3,1,""],VIX_E_INVALID_PROPERTY_VALUE:[1,3,1,""],VIX_E_INVALID_SERIALIZED_DATA:[1,3,1,""],VIX_E_INVALID_UTF8_STRING:[1,3,1,""],VIX_E_INVALID_XML:[1,3,1,""],VIX_E_LICENSE:[1,3,1,""],VIX_E_LOGIN_TYPE_NOT_SUPPORTED:[1,3,1,""],VIX_E_MISSING_ANON_GUEST_ACCOUNT:[1,3,1,""],VIX_E_MISSING_REQUIRED_PROPERTY:[1,3,1,""],VIX_E_MNTAPI_ALREADY_OPENED:[1,3,1,""],VIX_E_MNTAPI_CANT_MAKE_VAR_DIR:[1,3,1,""],VIX_E_MNTAPI_CANT_READ_PARTS:[1,3,1,""],VIX_E_MNTAPI_CODECONVERSION:[1,3,1,""],VIX_E_MNTAPI_CREATE_PARTITIONTABLE_ERROR:[1,3,1,""],VIX_E_MNTAPI_DAEMON:[1,3,1,""],VIX_E_MNTAPI_DICT:[1,3,1,""],VIX_E_MNTAPI_DICT_LOCKED:[1,3,1,""],VIX_E_MNTAPI_DISK_CANT_OPEN:[1,3,1,""],VIX_E_MNTAPI_DISK_IS_MOUNTED:[1,3,1,""],VIX_E_MNTAPI_DISK_NOT_FOUND:[1,3,1,""],VIX_E_MNTAPI_DISK_NOT_MOUNTED:[1,3,1,""],VIX_E_MNTAPI_DISK_NOT_SAFE:[1,3,1,""],VIX_E_MNTAPI_DRIVE_LETTER_ALREADY_ASSIGNED:[1,3,1,""],VIX_E_MNTAPI_DRIVE_LETTER_IN_USE:[1,3,1,""],VIX_E_MNTAPI_FORMAT_FAILURE:[1,3,1,""],VIX_E_MNTAPI_GETFILE_ERROR:[1,3,1,""],VIX_E_MNTAPI_INCOMPATIBLE_VERSION:[1,3,1,""],VIX_E_MNTAPI_INTERNAL:[1,3,1,""],VIX_E_MNTAPI_ITEM_NOT_FOUND:[1,3,1,""],VIX_E_MNTAPI_LOOP_FAILED:[1,3,1,""],VIX_E_MNTAPI_MOUNTPT_IN_USE:[1,3,1,""],VIX_E_MNTAPI_MOUNTPT_NOT_FOUND:[1,3,1,""],VIX_E_MNTAPI_NO_CONNECTION_DETAILS:[1,3,1,""],VIX_E_MNTAPI_NO_DRIVER:[1,3,1,""],VIX_E_MNTAPI_NO_MOUNTABLE_PARTITONS:[1,3,1,""],VIX_E_MNTAPI_NO_ROOT:[1,3,1,""],VIX_E_MNTAPI_OPEN_FAILURE:[1,3,1,""],VIX_E_MNTAPI_OPEN_HANDLES:[1,3,1,""],VIX_E_MNTAPI_OS_ERROR:[1,3,1,""],VIX_E_MNTAPI_PARTITION_NOT_FOUND:[1,3,1,""],VIX_E_MNTAPI_PARTITION_RANGE:[1,3,1,""],VIX_E_MNTAPI_PERM:[1,3,1,""],VIX_E_MNTAPI_PUTFILE_ERROR:[1,3,1,""],VIX_E_MNTAPI_REGDELKEY_ERROR:[1,3,1,""],VIX_E_MNTAPI_REGWRITE_ERROR:[1,3,1,""],VIX_E_MNTAPI_REG_NOT_OPENED:[1,3,1,""],VIX_E_MNTAPI_SYSTEM:[1,3,1,""],VIX_E_MNTAPI_UMOUNT:[1,3,1,""],VIX_E_MNTAPI_UMOUNT_APP_NOT_FOUND:[1,3,1,""],VIX_E_MNTAPI_UNSUPPORTED_FT_VOLUME:[1,3,1,""],VIX_E_MNTAPI_UNSUPPROTED_BOOT_LOADER:[1,3,1,""],VIX_E_MNTAPI_UNSUPPROTED_OS:[1,3,1,""],VIX_E_MNTAPI_VOLUME_ALREADY_MOUNTED:[1,3,1,""],VIX_E_MNTAPI_VOLUME_NOT_MOUNTED:[1,3,1,""],VIX_E_MNTAPI_VOLUME_NOT_WRITABLE:[1,3,1,""],VIX_E_MUST_BE_CONSOLE_USER:[1,3,1,""],VIX_E_NEED_KEY:[1,3,1,""],VIX_E_NET_HTTP_COULDNT_CONNECT:[1,3,1,""],VIX_E_NET_HTTP_COULDNT_RESOLVE_HOST:[1,3,1,""],VIX_E_NET_HTTP_COULDNT_RESOLVE_PROXY:[1,3,1,""],VIX_E_NET_HTTP_GENERIC:[1,3,1,""],VIX_E_NET_HTTP_HTTP_RETURNED_ERROR:[1,3,1,""],VIX_E_NET_HTTP_OPERATION_TIMEDOUT:[1,3,1,""],VIX_E_NET_HTTP_SSL_CONNECT_ERROR:[1,3,1,""],VIX_E_NET_HTTP_SSL_SECURITY:[1,3,1,""],VIX_E_NET_HTTP_TOO_MANY_REDIRECTS:[1,3,1,""],VIX_E_NET_HTTP_TRANSFER:[1,3,1,""],VIX_E_NET_HTTP_UNSUPPORTED_PROTOCOL:[1,3,1,""],VIX_E_NET_HTTP_URL_MALFORMAT:[1,3,1,""],VIX_E_NOT_A_DIRECTORY:[1,3,1,""],VIX_E_NOT_A_FILE:[1,3,1,""],VIX_E_NOT_FOR_REMOTE_HOST:[1,3,1,""],VIX_E_NOT_FOUND:[1,3,1,""],VIX_E_NOT_SUPPORTED:[1,3,1,""],VIX_E_NOT_SUPPORTED_FOR_VM_VERSION:[1,3,1,""],VIX_E_NOT_SUPPORTED_ON_HANDLE_TYPE:[1,3,1,""],VIX_E_NOT_SUPPORTED_ON_REMOTE_OBJECT:[1,3,1,""],VIX_E_NO_DISPLAY_SERVER:[1,3,1,""],VIX_E_NO_GUEST_OS_INSTALLED:[1,3,1,""],VIX_E_NO_SUCH_PROCESS:[1,3,1,""],VIX_E_OBJECT_IS_BUSY:[1,3,1,""],VIX_E_OBJECT_NOT_FOUND:[1,3,1,""],VIX_E_OPERATION_ALREADY_IN_PROGRESS:[1,3,1,""],VIX_E_OPERATION_DISABLED:[1,3,1,""],VIX_E_OPERATION_NOT_ALLOWED_FOR_LOGIN_TYPE:[1,3,1,""],VIX_E_OP_NOT_SUPPORTED_ON_GUEST:[1,3,1,""],VIX_E_OUT_OF_MEMORY:[1,3,1,""],VIX_E_POWEROP_SCRIPTS_NOT_AVAILABLE:[1,3,1,""],VIX_E_PROGRAM_NOT_STARTED:[1,3,1,""],VIX_E_PROPERTY_TYPE_MISMATCH:[1,3,1,""],VIX_E_READ_ONLY_PROPERTY:[1,3,1,""],VIX_E_REQUIRES_LARGE_FILES:[1,3,1,""],VIX_E_ROOT_GUEST_OPERATIONS_PROHIBITED:[1,3,1,""],VIX_E_SCREEN_CAPTURE_BAD_FORMAT:[1,3,1,""],VIX_E_SCREEN_CAPTURE_COMPRESSION_FAIL:[1,3,1,""],VIX_E_SCREEN_CAPTURE_ERROR:[1,3,1,""],VIX_E_SCREEN_CAPTURE_LARGE_DATA:[1,3,1,""],VIX_E_SNAPSHOT_CHECKPOINT:[1,3,1,""],VIX_E_SNAPSHOT_CONFIG:[1,3,1,""],VIX_E_SNAPSHOT_DISKLIB:[1,3,1,""],VIX_E_SNAPSHOT_DISKLOCKED:[1,3,1,""],VIX_E_SNAPSHOT_DUMPER:[1,3,1,""],VIX_E_SNAPSHOT_DUPLICATEDDISK:[1,3,1,""],VIX_E_SNAPSHOT_EXISTS:[1,3,1,""],VIX_E_SNAPSHOT_HIERARCHY_TOODEEP:[1,3,1,""],VIX_E_SNAPSHOT_INCONSISTENT:[1,3,1,""],VIX_E_SNAPSHOT_INDEPENDENTDISK:[1,3,1,""],VIX_E_SNAPSHOT_INVAL:[1,3,1,""],VIX_E_SNAPSHOT_LOCKED:[1,3,1,""],VIX_E_SNAPSHOT_MAXSNAPSHOTS:[1,3,1,""],VIX_E_SNAPSHOT_MEMORY_ON_INDEPENDENT_DISK:[1,3,1,""],VIX_E_SNAPSHOT_MIN_FREE_SPACE:[1,3,1,""],VIX_E_SNAPSHOT_NAMETOOLONG:[1,3,1,""],VIX_E_SNAPSHOT_NOCHANGE:[1,3,1,""],VIX_E_SNAPSHOT_NONUNIQUE_NAME:[1,3,1,""],VIX_E_SNAPSHOT_NOPERM:[1,3,1,""],VIX_E_SNAPSHOT_NOTFOUND:[1,3,1,""],VIX_E_SNAPSHOT_NOT_REVERTABLE:[1,3,1,""],VIX_E_SNAPSHOT_VERSION:[1,3,1,""],VIX_E_SNAPSHOT_VIXFILE:[1,3,1,""],VIX_E_SUSPEND_ERROR:[1,3,1,""],VIX_E_TEMPLATE_VM:[1,3,1,""],VIX_E_TIMEOUT_WAITING_FOR_TOOLS:[1,3,1,""],VIX_E_TOOLS_INSTALL_ALREADY_UP_TO_DATE:[1,3,1,""],VIX_E_TOOLS_INSTALL_AUTO_NOT_SUPPORTED:[1,3,1,""],VIX_E_TOOLS_INSTALL_CANCELLED:[1,3,1,""],VIX_E_TOOLS_INSTALL_DEVICE_NOT_CONNECTED:[1,3,1,""],VIX_E_TOOLS_INSTALL_ERROR:[1,3,1,""],VIX_E_TOOLS_INSTALL_GUEST_NOT_READY:[1,3,1,""],VIX_E_TOOLS_INSTALL_IMAGE_COPY_FAILED:[1,3,1,""],VIX_E_TOOLS_INSTALL_IMAGE_INACCESIBLE:[1,3,1,""],VIX_E_TOOLS_INSTALL_INIT_FAILED:[1,3,1,""],VIX_E_TOOLS_INSTALL_IN_PROGRESS:[1,3,1,""],VIX_E_TOOLS_INSTALL_NO_DEVICE:[1,3,1,""],VIX_E_TOOLS_INSTALL_NO_IMAGE:[1,3,1,""],VIX_E_TOOLS_NOT_RUNNING:[1,3,1,""],VIX_E_TOO_MANY_HANDLES:[1,3,1,""],VIX_E_TOO_MANY_LOGONS:[1,3,1,""],VIX_E_TYPE_MISMATCH:[1,3,1,""],VIX_E_UNFINISHED_JOB:[1,3,1,""],VIX_E_UNRECOGNIZED_COMMAND:[1,3,1,""],VIX_E_UNRECOGNIZED_COMMAND_IN_GUEST:[1,3,1,""],VIX_E_UNRECOGNIZED_PROPERTY:[1,3,1,""],VIX_E_VMDB:[1,3,1,""],VIX_E_VMX_MSG_DIALOG_AND_NO_UI:[1,3,1,""],VIX_E_VM_ALREADY_LOADED:[1,3,1,""],VIX_E_VM_ALREADY_UP_TO_DATE:[1,3,1,""],VIX_E_VM_HOST_DISCONNECTED:[1,3,1,""],VIX_E_VM_INSUFFICIENT_HOST_MEMORY:[1,3,1,""],VIX_E_VM_IS_RUNNING:[1,3,1,""],VIX_E_VM_NOT_ENOUGH_CPUS:[1,3,1,""],VIX_E_VM_NOT_FOUND:[1,3,1,""],VIX_E_VM_NOT_RUNNING:[1,3,1,""],VIX_E_VM_UNSUPPORTED_GUEST:[1,3,1,""],VIX_E_WRAPPER_MULTIPLE_SERVICEPROVIDERS:[1,3,1,""],VIX_E_WRAPPER_PLAYER_NOT_INSTALLED:[1,3,1,""],VIX_E_WRAPPER_RUNTIME_NOT_INSTALLED:[1,3,1,""],VIX_E_WRAPPER_SERVICEPROVIDER_NOT_FOUND:[1,3,1,""],VIX_E_WRAPPER_VERSION_NOT_FOUND:[1,3,1,""],VIX_E_WRAPPER_WORKSTATION_NOT_INSTALLED:[1,3,1,""],VIX_OK:[1,3,1,""]},"vix.VixHandle":{VixHandle:[1,0,1,""]},"vix.VixHandle.VixHandle":{VIX_HANDLETYPE_HOST:[1,3,1,""],VIX_HANDLETYPE_JOB:[1,3,1,""],VIX_HANDLETYPE_METADATA_CONTAINER:[1,3,1,""],VIX_HANDLETYPE_NETWORK:[1,3,1,""],VIX_HANDLETYPE_NONE:[1,3,1,""],VIX_HANDLETYPE_PROPERTY_LIST:[1,3,1,""],VIX_HANDLETYPE_SNAPSHOT:[1,3,1,""],VIX_HANDLETYPE_VM:[1,3,1,""],VIX_INVALID_HANDLE:[1,3,1,""],add_ref:[1,4,1,""],get_type:[1,4,1,""],is_valid:[1,4,1,""],release:[1,4,1,""]},"vix.VixHost":{VIX_API_VERSION:[1,3,1,""],VIX_FIND_REGISTERED_VMS:[1,3,1,""],VIX_FIND_RUNNING_VMS:[1,3,1,""],VIX_HOSTOPTION_VERIFY_SSL_CERT:[1,3,1,""],VIX_SERVICEPROVIDER_DEFAULT:[1,3,1,""],VIX_SERVICEPROVIDER_VMWARE_PLAYER:[1,3,1,""],VIX_SERVICEPROVIDER_VMWARE_SERVER:[1,3,1,""],VIX_SERVICEPROVIDER_VMWARE_VI_SERVER:[1,3,1,""],VIX_SERVICEPROVIDER_VMWARE_WORKSTATION:[1,3,1,""],VIX_SERVICEPROVIDER_VMWARE_WORKSTATION_SHARED:[1,3,1,""],connect:[1,4,1,""],disconnect:[1,4,1,""],find_items:[1,4,1,""],open_vm:[1,4,1,""],register_vm:[1,4,1,""],unregister_vm:[1,4,1,""]},"vix.VixJob":{VixJob:[1,0,1,""]},"vix.VixJob.VixJob":{STR_RESULT_TYPES:[1,3,1,""],VIX_FILE_ATTRIBUTES_DIRECTORY:[1,3,1,""],VIX_FILE_ATTRIBUTES_SYMLINK:[1,3,1,""],VIX_PROPERTYTYPE_ANY:[1,3,1,""],VIX_PROPERTYTYPE_BLOB:[1,3,1,""],VIX_PROPERTYTYPE_BOOL:[1,3,1,""],VIX_PROPERTYTYPE_HANDLE:[1,3,1,""],VIX_PROPERTYTYPE_INT64:[1,3,1,""],VIX_PROPERTYTYPE_INTEGER:[1,3,1,""],VIX_PROPERTYTYPE_STRING:[1,3,1,""],VIX_PROPERTY_FOUND_ITEM_LOCATION:[1,3,1,""],VIX_PROPERTY_GUEST_SHAREDFOLDERS_SHARES_PATH:[1,3,1,""],VIX_PROPERTY_HOST_API_VERSION:[1,3,1,""],VIX_PROPERTY_HOST_HOSTTYPE:[1,3,1,""],VIX_PROPERTY_HOST_SOFTWARE_VERSION:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_COMMAND_OUTPUT:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_ERROR_CODE:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_EXIT_CODE:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_EXTRA_ERROR_INFO:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_FILE_FLAGS:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_FILE_MOD_TIME:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_FILE_SIZE:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_FOUND_ITEM_DESCRIPTION:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_GUEST_OBJECT_EXISTS:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_GUEST_PROGRAM_ELAPSED_TIME:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_GUEST_PROGRAM_EXIT_CODE:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_HANDLE:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_ITEM_NAME:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_PROCESS_BEING_DEBUGGED:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_PROCESS_COMMAND:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_PROCESS_ID:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_PROCESS_OWNER:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_PROCESS_START_TIME:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_SCREEN_IMAGE_DATA:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_SCREEN_IMAGE_SIZE:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_COUNT:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_FLAGS:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_HOST:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_USER_MESSAGE:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_VM_IN_GROUP:[1,3,1,""],VIX_PROPERTY_JOB_RESULT_VM_VARIABLE_STRING:[1,3,1,""],VIX_PROPERTY_META_DATA_CONTAINER:[1,3,1,""],VIX_PROPERTY_NONE:[1,3,1,""],VIX_PROPERTY_SNAPSHOT_DESCRIPTION:[1,3,1,""],VIX_PROPERTY_SNAPSHOT_DISPLAYNAME:[1,3,1,""],VIX_PROPERTY_SNAPSHOT_POWERSTATE:[1,3,1,""],VIX_PROPERTY_VM_ENCRYPTION_PASSWORD:[1,3,1,""],VIX_PROPERTY_VM_GUESTOS:[1,3,1,""],VIX_PROPERTY_VM_IN_VMTEAM:[1,3,1,""],VIX_PROPERTY_VM_IS_RUNNING:[1,3,1,""],VIX_PROPERTY_VM_MEMORY_SIZE:[1,3,1,""],VIX_PROPERTY_VM_NAME:[1,3,1,""],VIX_PROPERTY_VM_NUM_VCPUS:[1,3,1,""],VIX_PROPERTY_VM_POWER_STATE:[1,3,1,""],VIX_PROPERTY_VM_READ_ONLY:[1,3,1,""],VIX_PROPERTY_VM_SSL_ERROR:[1,3,1,""],VIX_PROPERTY_VM_SUPPORTED_FEATURES:[1,3,1,""],VIX_PROPERTY_VM_TOOLS_STATE:[1,3,1,""],VIX_PROPERTY_VM_VMTEAM_PATHNAME:[1,3,1,""],VIX_PROPERTY_VM_VMX_PATHNAME:[1,3,1,""],get_error:[1,4,1,""],get_properties:[1,4,1,""],is_done:[1,4,1,""],wait:[1,4,1,""]},"vix.VixSnapshot":{get_child:[1,4,1,""],get_num_children:[1,4,1,""],get_parent:[1,4,1,""]},"vix.VixVM":{VIX_CAPTURESCREENFORMAT_PNG:[1,3,1,""],VIX_CAPTURESCREENFORMAT_PNG_NOCOMPRESS:[1,3,1,""],VIX_CLONETYPE_FULL:[1,3,1,""],VIX_CLONETYPE_LINKED:[1,3,1,""],VIX_GUEST_ENVIRONMENT_VARIABLE:[1,3,1,""],VIX_INSTALLTOOLS_AUTO_UPGRADE:[1,3,1,""],VIX_INSTALLTOOLS_MOUNT_TOOLS_INSTALLER:[1,3,1,""],VIX_INSTALLTOOLS_RETURN_IMMEDIATELY:[1,3,1,""],VIX_LOGIN_IN_GUEST_REQUIRE_INTERACTIVE_ENVIRONMENT:[1,3,1,""],VIX_POWERSTATE_BLOCKED_ON_MSG:[1,3,1,""],VIX_POWERSTATE_PAUSED:[1,3,1,""],VIX_POWERSTATE_POWERED_OFF:[1,3,1,""],VIX_POWERSTATE_POWERED_ON:[1,3,1,""],VIX_POWERSTATE_POWERING_OFF:[1,3,1,""],VIX_POWERSTATE_POWERING_ON:[1,3,1,""],VIX_POWERSTATE_RESETTING:[1,3,1,""],VIX_POWERSTATE_RESUMING:[1,3,1,""],VIX_POWERSTATE_SUSPENDED:[1,3,1,""],VIX_POWERSTATE_SUSPENDING:[1,3,1,""],VIX_POWERSTATE_TOOLS_RUNNING:[1,3,1,""],VIX_RUNPROGRAM_ACTIVATE_WINDOW:[1,3,1,""],VIX_RUNPROGRAM_RETURN_IMMEDIATELY:[1,3,1,""],VIX_SHAREDFOLDER_WRITE_ACCESS:[1,3,1,""],VIX_SNAPSHOT_INCLUDE_MEMORY:[1,3,1,""],VIX_SNAPSHOT_REMOVE_CHILDREN:[1,3,1,""],VIX_TOOLSSTATE_NOT_INSTALLED:[1,3,1,""],VIX_TOOLSSTATE_RUNNING:[1,3,1,""],VIX_TOOLSSTATE_UNKNOWN:[1,3,1,""],VIX_VMDELETE_DISK_FILES:[1,3,1,""],VIX_VMPOWEROP_FROM_GUEST:[1,3,1,""],VIX_VMPOWEROP_LAUNCH_GUI:[1,3,1,""],VIX_VMPOWEROP_NORMAL:[1,3,1,""],VIX_VMPOWEROP_START_VM_PAUSED:[1,3,1,""],VIX_VMPOWEROP_SUPPRESS_SNAPSHOT_POWERON:[1,3,1,""],VIX_VM_CONFIG_RUNTIME_ONLY:[1,3,1,""],VIX_VM_GUEST_VARIABLE:[1,3,1,""],VIX_VM_SUPPORT_HARDWARE_UPGRADE:[1,3,1,""],VIX_VM_SUPPORT_MULTIPLE_SNAPSHOTS:[1,3,1,""],VIX_VM_SUPPORT_SHARED_FOLDERS:[1,3,1,""],VIX_VM_SUPPORT_TOOLS_INSTALL:[1,3,1,""],add_shared_folder:[1,4,1,""],capture_screen_image:[1,4,1,""],clone:[1,4,1,""],copy_guest_to_host:[1,4,1,""],copy_host_to_guest:[1,4,1,""],create_directory:[1,4,1,""],create_snapshot:[1,4,1,""],create_temp:[1,4,1,""],dir_delete:[1,4,1,""],dir_exists:[1,4,1,""],dir_list:[1,4,1,""],file_delete:[1,4,1,""],file_exists:[1,4,1,""],file_rename:[1,4,1,""],get_file_info:[1,4,1,""],get_shared_folder_count:[1,4,1,""],get_shared_folder_state:[1,4,1,""],install_tools:[1,4,1,""],login:[1,4,1,""],logout:[1,4,1,""],pause:[1,4,1,""],power_off:[1,4,1,""],power_on:[1,4,1,""],proc_kill:[1,4,1,""],proc_list:[1,4,1,""],proc_run:[1,4,1,""],reset:[1,4,1,""],run_script:[1,4,1,""],share_enable:[1,4,1,""],share_remove:[1,4,1,""],share_set_state:[1,4,1,""],snapshot_get_current:[1,4,1,""],snapshot_get_named:[1,4,1,""],snapshot_get_root:[1,4,1,""],snapshot_remove:[1,4,1,""],snapshot_revert:[1,4,1,""],snapshots_get_root_count:[1,4,1,""],suspend:[1,4,1,""],unpause:[1,4,1,""],upgrade_virtual_hardware:[1,4,1,""],var_read:[1,4,1,""],var_write:[1,4,1,""],vm_delete:[1,4,1,""],wait_for_tools:[1,4,1,""]},vix:{VixError:[1,2,1,""],VixHost:[1,0,1,""],VixSnapshot:[1,0,1,""],VixVM:[1,0,1,""]}},objnames:{"0":["py","class","Python class"],"1":["py","staticmethod","Python static method"],"2":["py","exception","Python exception"],"3":["py","attribute","Python attribute"],"4":["py","method","Python method"]},objtypes:{"0":"py:class","1":"py:staticmethod","2":"py:exception","3":"py:attribute","4":"py:method"},terms:{"byte":1,"class":0,"function":1,"import":0,"int":1,"new":1,"return":1,"static":1,"true":1,"try":0,_get_vix_path:1,abl:1,about:1,activ:1,add:1,add_ref:1,add_shared_fold:1,all:1,allow:1,allow_writ:1,ani:1,any:1,api:0,architectur:1,arg:1,argument:1,assertionerror:1,associ:1,authent:1,auto:1,auto_upgrad:1,base:1,between:1,binari:1,block:1,bool:1,captur:1,capture_screen_imag:1,caus:1,check:1,child:1,child_index:1,children:1,citeria:1,clone:1,close:1,cmd:1,com:0,command:1,command_lin:1,complet:1,configur:1,connect:[0,1],constant:1,contain:1,context:1,copi:1,copy_guest_to_host:1,copy_host_to_guest:1,count:1,crash:1,creat:1,create_directori:1,create_snapshot:[0,1],create_temp:1,credenti:1,current:1,dealt:1,debug:1,decreas:1,delet:1,delete_fil:1,demo:0,descript:1,design:1,desir:1,dest_vm:1,dest_vmx:1,dir:1,dir_delet:1,dir_exist:1,dir_list:1,directli:1,directori:1,directorylistentri:1,disabl:1,disconnect:1,disk:1,dll:1,each:1,enabl:1,end:1,env:1,environ:1,error:1,error_cod:1,errors:1,exampl:0,except:[0,1],exception:1,exclus:1,execut:1,exist:1,exit:1,expect:1,expir:1,fail:[0,1],failur:1,fals:1,feel:0,fetch:1,ffi:1,file:1,file_delet:1,file_exist:1,file_renam:1,find:1,find_item:1,folder:1,forev:1,form:1,format:0,found:1,free:0,from:[0,1],from_guest:1,full:1,further:1,get:1,get_child:1,get_error:1,get_file_info:1,get_num_children:1,get_par:1,get_properti:1,get_shared_folder_count:1,get_shared_folder_st:1,get_typ:1,github:0,give:1,given:1,guest:1,guest_path:1,gui:1,handl:1,hardwar:1,here:1,host:[0,1],host_path:1,hostnam:1,http:0,imag:1,immedi:1,immediatli:1,includ:1,include_memori:1,increas:1,index:[0,1],info:1,inform:1,initi:1,instal:1,install_tool:1,instanc:1,interact:1,internal:0,interpret:1,interpreter_path:1,is_don:1,is_valid:1,issu:0,item:1,job:1,just:0,kill:1,kwarg:1,launch:1,launch_gui:1,librari:1,line:1,link:1,list:1,locat:1,login:1,logout:1,machin:1,made:0,mai:1,match:1,method:1,methoid:1,mod:1,modifi:1,modul:[0,1],more:1,mount:1,must:1,mutual:1,naim94a:0,name:1,neg:1,new_nam:1,none:1,normal:1,notimplement:1,number:1,object:1,off:1,old_nam:1,open:1,open_vm:[0,1],oper:1,operat:0,option:1,optional:1,other:1,otherwis:1,othwerwis:1,own:1,owner:1,packag:0,page:0,paramet:1,parent:1,pass:1,password:1,path:1,paus:1,pid:1,png:1,port:1,power:1,power_off:1,power_on:1,previou:1,print:0,proc_kil:1,proc_list:1,proc_run:1,process:1,product:1,program:1,program_nam:1,project:0,properti:1,pull:0,rais:1,ram:1,read:1,recogn:1,refcount:1,regist:1,register_vm:1,releas:1,remov:1,remove_children:1,renam:1,repres:1,represnt:1,request:[0,1],requir:1,require_interact:1,reset:1,result:1,resum:1,retreiv:1,retriev:1,retriv:1,revert:1,revet:1,right:1,root:1,run_script:1,screenshot:1,script:1,script_text:1,search:0,search_typ:1,second:1,servic:1,service_provid:1,session:1,set:1,share:1,share_en:1,share_nam:1,share_remov:1,share_set_st:1,sharedfold:1,should_block:1,shouldn:1,size:1,snapshot:[0,1],snapshot_get_curr:1,snapshot_get_nam:1,snapshot_get_root:1,snapshot_remov:1,snapshot_revert:1,snapshots_get_root_count:1,specifi:1,start:1,state:1,store:1,str:1,str_result_types:1,string:1,submit:0,support:1,suspend:1,symlink:1,temporari:1,test:0,than:1,thi:[0,1],till:1,time:1,timeout:1,todai:0,too:1,tool:1,tupl:1,type:1,unoffici:0,unpaus:1,unregist:1,unregister_vm:1,until:1,upgrad:1,upgrade:1,upgrade_virtual_hardwar:1,usernam:1,using:1,valid:1,valu:1,var_read:1,var_writ:1,variabl:1,variable_typ:1,virtual:1,vix_api_version:1,vix_async:1,vix_capturescreenformat_png:1,vix_capturescreenformat_png_nocompress:1,vix_clonetype_full:1,vix_clonetype_linked:1,vix_e_already_exists:1,vix_e_anon_guest_operations_prohibited:1,vix_e_argument_too_big:1,vix_e_async_mixedmode_unsupported:1,vix_e_authentication_fail:1,vix_e_bad_vm_index:1,vix_e_buffer_toosmall:1,vix_e_cancelled:1,vix_e_cannot_authenticate_with_guest:1,vix_e_cannot_connect_to_host:1,vix_e_cannot_connect_to_vm:1,vix_e_cannot_power_on_vm:1,vix_e_cannot_read_vm_config:1,vix_e_cannot_start_read_only_vm:1,vix_e_console_guest_operations_prohibited:1,vix_e_crypto_bad_buffer_size:1,vix_e_crypto_bad_format:1,vix_e_crypto_bad_password:1,vix_e_crypto_empty:1,vix_e_crypto_error:1,vix_e_crypto_invalid_operation:1,vix_e_crypto_keysafe_locator:1,vix_e_crypto_locked:1,vix_e_crypto_need_password:1,vix_e_crypto_no_crypto:1,vix_e_crypto_not_in_dictionary:1,vix_e_crypto_random_device:1,vix_e_crypto_unknown_algorithm:1,vix_e_disk_attach_rootlink:1,vix_e_disk_cantrepair:1,vix_e_disk_cantshrink:1,vix_e_disk_capacity_mismatch:1,vix_e_disk_cid_mismatch:1,vix_e_disk_encoding:1,vix_e_disk_full:1,vix_e_disk_inval:1,vix_e_disk_invalid_connection:1,vix_e_disk_invalidchain:1,vix_e_disk_invaliddisk:1,vix_e_disk_invalidpartitiontable:1,vix_e_disk_key_notfound:1,vix_e_disk_needkey:1,vix_e_disk_needsrepair:1,vix_e_disk_needvmfs:1,vix_e_disk_nodevice:1,vix_e_disk_noinit:1,vix_e_disk_noio:1,vix_e_disk_nokey:1,vix_e_disk_nokeyoverride:1,vix_e_disk_nolicense:1,vix_e_disk_notencdesc:1,vix_e_disk_notencrypted:1,vix_e_disk_notnormal:1,vix_e_disk_notsupported:1,vix_e_disk_openparent:1,vix_e_disk_outofrange:1,vix_e_disk_parent_notallowed:1,vix_e_disk_partialchain:1,vix_e_disk_partmismatch:1,vix_e_disk_rawtoobig:1,vix_e_disk_rawtoosmall:1,vix_e_disk_subsystem_init_fail:1,vix_e_disk_toomanyopenfiles:1,vix_e_disk_toomanyredo:1,vix_e_disk_unsupporteddevice:1,vix_e_disk_unsupporteddiskversion:1,vix_e_duplicate_name:1,vix_e_empty_password_not_allowed_in_guest:1,vix_e_fail:1,vix_e_file_access_error:1,vix_e_file_already_exists:1,vix_e_file_already_locked:1,vix_e_file_error:1,vix_e_file_name_invalid:1,vix_e_file_name_too_long:1,vix_e_file_not_found:1,vix_e_file_read_only:1,vix_e_file_too_big:1,vix_e_guest_operations_prohibited:1,vix_e_guest_user_permissions:1,vix_e_guest_volumes_not_frozen:1,vix_e_host_connection_lost:1,vix_e_host_disk_invalid_value:1,vix_e_host_disk_sectorsize:1,vix_e_host_file_error_eof:1,vix_e_host_nbd_hashfile_init:1,vix_e_host_nbd_hashfile_volume:1,vix_e_host_netblkdev_handshake:1,vix_e_host_network_conn_refused:1,vix_e_host_not_connected:1,vix_e_host_server_not_found:1,vix_e_host_socket_creation_error:1,vix_e_host_tcp_conn_lost:1,vix_e_host_tcp_socket_error:1,vix_e_host_user_permissions:1,vix_e_incorrect_file_type:1,vix_e_interactive_session_not_present:1,vix_e_interactive_session_user_mismatch:1,vix_e_invalid_arg:1,vix_e_invalid_authentication_session:1,vix_e_invalid_handle:1,vix_e_invalid_hostname_specification:1,vix_e_invalid_message_body:1,vix_e_invalid_message_header:1,vix_e_invalid_property_value:1,vix_e_invalid_serialized_data:1,vix_e_invalid_utf8_string:1,vix_e_invalid_xml:1,vix_e_license:1,vix_e_login_type_not_supported:1,vix_e_missing_anon_guest_account:1,vix_e_missing_required_property:1,vix_e_mntapi_already_opened:1,vix_e_mntapi_cant_make_var_dir:1,vix_e_mntapi_cant_read_parts:1,vix_e_mntapi_codeconversion:1,vix_e_mntapi_create_partitiontable_error:1,vix_e_mntapi_daemon:1,vix_e_mntapi_dict:1,vix_e_mntapi_dict_locked:1,vix_e_mntapi_disk_cant_open:1,vix_e_mntapi_disk_is_mounted:1,vix_e_mntapi_disk_not_found:1,vix_e_mntapi_disk_not_mounted:1,vix_e_mntapi_disk_not_safe:1,vix_e_mntapi_drive_letter_already_assigned:1,vix_e_mntapi_drive_letter_in_use:1,vix_e_mntapi_format_failure:1,vix_e_mntapi_getfile_error:1,vix_e_mntapi_incompatible_version:1,vix_e_mntapi_internal:1,vix_e_mntapi_item_not_found:1,vix_e_mntapi_loop_failed:1,vix_e_mntapi_mountpt_in_use:1,vix_e_mntapi_mountpt_not_found:1,vix_e_mntapi_no_connection_details:1,vix_e_mntapi_no_driver:1,vix_e_mntapi_no_mountable_partitons:1,vix_e_mntapi_no_root:1,vix_e_mntapi_open_failure:1,vix_e_mntapi_open_handles:1,vix_e_mntapi_os_error:1,vix_e_mntapi_partition_not_found:1,vix_e_mntapi_partition_range:1,vix_e_mntapi_perm:1,vix_e_mntapi_putfile_error:1,vix_e_mntapi_reg_not_opened:1,vix_e_mntapi_regdelkey_error:1,vix_e_mntapi_regwrite_error:1,vix_e_mntapi_system:1,vix_e_mntapi_umount:1,vix_e_mntapi_umount_app_not_found:1,vix_e_mntapi_unsupported_ft_volume:1,vix_e_mntapi_unsupproted_boot_loader:1,vix_e_mntapi_unsupproted_os:1,vix_e_mntapi_volume_already_mounted:1,vix_e_mntapi_volume_not_mounted:1,vix_e_mntapi_volume_not_writable:1,vix_e_must_be_console_user:1,vix_e_need_key:1,vix_e_net_http_couldnt_connect:1,vix_e_net_http_couldnt_resolve_host:1,vix_e_net_http_couldnt_resolve_proxy:1,vix_e_net_http_generic:1,vix_e_net_http_http_returned_error:1,vix_e_net_http_operation_timedout:1,vix_e_net_http_ssl_connect_error:1,vix_e_net_http_ssl_security:1,vix_e_net_http_too_many_redirects:1,vix_e_net_http_transfer:1,vix_e_net_http_unsupported_protocol:1,vix_e_net_http_url_malformat:1,vix_e_no_display_server:1,vix_e_no_guest_os_installed:1,vix_e_no_such_process:1,vix_e_not_a_directory:1,vix_e_not_a_file:1,vix_e_not_for_remote_host:1,vix_e_not_found:1,vix_e_not_supported:1,vix_e_not_supported_for_vm_version:1,vix_e_not_supported_on_handle_type:1,vix_e_not_supported_on_remote_object:1,vix_e_object_is_busy:1,vix_e_object_not_found:1,vix_e_op_not_supported_on_guest:1,vix_e_operation_already_in_progress:1,vix_e_operation_disabled:1,vix_e_operation_not_allowed_for_login_type:1,vix_e_out_of_memory:1,vix_e_powerop_scripts_not_available:1,vix_e_program_not_started:1,vix_e_property_type_mismatch:1,vix_e_read_only_property:1,vix_e_requires_large_files:1,vix_e_root_guest_operations_prohibited:1,vix_e_screen_capture_bad_format:1,vix_e_screen_capture_compression_fail:1,vix_e_screen_capture_error:1,vix_e_screen_capture_large_data:1,vix_e_snapshot_checkpoint:1,vix_e_snapshot_config:1,vix_e_snapshot_disklib:1,vix_e_snapshot_disklocked:1,vix_e_snapshot_dumper:1,vix_e_snapshot_duplicateddisk:1,vix_e_snapshot_exists:1,vix_e_snapshot_hierarchy_toodeep:1,vix_e_snapshot_inconsistent:1,vix_e_snapshot_independentdisk:1,vix_e_snapshot_inval:1,vix_e_snapshot_locked:1,vix_e_snapshot_maxsnapshots:1,vix_e_snapshot_memory_on_independent_disk:1,vix_e_snapshot_min_free_space:1,vix_e_snapshot_nametoolong:1,vix_e_snapshot_nochange:1,vix_e_snapshot_nonunique_name:1,vix_e_snapshot_noperm:1,vix_e_snapshot_not_revertable:1,vix_e_snapshot_notfound:1,vix_e_snapshot_version:1,vix_e_snapshot_vixfile:1,vix_e_suspend_error:1,vix_e_template_vm:1,vix_e_timeout_waiting_for_tools:1,vix_e_too_many_handles:1,vix_e_too_many_logons:1,vix_e_tools_install_already_up_to_date:1,vix_e_tools_install_auto_not_supported:1,vix_e_tools_install_cancelled:1,vix_e_tools_install_device_not_connected:1,vix_e_tools_install_error:1,vix_e_tools_install_guest_not_ready:1,vix_e_tools_install_image_copy_failed:1,vix_e_tools_install_image_inaccesible:1,vix_e_tools_install_in_progress:1,vix_e_tools_install_init_failed:1,vix_e_tools_install_no_device:1,vix_e_tools_install_no_image:1,vix_e_tools_not_running:1,vix_e_type_mismatch:1,vix_e_unfinished_job:1,vix_e_unrecognized_command:1,vix_e_unrecognized_command_in_guest:1,vix_e_unrecognized_property:1,vix_e_vm_already_loaded:1,vix_e_vm_already_up_to_date:1,vix_e_vm_host_disconnected:1,vix_e_vm_insufficient_host_memory:1,vix_e_vm_is_running:1,vix_e_vm_not_enough_cpus:1,vix_e_vm_not_found:1,vix_e_vm_not_running:1,vix_e_vm_unsupported_guest:1,vix_e_vmdb:1,vix_e_vmx_msg_dialog_and_no_ui:1,vix_e_wrapper_multiple_serviceproviders:1,vix_e_wrapper_player_not_installed:1,vix_e_wrapper_runtime_not_installed:1,vix_e_wrapper_serviceprovider_not_found:1,vix_e_wrapper_version_not_found:1,vix_e_wrapper_workstation_not_installed:1,vix_file_attributes_directory:1,vix_file_attributes_symlink:1,vix_find_:1,vix_find_registered_vms:1,vix_find_running_vms:1,vix_guest_environment_variable:1,vix_handletype_:1,vix_handletype_host:1,vix_handletype_job:1,vix_handletype_metadata_container:1,vix_handletype_network:1,vix_handletype_none:1,vix_handletype_property_list:1,vix_handletype_snapshot:1,vix_handletype_vm:1,vix_hostoption_verify_ssl_cert:1,vix_installtools_auto_upgrade:1,vix_installtools_mount_tools_installer:1,vix_installtools_return_immediately:1,vix_invalid_handle:1,vix_login_in_guest_require_interactive_environment:1,vix_ok:1,vix_powerstate_blocked_on_msg:1,vix_powerstate_paused:1,vix_powerstate_powered_off:1,vix_powerstate_powered_on:1,vix_powerstate_powering_off:1,vix_powerstate_powering_on:1,vix_powerstate_resetting:1,vix_powerstate_resuming:1,vix_powerstate_suspended:1,vix_powerstate_suspending:1,vix_powerstate_tools_running:1,vix_property_found_item_location:1,vix_property_guest_sharedfolders_shares_path:1,vix_property_host_api_version:1,vix_property_host_hosttype:1,vix_property_host_software_version:1,vix_property_job_result_:1,vix_property_job_result_command_output:1,vix_property_job_result_error_code:1,vix_property_job_result_exit_code:1,vix_property_job_result_extra_error_info:1,vix_property_job_result_file_flags:1,vix_property_job_result_file_mod_time:1,vix_property_job_result_file_size:1,vix_property_job_result_found_item_description:1,vix_property_job_result_guest_object_exists:1,vix_property_job_result_guest_program_elapsed_time:1,vix_property_job_result_guest_program_exit_code:1,vix_property_job_result_handle:1,vix_property_job_result_item_name:1,vix_property_job_result_process_being_debugged:1,vix_property_job_result_process_command:1,vix_property_job_result_process_id:1,vix_property_job_result_process_owner:1,vix_property_job_result_process_start_time:1,vix_property_job_result_screen_image_data:1,vix_property_job_result_screen_image_size:1,vix_property_job_result_shared_folder_count:1,vix_property_job_result_shared_folder_flags:1,vix_property_job_result_shared_folder_host:1,vix_property_job_result_user_message:1,vix_property_job_result_vm_in_group:1,vix_property_job_result_vm_variable_string:1,vix_property_meta_data_container:1,vix_property_none:1,vix_property_snapshot_description:1,vix_property_snapshot_displayname:1,vix_property_snapshot_powerstate:1,vix_property_vm_encryption_password:1,vix_property_vm_guestos:1,vix_property_vm_in_vmteam:1,vix_property_vm_is_running:1,vix_property_vm_memory_size:1,vix_property_vm_name:1,vix_property_vm_num_vcpus:1,vix_property_vm_power_state:1,vix_property_vm_read_only:1,vix_property_vm_ssl_error:1,vix_property_vm_supported_features:1,vix_property_vm_tools_state:1,vix_property_vm_vmteam_pathname:1,vix_property_vm_vmx_pathname:1,vix_propertytype_any:1,vix_propertytype_blob:1,vix_propertytype_bool:1,vix_propertytype_handle:1,vix_propertytype_int64:1,vix_propertytype_integer:1,vix_propertytype_string:1,vix_runprogram_activate_window:1,vix_runprogram_return_immediately:1,vix_serviceprovider_:1,vix_serviceprovider_default:1,vix_serviceprovider_vmware_player:1,vix_serviceprovider_vmware_server:1,vix_serviceprovider_vmware_vi_server:1,vix_serviceprovider_vmware_workstation:1,vix_serviceprovider_vmware_workstation_shared:1,vix_sharedfolder_write_access:1,vix_snapshot_include_memory:[0,1],vix_snapshot_remove_children:1,vix_toolsstate_not_installed:1,vix_toolsstate_running:1,vix_toolsstate_unknown:1,vix_vm_config_runtime_only:1,vix_vm_guest_variable:1,vix_vm_support_hardware_upgrade:1,vix_vm_support_multiple_snapshots:1,vix_vm_support_shared_folders:1,vix_vm_support_tools_install:1,vix_vmdelete_disk_files:1,vix_vmpowerop_:1,vix_vmpowerop_from_guest:1,vix_vmpowerop_launch_gui:1,vix_vmpowerop_normal:1,vix_vmpowerop_start_vm_paused:1,vix_vmpowerop_suppress_snapshot_poweron:1,vixbackend:0,vixerror:0,vixhandl:0,vixhost:0,vixjob:0,vixsnapshot:0,vixvm:0,vm_delet:1,vmware:[0,1],vmx:0,vmx_path:1,wait:1,wait_for_tool:1,window:0,write:1,write_access:1,zero:1},titles:["VIX python binding","vix package"],titleterms:{"class":1,bind:0,indice:0,internal:1,packag:1,python:0,tabl:0,vix:[0,1],vixbackend:1,vixerror:1,vixhandl:1,vixhost:1,vixjob:1,vixsnapshot:1,vixvm:1}})