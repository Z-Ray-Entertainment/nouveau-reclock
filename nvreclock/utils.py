import os
import subprocess

from nvreclock.class_gpu import GPU
from nvreclock.const import NVIDIA_VENDOR_ID, DEVICE_CLASS_GPU, PCI_DEVICE_PATH, DRIVER_ID
from nvreclock.pci_ids import get_name, is_supported
from packaging.version import Version

found_devices = []


class PciDeviceInfo:
    """
    PciDeviceInfo Helper class build using uevent
    A typical uevent looks like:
    DRIVER=nouveau -> This is the driver in use for this device
    PCI_CLASS=30200 -> This tells what kind of pci device this is. Desktop GPU Mobile GPU, Wi-Fi Card, Sound card etc.
    PCI_ID=10DE:1290 -> VENDOR_ID:DEVICE_ID as hex values
    PCI_SUBSYS_ID=1462:10B8 -> IDK
    PCI_SLOT_NAME=0000:01:00.0 -> PCI bus id. This tells where and how this device is connected to the CPU
    MODALIAS=pci:v000010DEd00001290sv00001462sd000010B8bc03sc02i00 -> IDK
    """

    def __init__(self, device_uevent_result):
        device_uevent = device_uevent_result.stdout.decode("utf-8").rstrip()
        device_info = device_uevent.split("\n")
        for properties in device_info:
            prop = properties.split("=")

            match prop[0]:
                case "PCI_CLASS":
                    self.pci_class = prop[1]
                case "DRIVER":
                    self.driver = prop[1]
                case "PCI_ID":
                    pci_id = prop[1].split(":")
                    self.vendor = pci_id[0]
                    self.device_id = pci_id[1]
                case "PCI_SLOT_NAME":
                    self.bus_id = prop[1]

    def get_gpu_device(self):
        """
        Returns the current PCI device as a GPU device if it is supported.
        """
        if self.vendor == NVIDIA_VENDOR_ID and self.pci_class in DEVICE_CLASS_GPU and is_supported(
                self.device_id) and self.driver == DRIVER_ID:
            return GPU(0, self.device_id, get_name(self.device_id), self.bus_id)
        else:
            return None


def is_kernel_supported():
    uname_result = subprocess.run(["uname", "-r"], stdout=subprocess.PIPE)
    uname = uname_result.stdout.decode("utf-8").rstrip().split("-")[0]
    return Version("4.5") <= Version(uname)


def find_gpus():
    """
    Iterates over all pci devices and collects supported GPUs in found_devices
    """
    for subdir, dirs, files in os.walk(PCI_DEVICE_PATH):
        for device in dirs:
            device_uevent_result = subprocess.run(["cat", PCI_DEVICE_PATH + device + "/uevent"], stdout=subprocess.PIPE)
            pci_device_info = PciDeviceInfo(device_uevent_result, )
            gpu_device: GPU = pci_device_info.get_gpu_device()
            if gpu_device is not None:
                found_devices.append(gpu_device)

