import os
import yaml
import shutil
import platform
from rich import print


class YAMLConfigHelper:
    def __init__(self):
        self.data = None
        self.xdg_config_home = None

        # Get the platform
        self.platform = platform.system().lower()

        if "windows" in self.platform:
            self.full_config_path = os.path.join(
                os.getenv("LOCALAPPDATA"), "proxysqlctl", "proxysqlctl.yaml"
            )
        else:
            if os.getenv("XDG_CONFIG_HOME") is None:
                self.xdg_config_home = os.path.expanduser(os.path.join("~", ".config"))
            else:
                self.xdg_config_home = os.path.expanduser(
                    os.path.join(
                        os.getenv("XDG_CONFIG_HOME"), "proxysqlctl", "proxysqlctl.yaml"
                    )
                )

        self.full_config_path = os.path.join(
            self.xdg_config_home, "proxysqlctl", "proxysqlctl.yaml"
        )

    def install(self):
        cfgsrc = os.path.join("config", "proxysqlctl.yaml")
        cfgdst = self.full_config_path

        if not os.path.exists(self.full_config_path):
            print("This appears to be the first time you've run proxysqlctl.")
            print("  Creating config file.")
            os.makedirs(os.path.dirname(self.full_config_path), exist_ok=True)
            shutil.copyfile(cfgsrc, self.full_config_path)
            print(f"Config file installed to:\n   {cfgdst}\n")
            print("Please edit the config file and re-run this command")
            exit(1)

    def load(self):
        try:
            with open(self.full_config_path, "r") as f:
                self.data = yaml.safe_load(f)
        except FileNotFoundError:
            return None

        return self.data

    def get_instance(self, name):
        return self.data["instances"][f"{name}"]

    def get_default_instance(self):
        instance = self.data["default_instance"]
        return self.data["instances"][f"{instance}"]
