import os
import yaml


class YAMLConfigHelper:
    def __init__(self):
        self.filename = os.path.expanduser(
            os.path.join("~", "repos", "proxysqlctl", "config", "proxysqlctl.yaml")
        )
        # self.filename = os.path.expanduser(os.path.join("~", ".config", "proxysqlctl", "proxysqlctl.yaml"))
        self.data = None

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
