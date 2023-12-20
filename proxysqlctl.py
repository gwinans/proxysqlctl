from rich import print
from pylib.YAMLConfigHelper import YAMLConfigHelper
from pylib.GenericHelper import GenericHelper

def startup():
    # globals are usually bad, but this use-case makes sense ( to me )
    global pxcfg
    global dbconfig
    global default_instance

    # Load our config
    pxyml = YAMLConfigHelper()

    # Run the "installer". This will create the config file only if it doesn't exist
    pxyml.install()

    # Load the config file
    pxcfg = pxyml.load()

    default_instance = pxcfg["default_instance"]
    dbconfig = {
        "host": pxcfg["instances"][default_instance]["hostname"],
        "user": pxcfg["instances"][default_instance]["username"],
        "password": pxcfg["instances"][default_instance]["password"],
        "db": "proxysql",
    }


def main():
    print("You will be connecting to the following instance:")
    print(f"   {default_instance}")

    GenericHelper.yesno("Is this correct?")

if __name__ == "__main__":
    main()
