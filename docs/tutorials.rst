Tutorial
========

Capturing screens
-----------------
Every wanted to take a screenshot of whats going on in a running VM?
Well, you are in luck! VIX supports taking screenshots, this will require you to know a guest's username/password.

The VIX python binding can return a screenshot in PNG format. You can choose between having the file written to a file, or getting the PNG buffer.

This example will demonstrate how to take screenshots from a VM every 10 seconds.

.. code-block:: python

    import time
    from vix import VixHost

    host = VixHost()
    vm = host.open_vm('/path/to/my/vm.vmx')

    # Must login to do some things...
    vm.login('root', 'toor')
    while True:
        vm.capture_screen_image('/path/to/my/screenshot_{name}_{timestamp:.0f}.png'.format(name=vm.name, timestamp=time.time()))
        time.sleep(10.0)


Cloning Machines
----------------

Cloning machines are usually a more useful action then capturing screenshots. It is a pretty simple task to...

.. code-block:: python

    from vix import VixHost

    host = VixHost()
    vm = host.open_vm('/path/to/my/template/vm.vmx')

    # Assuming that template.vmx is currently on a powered off snapshot.
    snapshot = vm.snapshot_get_current()

    # This clone will be based of 'template.vmx' at the specified snapshot.
    # Linked snapshots take less space...
    cloned = vm.clone('/path/to/my/cloned/vm.vmx', snapshot=snapshot, linked=True)

    # Let fire up our cloned machine!
    cloned.power_on()
