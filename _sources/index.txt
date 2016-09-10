.. vix documentation master file, created by
   sphinx-quickstart on Sat Sep 10 21:29:58 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

VIX python binding
==================

This is an unofficial binding of VMware's VIX API.

The VIX project is hosted on GitHub: https://github.com/naim94a/vix.
Feel free to submit pull requests and issues.

Example:

.. code-block:: python
	:caption: snapshot-demo.py

	from vix import VixHost, VixError
	from vix.VixVM import VIX_SNAPSHOT_INCLUDE_MEMORY

	host = VixHost()
	host.connect()

	try:
		vm = host.open_vm(r'~/Windows 7.vmx')

		snapshot = vm.create_snapshot(
			'Todays Snapshot', 
			'Just testing vix', 
			VIX_SNAPSHOT_INCLUDE_MEMORY
		)

		print("Made snapshot!")

	except VixError as ex:
		print("Operatation failed: {0}".format(ex))

API:

.. toctree::
   :maxdepth: 4

   vix


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

