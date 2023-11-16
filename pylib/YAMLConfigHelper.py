import os
import yaml
import shutils


class YAMLConfigHelper:
    def __init__(self):
        self.filename = os.path.expanduser(
            os.path.join("~", "repos", "proxysqlctl", "config", "proxysqlctl.yaml")
        )
        # self.filename = os.path.expanduser(os.path.join("~", ".config", "proxysqlctl", "proxysqlctl.yaml"))
        self.data = None

    def install(self):
        cfgsrc = os.path.join("config", "proxysqlctl.yaml")
        cfgdst = self.filename

        if not os.path.exists(self.filename):
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            shutils.copyfile(cfgsrc, cfgdst)

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
