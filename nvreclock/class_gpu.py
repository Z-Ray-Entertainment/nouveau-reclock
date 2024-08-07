from enum import Enum


class PState(Enum):
    OFF = 0
    MIN = 1
    MED = 2
    MAX = 3


class GPU:
    def __init__(self, device_id: str, device_name: str, device_bus_id: str):
        self.device_id = device_id
        self.device_name = device_name
        self.device_current_pstate = PState.MIN
        self.device_bus_id = device_bus_id

    def get_pstates(self):
        pass

    def set_pstate(self, pstate: PState):
        self.device_current_pstate = pstate

    def print_gpu(self):
        print("Name: " + self.device_name + " ID: " + self.device_id + " BUS: " + self.device_bus_id)
