.. vix documentation master file, created by
   sphinx-quickstart on Sat Sep 10 21:29:58 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
    :maxdepth: 2
    :hidden:

    tutorials
    vix

VIX Python binding
==================

This is an unofficial binding of VMware's VIX API.

The VIX project is hosted on GitHub: https://github.com/naim94a/vix.
Feel free to submit pull requests and issues.

About
-----
VIX is a C library created by VMWare, the aim of this project is to wrap it in python.
This project allow Object-Oriented access to various VMWare products.


Installing
----------

.. code-block:: shell

	pip install vix


Example usage
-------------

.. code-block:: python
	:caption: snapshot-demo.py

	from vix import VixHost, VixError

	host = VixHost()
	host.connect()

	try:
		vm = host.open_vm(r'~/Windows 7.vmx')

		snapshot = vm.create_snapshot(
			'Todays Snapshot', 
			'Just testing vix',
			include_memory=True
		)

		print("Made snapshot!")

	except VixError as ex:
		print("Operatation failed: {0}".format(ex))
