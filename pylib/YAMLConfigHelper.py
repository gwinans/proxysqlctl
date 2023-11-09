import os
import yaml


class YAMLConfigHelper:
    def __init__(self):
        # self.filename = os.path.expanduser(os.path.join("~", ".config", "proxysqlctl", "proxysqlctl.yaml")),
        self.filename = os.path.expanduser(
            os.path.join("~", "repos", "proxysql", "config", "proxysqlctl.yaml")
        )
        self.data = None

        try:
            with open(self.filename, "r") as f:
                self.data = yaml.safe_load(f).get("proxysqlctl")
        except FileNotFoundError:
            return None

        return data

    def get_instance(self, name):
        return self.data["instances"][f"{name}"]

    def get_default_instance(self):
        return self.data["default_instance"]
