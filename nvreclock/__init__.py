from nvreclock import utils

if utils.is_kernel_supported():
    utils.find_gpus()
    if len(utils.found_devices) == 0:
        print("No supported devices found")
    else:
        for gpu in utils.found_devices:
            gpu.print_gpu()
else:
    print("Current Kernel is too old. Please update!")