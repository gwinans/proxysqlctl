from pylib.DatabaseHelper import DatabaseHelper
from pylib.YAMLConfigHelper import YAMLConfigHelper


def main():
    # Load our config
    pxcfg = YAMLConfigHelper()
    # Run the "installer". This will create the config file only if it doesn't exist
    pxcfg.install()
    cfg_yaml = pxcfg.load()

    default_instance = cfg_yaml["instances"][cfg_yaml["default_instance"]]

    print(f"Default instance: {default_instance}")
