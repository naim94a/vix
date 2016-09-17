"""
	vix.tests
	---------

	Tests for the vix library.

	.. warning:: Unit tests may cause data on running VMs to be lost.
"""

import unittest
from vix import VixHost, VixVM, VixSnapshot


class VixHostTest(unittest.TestCase):
	def setUp(self):
		self._conn = VixHost()

	def test_host_info(self):
		host_info = self._conn.host_info

		self.assertIn(host_info.host_type, (
			VixHost.VIX_SERVICEPROVIDER_VMWARE_SERVER,
			VixHost.VIX_SERVICEPROVIDER_VMWARE_WORKSTATION,
			VixHost.VIX_SERVICEPROVIDER_VMWARE_PLAYER,
			VixHost.VIX_SERVICEPROVIDER_VMWARE_VI_SERVER,
			VixHost.VIX_SERVICEPROVIDER_VMWARE_WORKSTATION_SHARED,
		), 'host_type is unknown')

		self.assertIsNot(host_info.api_version, None, 'invalid api_version')
		self.assertIsInstance(host_info.software_version, str, 'software_version is not a string.')

	def test_find_item_names(self):
		items = self._conn.find_items(names_only=True)

		self.assertIsInstance(items, list, 'Expected list')
		self.assertGreater(len(items), 0, 'No VMS running. Cant test...')

		for item in items:
			self.assertIsInstance(item, str, 'Expected string')

	def test_find_item_instances(self):
		items = self._conn.find_items(names_only=False)

		self.assertIsInstance(items, list, 'Expected list')
		self.assertGreater(len(items), 0, 'No VMS running. Cant test...')

		for item in items:
			self.assertIsInstance(item, VixVM, 'Expected VixVM')

	def tearDown(self):
		del self._conn


class BaseVixVMTest(unittest.TestCase):
	def setUp(self):
		self._host = VixHost()
		items = self._host.find_items()
		self._vm = items[0]

		self.assertIsInstance(self._vm, VixVM)


class VixVMTest(BaseVixVMTest):
	def test_properties(self):
		self.assertIsInstance(self._vm.vmx_path, str, 'vmx_path is not a string')
		
		self.assertIsInstance(self._vm.machine_info[0], int, 'num CPUs is not an int')
		self.assertIsInstance(self._vm.machine_info[1], int, 'memory size is not an int')
		self.assertEqual(len(self._vm.machine_info), 2, 'machine_info must be size 2')

		self.assertIsInstance(self._vm.name, str, 'expected str')
		
		self.assertIsInstance(self._vm.guest_os, str, 'expected str')

		self.assertIsInstance(self._vm.is_running, bool, 'expected bool')

		self.assertIsInstance(self._vm.power_state, int)
		self.assertIsInstance(self._vm.tools_state, int)
		self.assertIsInstance(self._vm.supported_features, int)

	def test_pause_unpause(self):
		self._vm.pause()
		self._vm.unpause()

	def test_poweroff_poweron(self):
		self.assertGreater(self._vm.power_state & VixVM.VIX_POWERSTATE_POWERED_ON, 0, 'expected vm to be powered on')
		self._vm.power_off()
		self.assertGreater(self._vm.power_state & VixVM.VIX_POWERSTATE_POWERED_OFF, 0, 'expected vm to be powered off')
		self._vm.power_on()
		self.assertGreater(self._vm.power_state & VixVM.VIX_POWERSTATE_POWERED_ON, 0, 'expected vm to be powered on')

	def test_reset(self):
		self._vm.reset()

	def test_suspend(self):
		self.assertGreater(self._vm.power_state & VixVM.VIX_POWERSTATE_POWERED_ON, 0, 'expected vm to be powered on')
		self._vm.suspend()
		self.assertGreater(self._vm.power_state & VixVM.VIX_POWERSTATE_SUSPENDED, 0, 'expected vm to be suspended')
		self._vm.power_on()
		self.assertGreater(self._vm.power_state & VixVM.VIX_POWERSTATE_POWERED_ON, 0, 'expected vm to be powered on')


class VixVMSnapshotTest(BaseVixVMTest):
	def test_clone_delete(self):
		cloned_vm = self._vm.clone(r'cloned.vmx', snapshot=self._vm.snapshot_get_current(), linked=True)
		self.assertIsInstance(cloned_vm, VixVM)

		cloned_vm.vm_delete(delete_files=True)

	def test_create_remove(self):
		snapshot = self._vm.create_snapshot('Test Snapshot', 'Created By UnitTest', include_memory=False)
		self.assertIsInstance(snapshot, VixSnapshot)

		self.assertIsInstance(snapshot.name, str)
		self.assertIsInstance(snapshot.description, str)
		self.assertIsInstance(snapshot.power_state, int)

		self._vm.snapshot_remove(snapshot)


class VixSnapshotTest(BaseVixVMTest):
	def setUp(self):
		super(VixSnapshotTest, self).setUp()

		self._snapshot = self._vm.snapshot_get_current()
		self.assertIsInstance(self._snapshot, VixSnapshot)

	def test_properties(self):
		self.assertIsInstance(self._snapshot.name, str)
		self.assertIsInstance(self._snapshot.description, str)
		self.assertIsInstance(self._snapshot.power_state, int)

	def test_get_named(self):
		name = self._snapshot.name

		snp = self._vm.snapshot_get_named(name)
		self.assertIsInstance(snp, VixSnapshot)

		self.assertEqual(snp.name, name)

	def test_root(self):
		root = self._vm.snapshot_get_root()
		self.assertIsInstance(root, VixSnapshot)

		self.assertIs(root.get_parent(), None)

	def test_children(self):
		for i in range(self._snapshot.get_num_children()):
			self.assertIsInstance(self._snapshot.get_child(i), VixSnapshot)

if "__main__" == __name__:
	unittest.main()
