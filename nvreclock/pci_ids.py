# See: https://nouveau.freedesktop.org/PowerManagement.html
# See: https://nouveau.freedesktop.org/CodeNames.html#NV40

supported_device_matrix = {
    "1003": "GeForce GTX Titan LE", "1004": "GeForce GTX 780", "1005": "GeForce GTX TITAN",
    "1007": "GeForce GTX 780 Rev. 2", "1008": "GeForce GTX 780 Ti 6GB", "1286": "GeForce GT 720",
    "1289": "GeForce GT 710", "1280": "GeForce GT 635", "1281": "GeForce GT 710",
    "1282": "GeForce GT 640 Rev. 2", "1284": "GeForce GT 630 Rev. 2", "11c7": "GeForce GTX 750 Ti",
    "11c8": "GeForce GTX 650 OEM", "11cb": "GeForce GT 740", "11c3": "GeForce GTX 650 Ti OEM",
    "11c4": "GeForce GTX 645 OEM", "11c5": "GeForce GT 740", "11c6": "GeForce GTX 650 Ti",
    "11c0": "GeForce GTX 660", "11c2": "GeForce GTX 650 Ti Boost", "1191": "GeForce GTX 760 Rev. 2",
    "1193": "GeForce GTX 760 Ti OEM", "118e": "GeForce GTX 760 OEM", "1186": "GeForce GTX 660 Ti",
    "1184": "GeForce GTX 770", "1185": "GeForce GTX 660 OEM", "1187": "GeForce GTX 760",
    "1195": "GeForce GTX 660 Rev. 2", "1188": "GeForce GTX 690", "1189": "GeForce GTX 670",
    "118c": "GRID K2 NVS USM", "1180": "GeForce GTX 680", "1182": "GeForce GTX 760 Ti",
    "1183": "GeForce GTX 660 Ti", "0ffd": "NVS 510", "0ff1": "NVS 1000", "0fe5": "GeForce K340 USM",
    "0fe6": "GRID K1 NVS USM", "0fc5": "GeForce GT 1030", "0fc6": "GeForce GTX 650",
    "0fc8": "GeForce GT 740", "0fc9": "GeForce GT 730", "0fc0": "GeForce GT 640 OEM",
    "0fc1": "GeForce GT 640", "0fc2": "GeForce GT 630 OEM", "1287": "GeForce GT 730",
    "1288": "GeForce GT 720", "128b": "GeForce GT 710", "100c": "GeForce GTX TITAN Black",
    "1001": "GeForce GTX TITAN Z", "100a": "GeForce GTX 780 Ti", "128a": "GK208B",
    "128c": "GK208B", "12a0": "GK208",
    "11fa": "Quadro K4000", "11bf": "GRID K2", "11ba": "Quadro K5000",
    "11bb": "Quadro 4100", "11b0": "GRID K240Q / K260Q vGPU", "11b1": "GRID K2 Tesla USM",
    "11b4": "Quadro K4200", "118f": "Tesla K10", "1194": "Tesla K8", "103a": "Quadro K6000",
    "103c": "Quadro K5200", "1022": "Tesla K20c", "118a": "GRID K520",
    "118b": "GRID K2 GeForce USM", "118d": "GRID K200 vGPU", "101e": "Tesla K20X",
    "101f": "Tesla K20", "1020": "Tesla K20X", "1021": "Tesla K20Xm",
    "0fff": "Quadro 410", "102d": "Tesla K80", "1024": "Tesla K40c",
    "1026": "Tesla K20s", "1028": "Tesla K20m", "0ff9": "Quadro K2000D",
    "0ffa": "Quadro K600", "0ffe": "Quadro K2000", "0ff2": "GRID K1",
    "0ff3": "Quadro K420", "0ff5": "GRID K1 Tesla USM", "0ff7": "GRID K140Q vGPU",
    "0fef": "GRID K340", "0fe7": "GRID K100 vGPU", "102e": "Tesla K40d",
    "102f": "Tesla Stella Solo", "1023": "Tesla K40m", "1029": "Tesla K40s",
    "102a": "Tesla K40t", "1027": "Tesla K40st", "103f": "Tesla Stella SXM",
    "1290": "GeForce GT 730M", "1299": "GeForce 920M", "129a": "GeForce 910M",
    "1291": "GeForce GT 735M", "1292": "GeForce GT 740M", "1293": "GeForce GT 730M",
    "1294": "GeForce GT 740M", "1295": "GeForce 710M", "1296": "GeForce 825M",
    "1298": "GeForce GT 720M", "11e2": "GeForce GTX 765M", "11e3": "GeForce GTX 760M",
    "11e0": "GeForce GTX 770M", "11e1": "GeForce GTX 765M", "119f": "GeForce GTX 780M",
    "11a0": "GeForce GTX 680M", "11a1": "GeForce GTX 670MX", "11a2": "GeForce GTX 675MX Mac Edition",
    "1199": "GeForce GTX 870M", "119a": "GeForce GTX 860M", "119d": "GeForce GTX 775M Mac Edition",
    "119e": "GeForce GTX 780M Mac Edition", "11a3": "GeForce GTX 680MX", "11a7": "GeForce GTX 675MX",
    "11a9": "GeForce GTX 870M", "0fe8": "N14P-GS", "0fe9": "GeForce GT 750M Mac Edition",
    "0fd9": "GeForce GT 645M", "0fdf": "GeForce GT 740M", "0fe0": "GeForce GTX 660M Mac Edition",
    "0fe1": "GeForce GT 730M", "0fe2": "GeForce GT 745M", "0fd1": "GeForce GT 650M",
    "0fd2": "GeForce GT 640M", "0fd3": "GeForce GT 640M LE", "0fd4": "GeForce GTX 660M",
    "0fd5": "GeForce GT 650M Mac Edition", "0fd8": "GeForce GT 640M Mac Edition",
    "0fea": "GeForce GT 755M Mac Edition",
    "0fec": "GeForce 710A", "0fed": "GeForce 820M", "0fee": "GeForce 810M", "0fe3": "GeForce GT 745M",
    "0fe4": "GeForce GT 750M", "0fcd": "GeForce GT 755M", "0fce": "GeForce GT 640M LE",
    "1198": "GeForce GTX 880M", "0fdb": "GK107M", "0fd6": "GK107M", "11e7": "GK106M",
    "12b9": "Quadro K610M", "12ba": "Quadro K510M", "11be": "Quadro K3000M",
    "11fc": "Quadro K2100M", "11b6": "Quadro K3100M", "11b7": "Quadro K4100M",
    "11b8": "Quadro K5100M", "11bc": "Quadro K5000M", "11bd": "Quadro K4000M",
    "11af": "GRID IceCube", "11a8": "Quadro K5100M", "0ff8": "Quadro K500M",
    "0ffb": "Quadro K2000M", "0ffc": "Quadro K1000M", "0ff6": "Quadro K1100M", "11b9": "GK104GLM"
}


def is_supported(device_id: str):
    return False


def get_name(device_id: str):
    if device_id in supported_device_matrix:
        return supported_device_matrix[device_id]
    else:
        return "Unknown"