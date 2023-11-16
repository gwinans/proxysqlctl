from pylib.DatabaseHelper import DatabaseHelper
from pylib.YAMLConfigHelper import YAMLConfigHelper


def main():
    # Load our config
    pxyml = YAMLConfigHelper()
    # Run the "installer". This will create the config file only if it doesn't exist
    pxyml.install()
    # Load the config file
    pxcfg = pxyml.load()

    default_instance = pxcfg["instances"][pxcfg["default_instance"]]

    print(f"Default instance: {default_instance}")
