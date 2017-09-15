[![PyPI version](https://badge.fury.io/py/vix.svg)](https://badge.fury.io/py/vix)

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
  * Get PNG screenshots of VMs
* Deletion of VMs from host
* Registration and unregistration of VMs from hosts.

## Licenses
vix (this project) is released under the [GPLv3](LICENSE) license. 
This projects uses redistributable software developed by VMware.

## Bugs, Features, support
Please reffer to [CONTRIBUTING](CONTRIBUTING.md).

## Donations
Please send donations to us via BitCoin:1GWpPGLai6hbEi7cMhsA4cNkp9e86W9E7q
