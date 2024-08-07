#!/usr/bin/env python3
import sys

from os import environ

pkgdatadir = '@pkgdatadir@'
if environ.get("FLATPAK_ID") is not None:
    sys.path.insert(1, pkgdatadir)
    print(pkgdatadir)

from nvreclock import utils
from nvreclock.const import APP_ID
from nvreclock.main_ui import NouveauReClock

if utils.is_kernel_supported():
    utils.find_gpus()
    if len(utils.found_devices) == 0:
        print("No supported devices found.")
        print("If you believe this to be an error here is a complete list off all GPUs found in this system:\n")
        for pci_device in utils.all_gpus:
            print("################################################")
            pci_device.print_pci_device()
        print("\nPlease report this to the developers of this application")
    else:
        for gpu in utils.found_devices:
            gpu.print_gpu()
else:
    print("Current Kernel is too old. Please update!")

if __name__ == '__main__':
    NouveauReClock(application_id=APP_ID).run(sys.argv)
