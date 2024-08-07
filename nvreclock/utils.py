import os
import subprocess

from nvreclock.class_gpu import GPU
from nvreclock.const import NVIDIA_VENDOR_ID, DEVICE_CLASS_GPU, PCI_DEVICE_PATH
from nvreclock.pci_ids import get_name, is_supported


# DRIVER=nouveau
# PCI_CLASS=30200
# PCI_ID=10DE:1290
# PCI_SUBSYS_ID=1462:10B8
# PCI_SLOT_NAME=0000:01:00.0
# MODALIAS=pci:v000010DEd00001290sv00001462sd000010B8bc03sc02i00
class PciDeviceInfo:
    def __init__(self, device_uevent_result):
        device_uevent = device_uevent_result.stdout.decode("utf-8").rstrip()
        device_info = device_uevent.split("\n")
        for properties in device_info:
            property = properties.split("=")

            match property[0]:
                case "PCI_CLASS":
                    self.pci_class = property[1]
                case "DRIVER":
                    self.driver = property[1]
                case "PCI_ID":
                    pci_id = property[1].split(":")
                    self.vendor = pci_id[0]
                    self.device_id = pci_id[1]
                case "PCI_SLOT_NAME":
                    self.bus_id = property[1]

    def get_gpu_device(self):
        if self.vendor == NVIDIA_VENDOR_ID and self.pci_class in DEVICE_CLASS_GPU and is_supported(self.device_id):
            return GPU(0, self.device_id, get_name(self.device_id), self.bus_id)
        else:
            return None


def find_gpus():
    for subdir, dirs, files in os.walk(PCI_DEVICE_PATH):
        for device in dirs:
            device_uevent_result = subprocess.run(["cat", PCI_DEVICE_PATH + device + "/uevent"], stdout=subprocess.PIPE)
            pci_device_info = PciDeviceInfo(device_uevent_result, )
            gpu_device: GPU = pci_device_info.get_gpu_device()
            if gpu_device is not None:
                gpu_device.print_gpu()


find_gpus()
