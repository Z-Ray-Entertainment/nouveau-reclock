from os import environ

if environ.get("FLATPAK_ID") is not None:
    VERSION = "@VERSION@"
    LOCALE_DIR = "@localedir@"
else:
    VERSION = "0.dev0"
    LOCALE_DIR = "nvreclock/data/po"
APP_NAME = "Nouveau Reclock"
APP_ID = "de.z_ray.Nvreclock"
