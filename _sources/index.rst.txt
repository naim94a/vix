.. toctree::
    :maxdepth: 2
    :hidden:

    installation
    tutorials
    vix

VIX Python binding
==================

An unofficial object oriented python binding for `VMware's VIX API`_.

Features
--------

- Control a VMs power state, and get the current state.
- Manage Snapshots: Create, modify, delete.
- Create screenshots of guest VMs.
- Clone VMs - either full or linked.
- Execute on guests

  - Run commands and scripts
  - List and delete files or processes

- Manage sharing folders with guests.

This wrapper should cover the full VIX API of VMware. If it doesn't, please
`create an issue`_.

License
-------

VIX is released under the GPLv3_ license.

.. _VMware's VIX API: https://www.vmware.com/support/developer/vix-api/
.. _GPLv3: https://github.com/naim94a/vix/blob/master/LICENSE.txt
.. _create an issue: https://github.com/naim94a/vix/issues/new
