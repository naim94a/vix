# Vix wrapper
VMware's [VIX](https://www.vmware.com/support/developer/vix-api/) library can be really useful if you wan't to automate VM operations. This project was written to provide an Object-Oriented interface with the VIX API.

Tested with VMware Workstation, this wrapper should support ESXs, VMware servers and other VMware products.

## Features
* Written for Python3, it should support Python2 as well.
* Access VIX API through [cffi](http://cffi.readthedocs.io/en/latest/), thus allowing execution over [pypy](http://pypy.org/).
* Supported operations:
  * Power (turn on, turn off, suspend, etc...)
  * Snapshot control
  * Cloning (both full and linked)
  * Finding powered on VMs (or registered, if your VMware product supports it)
  * Script & command execution on guest.
  * Listing directories & Processes
  * Killing processes
  * Deleting files & directories
  * Control VMs environment
  * Control shares
* Deletion of VMs from host
* Registration and unregistration of VMs from hosts.

## Licenses
vix (this project) is released under the [GPLv3](License) license. 
This projects uses redistributable software developed by VMware.

## Bugs, Features, support
Please submit bug, features and anything else related to the project's issue tracker on GitHub: https://github.com/naim94a/vix/issues.
Pull requests are welcome as well.
