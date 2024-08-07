supported_device_matrix = {
    "1290": "GT 730M"
}


def is_supported(device_id: str):
    return False


def get_name(device_id: str):
    return supported_device_matrix[device_id]
