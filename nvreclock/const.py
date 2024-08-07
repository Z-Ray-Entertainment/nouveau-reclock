from os import environ

if environ.get("FLATPAK_ID") is not None:
    VERSION = "@VERSION@"
    LOCALE_DIR = "@localedir@"
else:
    VERSION = "0.dev0"
    LOCALE_DIR = "nvreclock/data/po"
APP_NAME = "Nouveau Re-Clock"
APP_ID = "de.z_ray.Nvreclock"

NVIDIA_VENDOR_ID = "10DE"
DEVICE_CLASS_GPU = "30000" "30200"  # (desktop_gpu mobile_gpu)
DRIVER_ID = "nouveau"
PCI_DEVICE_PATH = "/sys/bus/pci/devices/"
