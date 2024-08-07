from nvreclock import utils

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
