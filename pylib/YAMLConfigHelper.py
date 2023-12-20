import os
import shutil
import platform
from rich import print
from omegaconf import OmegaConf


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
            print("Trying to create config file.")
            print("  Making diretory: " + os.path.dirname(self.full_config_path))

            try:
                os.makedirs(os.path.dirname(self.full_config_path), exist_ok=True)
            except OSError as e:
                print(f"  Failed to create directory: {e}")
                exit(1)

            print("  Copying config file")

            try:
                shutil.copyfile(cfgsrc, self.full_config_path)
            except IOError as e:
                print(f"  [bold red]Failed to copy config file: {e}")
                exit(1)

            print("Config file installed to:")
            print(f"  {cfgdst}")
            print()
            print("Please edit the config file and re-run this command")
            print()
            exit(1)

    def load(self):
        try:
            with open(self.full_config_path, "r") as f:
                self.data = OmegaConf.load(f)
        except FileNotFoundError:
            return None

        return self.data

    def get_instance(self, name):
        return self.data.instances[f"{name}"]

    def get_instances(self):
        return self.data.instances

    def get_default_instance(self):
        self.get_instance(self.data.default_instance)

    def set_default_instance(self, instance):
        if self.data.instances.get(instance) is None:
            print("Instance not found.")
            exit(1)

        self.data.default_instance = instance

        try:
            with open(self.full_config_path, "w") as f:
                OmegaConf.save(self.data, f)
                print("Default instance set to: " + instance)
        except FileNotFoundError:
            print("Config file not found.")
