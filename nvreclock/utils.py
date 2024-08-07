import os
import subprocess

from nvreclock.class_gpu import GPU
from nvreclock.const import NVIDIA_VENDOR_ID, DEVICE_CLASS_GPU
from nvreclock.pci_ids import get_name


class PciDeviceInfo:
    def __init__(self, device_uevent_result, bus_id):
        self.bus_id = bus_id
        device_uevent = device_uevent_result.stdout.decode("utf-8").rstrip()
        device_info = device_uevent.split("\n")
        for properties in device_info:
            propety = properties.split("=")
            match propety[0]:
                case "PCI_CLASS":
                    self.pci_class = propety[1]
                case "DRIVER":
                    self.driver = propety[1]
                case "PCI_ID":
                    pci_id = propety[1].split(":")
                    self.vendor = pci_id[0]
                    self.device_id = pci_id[1]

    def get_gpu_device(self):
        if self.vendor == NVIDIA_VENDOR_ID and self.pci_class in DEVICE_CLASS_GPU:
            return GPU(0, self.device_id, get_name(self.device_id), self.bus_id)
        else:
            return None


def find_gpus():
    pci_path = "/sys/bus/pci/devices/"
    for subdir, dirs, files in os.walk(pci_path):
        for device in dirs:
            device_uevent_result = subprocess.run(["cat", pci_path + device + "/uevent"], stdout=subprocess.PIPE)
            pci_device_info = PciDeviceInfo(device_uevent_result, device)
            gpu_device: GPU = pci_device_info.get_gpu_device()
            if gpu_device is not None:
                gpu_device.print_gpu()


find_gpus()
