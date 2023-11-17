import os
import yaml
import shutil
from rich import print


class YAMLConfigHelper:
    def __init__(self):
        if os.getenv("XDG_CONFIG_HOME") is not None:
            self.filename = os.path.join(
                os.getenv("XDG_CONFIG_HOME"), "proxysqlctl", "proxysqlctl.yaml"
            )
        else:
            self.filename = os.path.expanduser(
                os.path.join("~", ".config", "proxysqlctl", "proxysqlctl.yaml")
            )
        self.data = None

    def install(self):
        cfgsrc = os.path.join("config", "proxysqlctl.yaml")
        cfgdst = self.filename

        if not os.path.exists(self.filename):
            print("Installing config file")
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            shutil.copyfile(cfgsrc, cfgdst)
            print(f"Config file installed to:\n   {cfgdst}\n")
            print("Please edit the config file and re-run this command")
            exit(1)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                self.data = yaml.safe_load(f)
        except FileNotFoundError:
            return None

        return self.data

    def get_instance(self, name):
        return self.data["instances"][f"{name}"]

    def get_default_instance(self):
        instance = self.data["default_instance"]
        return self.data["instances"][f"{instance}"]
