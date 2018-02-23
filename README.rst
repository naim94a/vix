VIX
===

VIX is a object oriented python wrapper for `VMware's VIX API`_.

Installing
----------

Install and update using `pip`_:

.. code-block:: text

    pip install -U vix

Quick Example
-------------

.. code-block:: python

    from vix import VixHost, VixError
    
    host = VixHost()

    try:
        vm = host.open_vm(r'/home/root/VirtualMachines/Debian/Debian.vmx')
        snapshot = vm.create_snapshot(
            'Testing VIX',
            'Well, this is great!',
            include_memory=True
        )
        print('Snapshot created!')
    except VixError as ex:
        print("Something went wrong :( {0}".format(ex))

Features
--------

The full VIX API was wrapped, some of the supported operations include:

- Power on & power off VMs.
- Manage snapshots (with or without memory)
- Cloning (linked or full)
- Script & Command execution on guests

  - Executing scripts and processes
  - Manage directories, files & processes

- Control VMs environment
- Manage shared folders
- Create screenshot of guest VMs

.. _VMware's VIX API: https://www.vmware.com/support/developer/vix-api/
.. _pip: https://pip.pypa.io/en/stable/quickstart
